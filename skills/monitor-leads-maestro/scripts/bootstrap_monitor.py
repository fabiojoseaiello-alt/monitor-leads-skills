#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower().strip()).strip("-")
    if not value:
        raise ValueError("slug inválido")
    return value

def write_new(path: Path, content: str) -> None:
    if path.exists():
        raise FileExistsError(f"arquivo já existe: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser(description="Cria o esqueleto de um monitor de leads.")
    parser.add_argument("--client", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    slug = slugify(args.slug)
    root = Path(args.output).expanduser().resolve() / slug
    if root.exists() and any(root.iterdir()):
        raise SystemExit(f"Destino não vazio: {root}")
    for folder in ("api/_assets", "data/private/enrichment", "data/private/attendance", "data/private/conversations", "scripts", "qa"):
        (root / folder).mkdir(parents=True, exist_ok=True)
    config = {
        "schema_version": 1,
        "client": {"name": args.client, "slug": slug, "timezone": "America/Sao_Paulo"},
        "brand": {"logo": "logo.png", "brand_dark": "#1d1010", "brand_main": "#6b1c22", "brand_bright": "#e25555", "accent": "#f1a33b"},
        "source": {"type": "google_sheets", "url": "", "tabs": [], "qualification_column": "", "establishment_column": "", "cnpj_column": ""},
        "conversation": {"provider": "chatwoot", "base_url_env": "CHATWOOT_BASE_URL", "token_env": "CHATWOOT_API_TOKEN", "account_id_env": "CHATWOOT_ACCOUNT_ID"},
        "crm": {"provider": "kommo", "base_url_env": "KOMMO_BASE_URL", "token_env": "KOMMO_API_TOKEN", "pipeline_id": ""},
        "enrichment": {"cnpj_providers": ["cnpj.ws", "minha_receita", "brasilapi"], "google_maps": True, "site": True, "instagram": True, "linkedin": True},
        "icp": {"segments": [], "volume_bands": [], "priority_rules": []},
        "privacy": {"publish_personal_contact": False, "conversation_delivery": "encrypted_authenticated_vault"},
        "publish": {"provider": "vercel", "project": slug, "domain": f"{slug}.vercel.app"}
    }
    manifest = {"schema_version": 1, "client_slug": slug, "stages": {name: {"status": "pending"} for name in ("ingestion", "enrichment", "attendance", "dashboard", "qa_publish")}}
    write_new(root / "monitor.config.json", json.dumps(config, ensure_ascii=False, indent=2) + "\n")
    write_new(root / "data/run-manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    write_new(root / ".gitignore", ".env\n*.tmp\ndata/private/\nqa/private-*\n")
    write_new(root / ".vercelignore", ".env\ndata/private\nscripts\nqa\n*.tmp\n")
    print(root)

if __name__ == "__main__":
    main()

