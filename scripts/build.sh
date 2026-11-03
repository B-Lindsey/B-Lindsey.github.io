#!/usr/bin/env bash
# Rebuild docs/ from sites/ and home/. See README.md.
set -euo pipefail
cd "$(dirname "$0")/.."
exec python3 scripts/build.py
