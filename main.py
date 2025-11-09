import modelo_ia as IA;
import bibliotecas;

biblio_bot = IA.BliblioAi(bibliotecas.lerBibliotecas()) 

while True:
    user_message = input()
    print(biblio_bot.fazer_pergunta(user_message))
    