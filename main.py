"""Leia o README primeiro antes de colocar o codigo a funcionar, pois la explico como pensei para criar o projeto como um todo.
Vou criar varios ficheiros em que em cada um vai ser uma classe, aqui ira ser a classe main onde todo a estrutura vai se interligar,
ou seja aqui é onde todo o codigo que farei nas outras classes se ira juntar e fazer o programa rodar, prefiro fazer desta forma devido
a ser parecido como funciona o java, e tambem assim consigo ter o codigo todo organizado de forma coerente para quem quiser fazer alguma 
alteração no codigo"""

from menu import Menu
from parking import Floor


class Main:
    def __init__(self, clients):
        self.menu = Menu(clients)
        self.clients = clients
        
        
        

    def run(self):
       self.menu.show_menu()

if __name__ == "__main__":
    
    clients = []
    main = Main(clients)  
    main.run()

    