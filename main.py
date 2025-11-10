import modelo_ia as IA;
import bibliotecas;
from rich.console import Console 
from rich.markdown import Markdown

console = Console()


biblio_bot = IA.BliblioAi(bibliotecas.lerBibliotecas()) 
print("\n--- BiblioBot pronto! Digite 'sair' para terminar. ---")

while True:
    user_message = input("Você: ")
    
    if(user_message.strip().lower() == "sair"):
        print("BiblioBot: Até a próxima! 🤖")
        break

    resposta = Markdown(biblio_bot.fazer_pergunta(user_message))
    print("BiblioBot:", end = " ")
    console.print(resposta)