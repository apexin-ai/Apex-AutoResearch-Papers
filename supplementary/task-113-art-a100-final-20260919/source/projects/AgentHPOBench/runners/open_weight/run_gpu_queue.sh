#!/usr/bin/env bash
set -u -o pipefail

GPU_ID="${1:?gpu id}"
shift

HERE="$(cd "$(dirname "$0")" && pwd)"
RUNNER="$HERE/run_model_seed.sh"

if [ $(( $# % 2 )) -ne 0 ]; then
  echo "Queue entries must be model/seed pairs." >&2
  exit 2
fi

echo "=== GPU QUEUE START $(date -Is) gpu=$GPU_ID entries=$(($# / 2)) ==="
rc=0
while [ "$#" -gt 0 ]; do
  model="$1"
  seed="$2"
  shift 2
  bash "$RUNNER" "$model" "$seed" "$GPU_ID" || rc=1
done
echo "=== GPU QUEUE END $(date -Is) gpu=$GPU_ID rc=$rc ==="
exit "$rc"
