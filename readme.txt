Data de inicio do projeto 22/07/2023
Data de termino do projeto 28/08/2023

Funcionalidades das classes

Classe Main:

    Nesta classe é onde o codigo todo se junta e o corre podendo omitir todo o restante codigo das classes , funcionada exatamente como a classe main em java.

Classe Client:

    Seria para ser a classe veiculo, mas como optei por criar mais variaves a classe que eram parecidas com os dados de um cliente acabei por criar com este nome.
    Nesta classe podemos varios metodos:
        
    def __init__:
        Metodo presente em todas as classes, chamado tambem construtor pois é aqui que iniciamos o estado inicial do nosso objeto
    
    def add_cost_to_history:
        Metodo criado com a intenção de adicionar o custo pago ao historico do mesmo, ou seja quando o cliente finaliza o pagamento o mesmo e adicionado ao historico no que pode ser
        visto de futuro , ñ esta completamente funcional pois a partir do momento que damos stop no programa o mesmo ñ armazena os dados em um banco de dados (ainda ñ aprendi a faze-lo).
    
    def registration:
        Metodo que faz o registo de novos cliente, pedindo todos os dados como input, tambem pode ser utilizado a funcao de criação automatica com a bibliote random, foi uma forma 
        que utilizei para fazer testes de forma mais rapida.

    def show_clients:
        Metodo que procura os cliente pelo nome, id_number e license_plate, de forma a sabermos alguns dados dos mesmos.

    def choose_parking_spot:
        Metodo utilizado para mostrar os lugares disponiveis por meio de uma tabela, onde podemos escolher o andar e automaticamente e proposto o melhor lugar para o nosso tipo de 
        cliente, apos aceitar estacionar o registo é efetuado e automaticamente atualizado os lugares por tipo quando formos ver os mesmos no "Park Administration" e def verify_park_availability_by_type
        , automaticamente apos escolher o lugar comeca a ser contado o tempo com o registo da hora e data em tempo real utilizando a biblioteca datetime.
    
    def customer_exists:
        Metodo utilizado para saber se o cliente ja existe na base de dados, caso ñ exista é perguntado se deseja se registration
    
    def payment_done:
        Metodo utilizado para quando o pagamento for efetuado com sucesso

    def payment_coupon:
        Metodo utilizado para quando o pagamento for feito com um cupao e o mesmo for aceite

Classe Parking:

    def __init__:
        Igual ao da classe client

    def time_to_minutes:
        Metodo utilizado para passar horas para minutos

    def calculate_charge:
        Metodo onde e calculado o quanto o cliente tem a pagar dependendo do tipo de cliente.







# Não esquecer de criar a informação do que e cada coluna na classe floor dentro da classe parking