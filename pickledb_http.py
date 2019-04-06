#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading
import pickledb

import sys

http_port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
db_file = sys.argv[2] if len(sys.argv) > 2 else ''
db = pickledb.load(db_file, False)

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        uri = self.path
        message = 'Invalid_Request'
        if uri.startswith('/get/'):
            kv = uri[5:].split('/')
            if len(kv) == 1:
                message = db.get(kv[0])
                if message == False:
                    message = ''
        elif uri.startswith('/set/'):
            kv = uri[5:].split('/')
            if len(kv) == 2:
                message = str(db.set(kv[0], kv[1]))
        self.wfile.write(message.encode('utf-8'))
        #self.wfile.write('\n')
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', http_port), Handler)
    print('Starting server at 0.0.0.0:{}, use <Ctrl-C> to stop'.format(http_port))
    server.serve_forever()
