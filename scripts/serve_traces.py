#!/usr/bin/env python3
"""Serve the static research trace viewer on localhost."""
import argparse
import functools
import http.server
from pathlib import Path
import webbrowser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--open", action="store_true", help="Open the viewer in your browser")
    args = parser.parse_args()
    directory = Path(__file__).resolve().parents[1]
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(directory))
    with http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        url = f"http://127.0.0.1:{server.server_port}/traces/"
        print(f"Research trace browser: {url}\nPress Ctrl+C to stop.", flush=True)
        if args.open:
            webbrowser.open(url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
