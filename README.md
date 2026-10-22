# Projeto 1: Inspetor de site

### Objetivo

Você completa o Inspetor de site, o script da ponte. Ele pede uma lista de endereços ao site de laboratório e mostra, para cada um, o código de status e se usa HTTPS. Assim você prova que sabe ler uma resposta e reconhecer um endereço que usa HTTPS.

### Entregável

Um repositório público no GitHub com o `inspetor.py` completo. O repositório já traz o código-base pronto, menos as 3 partes marcadas, e o site de laboratório. Você completa as 3 partes marcadas com `>>> PARTE` no `inspetor.py`:

- Parte 1: a função `pedir`, que pede a página e devolve o código de status.
- Parte 2: a função `usa_https`, que diz se o endereço começa com `https://`.
- Parte 3: a função `inspecionar`, que repete tudo para a lista inteira.

A saída esperada, com o texto exato:

```
Inspetor de site
--- https://localhost:8443/
código de status: 200
usa HTTPS: sim
--- http://localhost:8080/
código de status: 200
usa HTTPS: não
--- http://localhost:9999/
não achei o site; confira o endereço
usa HTTPS: não
```

Antes de entregar, rode `python3 verificar.py`: ele diz `OK` ou `FALHOU` para cada critério abaixo.

### Critérios de "pronto"

- `pedir` devolve 200 para `http://localhost:8080/` e para `https://localhost:8443/`.
- `usa_https` devolve `True` para `https://` e `False` para `http://`.
- A saída é igual à saída esperada: os 3 endereços, na ordem, cada um com a linha `usa HTTPS`.
- O endereço sem site mostra `não achei o site; confira o endereço` e o script não para.

### Ferramentas esperadas

- Python 3, só com a biblioteca padrão (`urllib.request` e `ssl`).
- Dois terminais: um para `python3 lab/servidor.py`, outro para o inspetor.
- Referências: documentação do Python sobre `urllib.request.urlopen` e sobre `str.startswith`.

## Como rodar

Você precisa do Python 3 instalado. Abra dois terminais na pasta do projeto.

No primeiro, ligue o site de laboratório e deixe aberto:

```
python3 lab/servidor.py
```

No segundo, rode o inspetor e confira os critérios:

```
python3 inspetor.py
python3 verificar.py
```

No Windows, se `python3` não funcionar, use `py` no lugar.

## O que já vem pronto

- `lab/`: o site de laboratório (não mexa).
- `inspetor.py`: o código-base. Procure `>>> PARTE` e complete as 3 partes.
- `verificar.py`: confere cada critério e diz qual parte ainda falta.
