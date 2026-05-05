# Spencer Ventures Dashboard

Shared business portfolio dashboard for ventures we're working on together.

## Setup (one-time)

Paste this into Claude Code:

```
Clone https://github.com/W1s3r/spencer-ventures.git into my home directory. Then create a macOS .app shortcut called "Spencer Ventures" on my Desktop. When launched, the app should: cd to ~/spencer-ventures, git pull, kill any existing process on port 3847, start server.py in the background (python3 server.py), wait for it to be ready, then open http://localhost:3847/index.html in Chrome app mode (--app flag, no tabs or URL bar). If Chrome isn't available, fall back to Safari. After creating the .app, open it to verify it works.
```

## View the dashboard

```bash
open ~/spencer-ventures/index.html
```

## Syncing shared tasks

Tasks auto-sync when you add, complete, or delete them. The local server writes to `tasks.json` and git-pushes in the background. The other person gets updates on their next launch (the app pulls on open).

## How it stays updated

The hourly cron auto-pulls business data and tasks. Or manually:

```bash
cd ~/spencer-ventures && git pull
```

## What's here

- **Patent Launch** — AI patent drafting service (patentlaun.ch)
- **Smart Strap** — EMG gesture-sensing watch band
- **SMART TECH** — Parent company, spatial smart home (VA LLC)
- **LaunchAI** — AI business launch app (iOS/watchOS)
