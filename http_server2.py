from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        f=open("hello.html","rb")
        self.wfile.write(f.read())

httpd = HTTPServer(('localhost', 8080), MyRequestHandler)
httpd.serve_forever()
