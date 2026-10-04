"""Small notebook-faithful prediction service. Run with: python server.py"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import json

INTERCEPT = 42.444772590839705
COEFFICIENT = 21.54587147

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != '/api/predict':
            self.send_error(404, 'Not found'); return
        try:
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length))
            temperature = float(body['temperature'])
            if not -50 <= temperature <= 100:
                raise ValueError('temperature must be between -50 and 100')
            prediction = INTERCEPT + COEFFICIENT * temperature
            payload = {'prediction': prediction, 'feature': 'Temperature', 'target': 'Revenue', 'model': 'LinearRegression', 'model_version': 'notebook-r1'}
            raw = json.dumps(payload).encode()
            self.send_response(200); self.send_header('Content-Type', 'application/json'); self.send_header('Content-Length', str(len(raw))); self.end_headers(); self.wfile.write(raw)
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            raw = json.dumps({'error': 'Invalid Temperature input.'}).encode()
            self.send_response(400); self.send_header('Content-Type', 'application/json'); self.send_header('Content-Length', str(len(raw))); self.end_headers(); self.wfile.write(raw)
    def do_GET(self):
        if self.path == '/api/health':
            raw=json.dumps({'status':'ok','model':'LinearRegression','feature':'Temperature'}).encode()
            self.send_response(200); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(raw))); self.end_headers(); self.wfile.write(raw); return
        super().do_GET()

if __name__ == '__main__':
    print('Shri Ice Cream running at http://0.0.0.0:8000')
    ThreadingHTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
