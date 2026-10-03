#!/usr/bin/env bash
set -euo pipefail

PORT="${PORT:-8080}"

python3 -c "from app import app; app.run(port=$PORT)"