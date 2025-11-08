from google import genai;
from pathlib import Path;

PASTA_RAIZ = Path(__file__).parent



class BliblioAi:
    def __init__(self, bibliotecas: list[dict[str,any]]):
        with open(PASTA_RAIZ / "system-instruction.md", 'r', encoding='utf-8') as f:
            system_instruction = f.read()
        