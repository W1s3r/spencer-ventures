#!/bin/bash
# Sync tasks for Spencer Ventures dashboard
# Usage: ./sync.sh (after clicking "Sync" button in the dashboard)

cd "$(dirname "$0")" || exit 1

# Pull latest first
git pull --rebase 2>/dev/null

# Paste clipboard into tasks.json
if command -v pbpaste &>/dev/null; then
  pbpaste > tasks.json
elif command -v xclip &>/dev/null; then
  xclip -selection clipboard -o > tasks.json
else
  echo "No clipboard tool found. Paste JSON into tasks.json manually."
  exit 1
fi

# Validate it's valid JSON
if ! python3 -c "import json; json.load(open('tasks.json'))" 2>/dev/null; then
  echo "Error: clipboard content is not valid JSON. Did you click Sync first?"
  git checkout tasks.json 2>/dev/null
  exit 1
fi

# Commit and push
git add tasks.json
git commit -m "sync tasks — $(date '+%Y-%m-%d %H:%M')"
git push

echo "Tasks synced."
