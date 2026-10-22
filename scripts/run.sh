#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=src exec uvicorn beebridge.main:app --app-dir src --host 0.0.0.0 --port "${PORT:-8000}"
