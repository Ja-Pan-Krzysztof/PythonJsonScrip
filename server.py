from http.server import HTTPServer, SimpleHTTPRequestHandler
import database
#tak...
db_name = "chuwel"
#krzychu + Pawel po odcięciu pierszej sylaby wychodzi chuwel


class LocalServer(SimpleHTTPRequestHandler):
    #klasa
    @staticmethod 
    def readhtml(path):
        with open(path,"r")as f:
            return f.read()
    def do_Get(self):
        if self.path =="/":
            
            self.path="./templates/index.html"
            file = self.readhtml(self.path)
            self.send_response(200,"OK");
            self.end_headers();
            self.wfile.write(bytes(file,"utf8"))
 


class HostServer:
    #clss to klasa 
    def __init__(self, host: str = '192.168.0.199', port: int = 8000):
        #tak.................
        self.port = port
        self.host = host

    def starhost(self) -> HTTPServer:
        #(-:
        return HTTPServer((self.host, self.port), LocalServer)
        #zwraca localny serwer 
        #loca
    
    def stophost(self):
        return self.starhost().shutdown()
        


        
        


        
#Autor pracy copyright by : Pawel Kuczmik czli paweltheriperr and Pan krzychu czyli ja 