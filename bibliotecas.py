from pathlib import Path;
from constantes import PASTA_RAIZ;
import json;

pasta_bibliotecas = PASTA_RAIZ / "bibliotecas"

def lerBibliotecas():
    bibliotecas = []
    print("Carregando bibliotecas...\n")
    for arquivo in pasta_bibliotecas.glob("*.json"):
        print(f"Carregando {arquivo.name}")
        try:
            with open(arquivo, "r", encoding="utf-8" ) as biblioteca:
                leitura = json.load(biblioteca)
                bibliotecas.append(leitura)
            print("Sucesso ✔")
        except:
            print("Falha ao carregar biblioteca 🔴")
    return bibliotecas
