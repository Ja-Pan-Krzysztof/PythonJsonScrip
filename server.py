from http.server import HTTPServer, SimpleHTTPRequestHandler

from database import User
import cgi
import logging.config
from io import BytesIO

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

''' MySQL
    :keyword here will be connection with MySQL
    :keyword and code below will be delete
'''

db_name = "chuwel"

u = User('ja', 'ja.db')
u.conn()
u.create_table()
u.disconn()


class LocalServer(SimpleHTTPRequestHandler):
    logger.info('Server working')

    @staticmethod
    def readhtml(path):
        try:
            with open(path) as f:
                file = f.read()

        except Exception as e:
            file = e

        return file

    def do_GET(self):
        if self.path == "/":
            template = "./templates/index.html"
            file = self.readhtml(template)
            self.send_response(200, "OK")
            self.end_headers()
            self.wfile.write(bytes(file, "utf8"))

        if self.path == '/success':
            pass

    def do_POST(self):  # xD
        if self.path == '/success':  # xD
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )

            name = form.getvalue('name')
            surname = form.getvalue('surname')

            template = './templates/success.html'
            file = self.readhtml(template)

            self.send_response(200, 'OK')
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(file, "utf8"))

        if self.path == "/ajax":
            form = cgi.FieldStorage(
                fp=BytesIO(bytes(self.rfile)),
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'},
                encoding='utf-8'
            )

            name = form.getvalue('name')
            surname = form.getvalue('surname')
            print(name, surname)

            print('It\'s work !')


class HostServer:
    def __init__(self, host: str = '192.168.0.111', port: int = 8000):
        self.port = port
        self.host = host

    def starhost(self) -> HTTPServer:
        return HTTPServer((self.host, self.port), LocalServer)

    def stophost(self):
        return self.starhost()\
            .shutdown()
