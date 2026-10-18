#!/usr/bin/env bash
set -euo pipefail

output=$(python3 -m pytest -q test_app.py) || {
    echo "$output"
    exit 1
}
echo "$output"
passed=$(echo "$output" | grep -oE '[0-9]+ passed' | grep -oE '[0-9]+' || true)
failed=$(echo "$output" | grep -oE '[0-9]+ failed' | grep -oE '[0-9]+' || true)
passed=${passed:-0}
failed=${failed:-0}
echo "TESTS: $passed/$((passed + failed))"