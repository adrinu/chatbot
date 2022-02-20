from socketserver import TCPServer, UDPServer, BaseRequestHandler
    
class ChatBot(BaseRequestHandler):
    
    def handle(self):
        while True:
            msg = self.request.recv(1024)
            if msg == b'quit\n':
                break
            self.request.send(b'Message received: ' + msg)
    def greet(self):
        pass

        
        
if __name__ == "__main__":
    pass
    with TCPServer(('',9999), ChatBot) as server:
        server.serve_forever()
#     greeting_msg = """
# __| |____________________________________________| |__
# (__   ____________________________________________   __)
#    | |                                            | |
#    | |             Welcome to ChatBot             | |
#    | |      Please select the following options   | |
#    | |                                            | |
#    | |                  1 - TCP                   | |
#    | |                  2 - UPD                   | |
#  __| |____________________________________________| |__
# (__   ____________________________________________   __)
#    | |                                            | |
#         """
 