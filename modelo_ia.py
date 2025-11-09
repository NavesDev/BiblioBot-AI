from google import genai;
from pathlib import Path;
from constantes import PASTA_RAIZ;

LIVROS_PREFIXO = "* "


# OBJETO PARA GERENCIAR O BIBLIOBOT
class BliblioAi:

    ## INICIALIZA A IA E SUA INSTRUÇÃO
    def __init__(self, bibliotecas: list[dict[str,any]]):
        with open(PASTA_RAIZ / "system-instruction.md", 'r', encoding='utf-8') as f:
            system_instruction = f.read()

        base_de_conhecimento = ""
        for biblioteca in bibliotecas:
            ### ENTRE PARÊNTESES O PYTHON CONCATENA AS STRINGS, DESDE QUE NÃO TENHA VÍRGULA
            biblioteca_titulo = (
            f"### {biblioteca['nome']}\n"
            f"(Local: {biblioteca['local']})\n"
            )
            
            ### OQUE A IA ESPERA DOS LIVROS
            #### * [Título] | [Autor] | [Ano de Publicação] | [Total de Empréstimos (Histórico)] | [Total de Cópias (no Acervo)] | [Cópias Disponíveis (Agora)] | [Categorias]

            biblioteca_livros = ""
            for livro in biblioteca["livros"]:
                biblioteca_livros += f"{LIVROS_PREFIXO} {livro['titulo']} | {livro['autor']} | {livro['ano_publicacao']} | {livro['empréstimos']} | {livro['quantidade_total']} | {livro['quantidade_disponivel']} | {livro['categorias']}\n"
            
            base_de_conhecimento += biblioteca_titulo + biblioteca_livros + "\n"
        
        system_instruction = system_instruction.format(base_de_conhecimento = base_de_conhecimento)

        self.system_instruction = system_instruction

            
       
