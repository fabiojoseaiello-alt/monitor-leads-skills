#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

PLACEHOLDER = re.compile(r"\{\{|TODO|CHANGE_ME|Nome do cliente", re.I)
PRIVATE_KEYS = {"email", "phone", "telefone", "celular", "messages", "mensagens", "token", "cookie"}

def walk(value, path="$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield f"{path}.{key}", key, child
            yield from walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")

def main() -> None:
    parser = argparse.ArgumentParser(description="Valida um monitor antes da publicação.")
    parser.add_argument("project")
    args = parser.parse_args()
    root = Path(args.project).expanduser().resolve()
    errors, warnings = [], []
    for relative in ("monitor.config.json", "data/run-manifest.json", "data/leads.json", "index.html", ".vercelignore"):
        if not (root / relative).is_file():
            errors.append(f"arquivo ausente: {relative}")
    config_path = root / "monitor.config.json"
    if config_path.is_file():
        config = json.loads(config_path.read_text(encoding="utf-8"))
        if PLACEHOLDER.search(json.dumps(config, ensure_ascii=False)):
            errors.append("monitor.config.json ainda contém placeholder")
    manifest_path = root / "data/run-manifest.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for stage, state in manifest.get("stages", {}).items():
            if state.get("status") not in {"complete", "partial"}:
                errors.append(f"estágio não concluído: {stage}={state.get('status')}")
    public_path = root / "data/leads.json"
    if public_path.is_file():
        public = json.loads(public_path.read_text(encoding="utf-8"))
        for item_path, key, value in walk(public):
            if key.lower() in PRIVATE_KEYS and value not in (None, "", [], {}):
                errors.append(f"possível dado privado no payload público: {item_path}")
    ignore_path = root / ".vercelignore"
    if ignore_path.is_file() and "data/private" not in ignore_path.read_text(encoding="utf-8"):
        errors.append(".vercelignore não exclui data/private")
    html_path = root / "index.html"
    if html_path.is_file():
        html = html_path.read_text(encoding="utf-8", errors="replace")
        if PLACEHOLDER.search(html):
            errors.append("index.html ainda contém placeholder")
        if 'rel="icon"' not in html and "rel='icon'" not in html:
            warnings.append("favicon não declarado")
    report = {"ok": not errors, "errors": errors, "warnings": warnings}
    report_path = root / "qa/report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["ok"] else 1)

if __name__ == "__main__":
    main()

