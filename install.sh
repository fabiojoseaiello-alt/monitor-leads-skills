#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source_root="$repo_root/skills"
destination="${1:-${CODEX_HOME:-$HOME/.codex}/skills}"

mkdir -p "$destination"

for skill in "$source_root"/monitor-leads-*; do
  name="$(basename "$skill")"
  target="$destination/$name"
  if [[ -e "$target" ]]; then
    echo "A skill '$name' já existe em '$target'. Remova-a ou escolha outro destino." >&2
    exit 1
  fi
  cp -R "$skill" "$target"
  echo "Instalada: $name"
done

echo "Skills instaladas em: $destination"

