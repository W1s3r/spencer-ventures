#!/usr/bin/env python3
"""Tiny local server for Spencer Ventures dashboard.
Serves static files + one POST endpoint that writes tasks.json and git-pushes."""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json, subprocess, os, threading

PORT = 3847
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/tasks':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)

            # Validate JSON
            try:
                tasks = json.loads(body)
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"error":"invalid json"}')
                return

            # Write tasks.json
            with open(os.path.join(DIR, 'tasks.json'), 'w') as f:
                json.dump(tasks, f, indent=2)
                f.write('\n')

            # Git commit + push in background (non-blocking)
            threading.Thread(target=git_sync, daemon=True).start()

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
            return

        self.send_response(404)
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def log_message(self, format, *args):
        pass  # silence request logs

def git_sync():
    try:
        subprocess.run(['git', 'pull', '--rebase'], cwd=DIR, capture_output=True, timeout=15)
        subprocess.run(['git', 'add', 'tasks.json'], cwd=DIR, capture_output=True)
        result = subprocess.run(
            ['git', 'commit', '-m', 'sync tasks'],
            cwd=DIR, capture_output=True, timeout=10
        )
        if result.returncode == 0:
            subprocess.run(['git', 'push'], cwd=DIR, capture_output=True, timeout=15)
    except Exception:
        pass  # fail silently, tasks are still saved locally

if __name__ == '__main__':
    os.chdir(DIR)
    print(f'Spencer Ventures → http://localhost:{PORT}')
    HTTPServer(('127.0.0.1', PORT), Handler).serve_forever()
