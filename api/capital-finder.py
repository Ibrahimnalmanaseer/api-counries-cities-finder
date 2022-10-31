
from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        # date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        api_path=self.path
        url_components=parse.urlsplit(api_path)
        query=parse.parse_qsl(url_components.query)
        print(query)
        self.wfile.write(str(query).encode())
        return