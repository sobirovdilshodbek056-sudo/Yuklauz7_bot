from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import threading
import time

PORT = int(os.getenv("PORT", "8080"))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        pass  # Suppress HTTP logs

def run_server():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Starting keepalive on port {PORT}")
    server.serve_forever()

if __name__ == "__main__":
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    while True:
        time.sleep(1)
