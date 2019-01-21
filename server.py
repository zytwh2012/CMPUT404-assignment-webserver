#  coding: utf-8 
import socketserver
from datetime import datetime
# Copyright 2013 Abram Hindle, Eddie Antonio Santos
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/



class MyWebServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("request")
        self.data = self.request.recv(1024).strip()
        print ("Got a request of: %s\n" % self.data)
        requests = self.data.split()
        location = requests[1]
        
        if location == bytearray("/base.css",'utf-8'):
            with open('./www/base.css','r', encoding="utf-8") as f:
                css = f.read()
                res='''HTTP/1.1 200 OK/r/n
                    Content-Type: text/css/r/n
                    Connection: Closed/r/n''' +css

                 self.request.sendall(bytearray(req, 'utf-8'))

        elif location == bytearray("/",'utf-8') or location == bytearray("/index.html",'utf-8'):
            with open('./www/index.html','r', encoding="utf-8") as f:
                html = f.read()
                res='''HTTP/1.1 200 OK/r/n
                   Content-Type: text/htmk/r/n
                   Connection: Closed/r/n''' +html
                
                self.request.sendall(bytearray(req, 'utf-8'))
            


        elif location == bytearray("/deep/",'utf-8') or location == bytearray("/deep/index.html",'utf-8'):
            with open('./www/deep/index.html','r', encoding="utf-8") as f:
                html = f.read()
                self.request.sendall(bytearray("HTTP/1.1 ",'utf-8'))
                self.request.sendall(bytearray("200 OK\n",'utf-8'))
                self.request.sendall(bytearray("Content-Type: text/html\n",'utf-8'))
                self.request.sendall(bytearray("Connection: Closed\n",'utf-8'))
                self.request.sendall(bytearray(html, 'utf-8'))

           
            
        elif location == bytearray("/deep/deep.css",'utf-8'):
            with open('./www/deep/deep.css','r', encoding="utf-8") as f:
                css = f.read()
                self.request.sendall(bytearray("HTTP/1.1 ",'utf-8'))
                self.request.sendall(bytearray("200 OK\n",'utf-8'))
                self.request.sendall(bytearray("Content-Type: text/css\n",'utf-8'))
                self.request.sendall(bytearray("Connection: Closed\n",'utf-8'))
                self.request.sendall(bytearray(css, 'utf-8'))

        elif location == bytearray("/hardcode/",'utf-8') or location == bytearray("/hardcode/index.html",'utf-8'):
            with open('./www/hardcode/index.html','r', encoding="utf-8") as f:
                html = f.read()
                self.request.sendall(bytearray("HTTP/1.1 ",'utf-8'))
                self.request.sendall(bytearray("200 OK\n",'utf-8'))
                self.request.sendall(bytearray("Content-Type: text/html\n",'utf-8'))
                self.request.sendall(bytearray("Connection: Closed\n",'utf-8'))  
                self.request.sendall(bytearray(html,'utf-8'))

        elif location == bytearray("/hardcode/deep.css",'utf-8'):
            self.request.sendall(bytearray("HTTP/1.1 ",'utf-8'))
            self.request.sendall(bytearray("200 OK\n",'utf-8'))
            self.request.sendall(bytearray("Content-Type: text/css\n",'utf-8'))
            self.request.sendall(bytearray("Connection: Closed\n",'utf-8'))
         
        else:
            self.request.sendall(bytearray("HTTP/1.1 ",'utf-8'))
            self.request.sendall(bytearray("404 Not FOUND\n",'utf-8'))
            self.request.sendall(bytearray("Connection: Closed\n",'utf-8'))
            self.request.sendall(bytearray('''
                                            <!DOCTYPE HTML">
                                            <html>
                                            <head>
                                            <title>404 Page Not Found</title>
                                            </head>
                                            <body>
                                            <h1>Not Found</h1>
                                            </body>
                                            </html>''','utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 8080
    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = socketserver.TCPServer((HOST, PORT), MyWebServer)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
