#!/usr/bin/env bash
set -euo pipefail

python3 -m pytest -q test_app.py
echo "TESTS: 3/3"