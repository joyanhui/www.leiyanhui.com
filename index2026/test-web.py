#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 19011
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def log_message(self, format, *args):
        pass

def main():
    try:
        with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
            print(f"http://127.0.0.1:{PORT}/index2026.html")
            httpd.serve_forever()
    except OSError as e:
        if "Address in use" in str(e):
            print(f"Port {PORT} in use")
        exit(1)

if __name__ == "__main__":
    main()
