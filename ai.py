
# CLASSE PARA ESTRUTURA BÁSICA DE LVIROS
class Livro:
    def __init__(self,id,titulo,categoria):
        self.titulo = titulo
        self.categoria = categoria
        self.id = id

# CLASSE PARA PARÂMETROS DE BUSCA (PARA FICAR COM O CÓDIGO MAIS LEGÍVEL)
class BuscaParams:
    POR_ID = 0
    POR_TITULO = 1
    POR_CATEGORIA = 2
    BUSCA_GERAL = 3


# CLASSE PARA GERENCIAR LIVROS COM EFICIÊNCIA

## CONSTANTES DE PARA NÍVEL DE PRIORIDADE NA BUSCA 
## P -> PRIORIDADE
P_ID = 0
P_TITULO = 1
P_CATEGORIA = 2

class Biblioteca:
    livros = []
    def __init__(self,nome = "Sem Nome"): 
        self.id_atual = 1

    def adicionar_livro(self, titulo, categoria):
        self.livros.append(Livro(self.id_atual,titulo,categoria))
        self.id_atual+=1
    def buscar_livro(self, parametro_busca):
        if(len(self.livros) >0 ):
            if(parametro_busca == BuscaParams.BUSCA_GERAL):
                pass
            elif(parametro_busca == BuscaParams.POR_TITULO):
                pass
            elif(parametro_busca == BuscaParams.POR_ID):
                pass
            elif (parametro_busca == BuscaParams.POR_CATEGORIA):
                pass
        else:
            return False;
            