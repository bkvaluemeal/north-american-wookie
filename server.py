from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

handler = CGIHTTPRequestHandler
httpd = HTTPServer(("", 80), handler)

print('Server started on port 80')

httpd.serve_forever()
