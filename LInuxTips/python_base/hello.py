#! python3
"""Hello World Multi Languages.

Dependendo da língua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

TEnha a variável LANG devidamente configurada, ex:

    export LANG = pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Geovane Dias de Araujo"
__license__ = "Unlicence"

import os

current_language = "en_US"

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao,Mondo!"

print(msg)
