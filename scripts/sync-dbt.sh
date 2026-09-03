#!/usr/bin/env bash
# Re-vendor dbt/ from continuo-demo's finance project. Single source of truth is
# continuo-demo. Dockerfile*/entrypoint.sh excluded — Airflow runs dbt directly.
set -euo pipefail
SRC="${1:-../continuo-demo/services/finance}"
HERE="$(cd "$(dirname "$0")/.." && pwd)"
rsync -a --delete \
  --exclude 'Dockerfile' --exclude 'Dockerfile.local' --exclude 'entrypoint.sh' \
  "$SRC/" "$HERE/dbt/"
echo "vendored $SRC -> $HERE/dbt"
