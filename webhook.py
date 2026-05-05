from http.server import BaseHTTPRequestHandler, HTTPServer

print("🔥 Webhook started on port 5001")

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length).decode()

        print("🚨 ALERT RECEIVED:", data)

        with open("/home/ubuntu/incidents.log", "a") as f:
            f.write("ALERT: " + data + "\n")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

HTTPServer(("0.0.0.0", 5001), Handler).serve_forever()
