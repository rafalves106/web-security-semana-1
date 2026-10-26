"""Inspetor de site: para cada endereco da lista, mostra o código de status e se usa HTTPS.
Procure por ">>> PARTE" neste arquivo: são as 3 partes que faltam. O resto já funciona."""
import os
import ssl
from urllib.request import urlopen

# O laboratório usa um certificado proprio. Esta linha diz ao Python para confiar nele.
CONTEXTO = ssl.create_default_context(cafile=os.path.join(os.path.dirname(os.path.abspath(__file__)), "lab", "cert.pem"))

ENDERECOS = ["https://localhost:8443/", "http://localhost:8080/", "http://localhost:9999/"]


def pedir(endereco):
    """Pede a página ao site e devolve o código de status (um numero)."""
    resposta = urlopen(endereco, context=CONTEXTO)
    return resposta.status


def usa_https(endereco):
    """Devolve True se o endereco usa HTTPS e False se não usa."""
    HTTPS = endereco.startswith("https://")
    return HTTPS


def inspecionar(enderecos):
    print("Inspetor de site")
    for end in enderecos:
        print("--- " + end)
        
        try:
            print("código de status: " + str(pedir(end)))
        except OSError:
            print("não achei o site; confira o endereço")
        
        if usa_https(end):
            print("usa HTTPS: sim")
        else:
            print("usa HTTPS: não")
    # >>> PARTE 3: para cada endereco da lista, mostre "--- " e o endereco.
    # Depois, dentro de um try, mostre "código de status:" e o resultado de pedir(endereco).
    # Se der OSError, mostre "não achei o site; confira o endereço".
    # No fim de cada volta, mostre "usa HTTPS:" e "sim" ou "não".


if __name__ == "__main__":
    inspecionar(ENDERECOS)
