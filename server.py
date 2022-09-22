from http.server import HTTPServer, SimpleHTTPRequestHandler
import database
import cgi

# tak...
db_name = "chuwel"


# krzychu + Pawel po odcięciu pierszej sylaby wychodzi chuwel


class LocalServer(SimpleHTTPRequestHandler):

    # klasa
    @staticmethod
    def readhtml(path):
        # with open(path,"r")as f:
        # return f.read()
        try:
            with open(path) as f:
                file = f.read()

        except Exception as e:
            file = e

        return file

    def do_GET(self):
        if self.path == '/':
            self.path = './templates/index.html'
            file = self.readhtml(self.path)
            self.send_response(200, "OK")
            self.end_headers()
            self.wfile.write(bytes(file, "utf8"))

    def do_POST(self):
        if self.path == '/success':
            ctype, pdict = cgi.parse_multipart(self.headers.get('content-type'))
            pdict['name'] = bytes(pdict['name'], 'utf-8')

            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                name = fields.get("name")[0]
                # create table User if it runs first time else not<font></font>
                html = f"<html><head></head><body><h1>Form data successfully recorded!!!</h1></body></html>"
                self.send_response(200, "OK")
                self.end_headers()
                self.wfile.write(bytes(html, "utf-8"))


class HostServer:
    # clss to klasa
    def __init__(self, host: str = '192.168.0.111', port: int = 8000):
        # tak.................
        self.port = port
        self.host = host

    def starhost(self) -> HTTPServer:
        # (-:
        return HTTPServer((self.host, self.port), LocalServer)
        # zwraca localny serwer
        # loca

    def stophost(self):
        return self.starhost().shutdown()

# Autor pracy copyright by : Pawel Kuczmik czli paweltheriperr and Pan krzychu czyli ja
