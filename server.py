from http.server import HTTPServer, SimpleHTTPRequestHandler
import database
#tak...
db_name = "chuwel"
#krzychu + Pawel po odcięciu pierszej sylaby wychodzi chuwel


class LocalServer(SimpleHTTPRequestHandler):
    pass
#klasa 


class HostServer:
    #clss to klasa 
    def __init__(self, host: str = '192.168.0.111', port: int = 8000):
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