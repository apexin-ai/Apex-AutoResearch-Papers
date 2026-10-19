#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUTOREP_ROOT="${AUTOREP_ROOT:-$(cd "$SCRIPT_DIR/../../.." && pwd)}"
REPO_DIR="${REPO_DIR:-$AUTOREP_ROOT/repositories/llm.c}"
FINEWEB_VERSION="${FINEWEB_VERSION:-10B}"
DOWNLOAD_HELLASWAG="${DOWNLOAD_HELLASWAG:-1}"
FINEWEB_RETRIES="${FINEWEB_RETRIES:-20}"

if [[ ! -d "$REPO_DIR" ]]; then
  echo "Missing repo: $REPO_DIR" >&2
  exit 2
fi

cmd=(python3 dev/data/fineweb.py --version "$FINEWEB_VERSION")

echo "Repo: $REPO_DIR"
printf 'Command:'
printf ' %q' "${cmd[@]}"
printf '\n'
if [[ "$DOWNLOAD_HELLASWAG" == "1" ]]; then
  echo "Then: python3 dev/data/hellaswag.py"
fi

if [[ "${DRY_RUN:-0}" == "1" ]]; then
  exit 0
fi

cd "$REPO_DIR"
for attempt in $(seq 1 "$FINEWEB_RETRIES"); do
  echo "FineWeb attempt $attempt/$FINEWEB_RETRIES"
  if "${cmd[@]}"; then
    break
  fi
  if [[ "$attempt" == "$FINEWEB_RETRIES" ]]; then
    echo "FineWeb failed after $FINEWEB_RETRIES attempts" >&2
    exit 1
  fi
  sleep $((attempt * 10))
done
if [[ "$DOWNLOAD_HELLASWAG" == "1" ]]; then
  python3 dev/data/hellaswag.py
fi
