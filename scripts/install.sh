#!/usr/bin/env bash
set -euo pipefail

agent="codex"
scope="global"
source_path=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --agent)
      agent="$2"
      shift 2
      ;;
    --source)
      source_path="$2"
      shift 2
      ;;
    --project)
      scope="project"
      shift
      ;;
    --help|-h)
      echo "Usage: ./scripts/install.sh [--agent codex] [--source owner/repo] [--project]"
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

if ! command -v npx >/dev/null 2>&1; then
  echo "npx is required. Install a current Node.js release and try again." >&2
  exit 1
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_path="${source_path:-$repo_root}"

args=(
  --yes skills add "$source_path"
  --skill frontend-design-pro
  --agent "$agent"
  --yes
  --copy
)

if [[ "$scope" == "global" ]]; then
  args+=(--global)
fi

npx "${args[@]}"
echo "Frontend Design Pro installed. Restart the target agent before using it."
