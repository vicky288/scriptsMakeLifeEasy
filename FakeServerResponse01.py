import SocketServer
import SimpleHTTPServer

file_handle = open('resp_headers.txt','r')
class HttpReqHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/admin':
            self._set_headers()
            self.wfile.write('This is admin page')
        else:
            #SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
	    self._set_headers()
            self.wfile.write('This is admin page')

    def _set_headers(self):
        self.send_response(200)
	for line in file_handle:
		line = line.rstrip()
		values = line.split(':')
        	self.send_header(values[0], values[1])
        self.end_headers()
httpServer = SocketServer.TCPServer(('',23359), HttpReqHandler)
httpServer.serve_forever()

		
	
