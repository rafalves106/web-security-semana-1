"""Site de laboratorio do Projeto 1. So biblioteca padrao.
Respostas fixas: o endereco http://localhost:8080/ e o https://localhost:8443/ devolvem sempre a mesma pagina.
O certificado e a chave desta pasta foram criados so para o laboratorio e nao protegem nada de verdade.
Nao precisa mexer neste arquivo. Para ligar o site: python3 lab/servidor.py"""
import os
import ssl
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

PASTA = os.path.dirname(os.path.abspath(__file__))


class Lab(BaseHTTPRequestHandler):
    server_version = "LabHTTP/1.0"
    sys_version = ""

    def do_GET(self):
        corpo = b"<h1>Loja Lab</h1>\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

    def log_message(self, *args):
        pass


def servir_https():
    contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    contexto.load_cert_chain(os.path.join(PASTA, "cert.pem"), os.path.join(PASTA, "chave.pem"))
    servidor = HTTPServer(("127.0.0.1", 8443), Lab)
    servidor.socket = contexto.wrap_socket(servidor.socket, server_side=True)
    servidor.serve_forever()


if __name__ == "__main__":
    threading.Thread(target=servir_https, daemon=True).start()
    print("site de laboratorio ligado: http://localhost:8080/ e https://localhost:8443/ (Ctrl+C para parar)")
    HTTPServer(("127.0.0.1", 8080), Lab).serve_forever()
