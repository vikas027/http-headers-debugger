#!/usr/bin/env python

''' This script creates a http server on port 8000 and
returns the headers
https://gist.github.com/phrawzty/62540f146ee5e74ea1ab
'''

import SimpleHTTPServer
import SocketServer

PORT = 8000


class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_head()
        for h in self.headers:
            self.send_header(h, self.headers[h])
        self.end_headers()
        self.send_response(200, "")


Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

httpd.serve_forever()
