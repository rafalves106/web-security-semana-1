"""Confere os 3 criterios do Projeto 1 contra o site de laboratório (lab/servidor.py precisa estar ligado)."""
import io
import subprocess
import sys
from contextlib import redirect_stdout

import inspetor

OK, FALHA = "OK    ", "FALHOU"
falhas = 0


def criterio(nome, passou, dica):
    global falhas
    print(f"{OK if passou else FALHA} {nome}" + ("" if passou else f"  -> {dica}"))
    falhas += 0 if passou else 1


criterio("a) pede cada endereço e mostra o status",
         inspetor.pedir("http://localhost:8080/") == 200 and inspetor.pedir("https://localhost:8443/") == 200,
         "PARTE 1: pedir() deve devolver 200 nos dois endereços do laboratório")

criterio("b) marca HTTPS sim/não pelo início da URL",
         inspetor.usa_https("https://localhost:8443/") is True and inspetor.usa_https("http://localhost:8080/") is False,
         "PARTE 2: usa_https() deve devolver True para https:// e False para http://")

saida = subprocess.run([sys.executable, "inspetor.py"], capture_output=True, text=True, timeout=30).stdout.splitlines()
esperada = [
    "Inspetor de site",
    "--- https://localhost:8443/", "código de status: 200", "usa HTTPS: sim",
    "--- http://localhost:8080/", "código de status: 200", "usa HTTPS: não",
    "--- http://localhost:9999/", "não achei o site; confira o endereço", "usa HTTPS: não",
]
criterio("c) percorre a lista inteira", saida == esperada,
         "PARTE 3: a saída deve ter os 3 endereços, na ordem, com o texto exato do enunciado")

print("pronto" if falhas == 0 else f"{falhas} criterio(s) falhando")
sys.exit(1 if falhas else 0)
