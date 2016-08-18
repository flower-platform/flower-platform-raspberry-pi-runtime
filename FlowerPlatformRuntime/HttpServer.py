import time
import BaseHTTPServer
import threading
import urlparse

"""
documentation of HTttpServer component
"""
class HttpServer:

    onCommandReceived = None
    
    """
    @flowerChildParameter { ref = "port", type = "int" }
    """
    def __init__(self, port = 8080):
        self.port = port
     
    def setup(self) :
      self.server = BaseHTTPServer.HTTPServer(('', self.port), HttpRequestHandler)
      self.server.onCommandReceived = self.onCommandReceived
      thread = threading.Thread(target = self.server.serve_forever)
      thread.daemon = True
      thread.start()

    def loop(self) :
      return

    def stop(self) :
      self.server.shutdown()
      self.server.server_close()

class HttpRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
      if self.server.onCommandReceived is None:
          return
      event = HttpCommandEvent()
      event.client = self
      parseResult = urlparse.urlparse(self.path)
      event.url = parseResult.path[1:]
      event.parameters = urlparse.parse_qs(parseResult.query)
      event.url
      self.server.onCommandReceived(event)

class HttpCommandEvent:

    url = None

    client = None
    
    parameters = None