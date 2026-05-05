# Spencer Ventures Dashboard

Shared business portfolio dashboard for ventures we're working on together.

## Setup (one-time)

Paste this into Claude Code:

```
Clone https://github.com/W1s3r/spencer-ventures.git into my home directory, then set up a cron job that auto-pulls from origin/main every hour. Then create a macOS app shortcut called "Spencer Ventures" that opens the dashboard (spencer-ventures/index.html) in Chrome or Safari as a standalone window (no tabs, no URL bar — like a web app). Put the .app on my Desktop so I can drag it wherever I want (Dock, Applications, etc). After that, open the dashboard.
```

## View the dashboard

```bash
open ~/spencer-ventures/index.html
```

## How it stays updated

The hourly cron auto-pulls. Or manually:

```bash
cd ~/spencer-ventures && git pull
```

## What's here

- **Patent Launch** — AI patent drafting service (patentlaun.ch)
- **Smart Strap** — EMG gesture-sensing watch band
- **SMART TECH** — Parent company, spatial smart home (VA LLC)
- **LaunchAI** — AI business launch app (iOS/watchOS)
