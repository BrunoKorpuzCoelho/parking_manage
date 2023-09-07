Portugues
 
Data de inicio do projeto 22/07/2023
Data de termino do projeto 28/08/2023

Funcionalidades das classes

Classe Main:

    Nesta classe é onde o codigo todo se junta e o corre podendo omitir todo o restante codigo das classes , funcionada exatamente como a classe main em java.

Classe Client:

    Seria para ser a classe veiculo, mas como optei por criar mais variaves a classe que eram parecidas com os dados de um cliente acabei por criar com este nome.
    Nesta classe podemos varios metodos.
    Nesta classe temos como registar um cliente novo pedindo alguns dados do mesmo, podemos utilizar a forma automatica para o crir o numero de clientes que queremos de forma ramdom,
    utilizando a biblioteca ramdom, podemos ver os clientes que estão criados, aqui tambem se encontra o metodo para escolhermos o lugar de estacionamento onde entra a biblioteca, datetime
    que a mesma utiliza a hora e data local para quando o veiculo entrar no estacionamento, existe tambem um metodo para saber se o cliente ja existe registado, outro metodo para 
    quando fizermos o pagamento com sucesso, e outro para quando utilizamos um cupao que se encontra ativo pelo sistema( neste caso todos estao ativos e nao tem implementação
    para nao o estarem)

Classe Parking:

    Dentro da classe parking temos uma classe floor tambem pois achei que seria mais facil se separar as duas tendo cada uma delas os seus metodos especificos.
    Na classe parking temos metodos que vem se tem lugares disponiveis no parque , tambem podemos ver todos os andares e ver que lugares existem (e atualizado quando um 
    carro estaciona), temos um metodo para transformar 1h em 60 minutos para depois fazermos as contas do quanto tem que pagar cada cliente, esse metodo de calcular o pagamento
    tambem se encontra nesta classe.
    Dentro da classe floor temos um metodo que cria uma tabela utilizando a bibliote tabulate (se nao funcionar tera de a instalar no cmd do seu pc pois no meu ela teve de ser instalada
    dessa forma), essa tabela e integrada em outros metodos utilizado por outras classes, temos tambem a criação dos objetos floor que neste caso temos 6 andares e cada um tem os
    seus lugares disponiveis 

    exemplo:
    floor_0 = Floor(3,10,2,25,10,0)
    aqui temos os seguintes lugares(cada variavel tem o seguinte significado)
    3 = Lugares VIP
    10 = Lugares para motas
    2 = Lugares Handicap
    25 = Lugares normais
    10 = Lugares para viatura eletricas
    0 = Andar em questão

Classe Menu:

    De longe a classe mais complexa e completa, resumindo aqui temos varios menus e sub menus dentro deles aqui e onde tudo se conecta e é enviado para a classe main correr
    aqui encontramos um loop infinito no primeiro menu onde tem que ser escolhida uma opção, tem uma seguranca caso a pessoa digite algo errado para voltar a perguntar, nesta
    classe encontramos todo o codigo desde criacao de tabelas para os menus e submenus, desde metodos para fazer o pagamento entre outros metodos que sao pedidos para o exercicio
    e outro foram adicionados para o programa ser mais coerente e completo.
    Dentro desses metodos temos a realçar os seguintes:
    def manage_parking_lot - É onde apos criar o cliente podemos escolher o lugar para estacionar
    def register_client - metodo utilizado para registar o cliente
    def pay_for_parking - metodo utilizado para efetura o pagamento do parque de estacionamento, a função paypal ñ funciona pois se fosse para utilizar o programa de verdade
    teriamos de colocar a API para ela funcionar.
    def historical_record - Não funciona pois a intenção era utilizar base de dados para armazenar as contas pagas anteriores , mas ainda ñ sei como utilizar eletricas
    def price_list - cria uma tabela para mostrar o preço por cada tipo de cliente por cada 15 min
    Em resumo e isto a classe tem muitas mais implementações mas estas creio que sao as mais importantes

De realçar tambem que o programa foi feito no IDE Visual Studio Code ñ sei se funcionara corretamente em outros IDE´s.
Meu primeiro grande projeto se assim se possa dizer, espero que o codigo tenha ficado de forma clara, utilizei as classes em separadores diferentes para que fosse mais facil de ler 
e alterar o codigo se necessario.
As bibliotecas utilizadas foram
tabulate
datetime
ramdom
Todo o conhecimento sobre elas foi estudado no site das proprias bibliotecas, no stakeoverflow, no youtube videos a explicar como funcinam elas
O programa pode ter Bug´s, tenter de todas as formas testar o mesmo e correu sem qualquer problema.





                                    Como utilizar o programa

                            1 - Registar um cliente (Manual ou automatico)
                            2 - Pesquisar o cliente pela matricula caso seja feito de forma automatica, e copiar a matricula
                            3 - Escolher a opção A(Park Administration) no menu principal e a opção C no submenu (Manage my parking lot.)
                            4 - Ao escolher essa opção digitar o que e pedidos
                            5 - Aceitar estacionar na opção mostrada pois sera sempre a melhor opção para o seu tipo de cliente
                            6 - No menu principal escolher a opção D(Financial Management), depois a opção A(Pay parking)
                            7 - Colocar a matricula e escrever yes
                            8 - Escolher a forma de pagamento
                            9 - Introduzir um numero de tranferencia aleatorio (Deveria de ser o numero de transferencia real caso estivesse ligado a uma API)
                            10 - Apos o pagamento feito o pode fechar o programa pois terminou para aquila matricula

Pode sempre correr o programa e experimentar de formas diferentes , as vezes pode dar erro pois se ultrupassar mos etapas pode faltar algum dado que e necessario para prosseguir
Bom teste 

Programa feito por Bruno Coelho






English

Start date of the project: July 22, 2023
End date of the project: August 28, 2023

Functionality of the classes

Main Class:

In this class is where all the code comes together and runs, allowing you to omit all the remaining code from the classes, functioning exactly like the main class in Java.

Client Class:

It was intended to be the vehicle class, but as I chose to create more variables that were similar to customer data, I ended up creating it with this name. In this class, we have several methods. In this class, we can register a new client by requesting some of their data. We can use the automatic way to create the number of clients we want randomly, using the random library. We can see the clients that are created here. This class also contains the method for choosing the parking spot, where the datetime library comes in, as it uses local time and date when the vehicle enters the parking lot. There's also a method to check if the client is already registered, another method for when we make a successful payment, and another for when we use a coupon that is active in the system (in this case, they are all active, and there is no implementation to deactivate them).

Parking Class:

Inside the Parking class, we have a Floor class as well because I thought it would be easier to separate the two, each having its specific methods. In the Parking class, we have methods to check if there are available parking spaces, view all the floors, and see which spaces are available (this is updated when a car parks). We have a method to convert 1 hour into 60 minutes to calculate how much each customer has to pay; this payment calculation method is also in this class. Inside the Floor class, we have a method that creates a table using the tabulate library (if it doesn't work, you may need to install it in your PC's command prompt, as it had to be installed in mine this way). This table is integrated into other methods used by other classes. We also have the creation of Floor objects; in this case, we have 6 floors, and each has its available spaces.

Example:
floor_0 = Floor(3,10,2,25,10,0)
Here we have the following spaces (each variable has the following meaning):
3 = VIP spaces
10 = Motorcycle spaces
2 = Handicap spaces
25 = Regular spaces
10 = Electric vehicle spaces
0 = Current floor

Menu Class:

By far, the most complex and comprehensive class; in summary, here we have various menus and sub-menus within them, and this is where everything connects and is sent to the main class to run. In this class, we find an infinite loop in the first menu where an option must be chosen. There's error handling in case the user enters something incorrectly. In this class, we find all the code, from creating tables for menus and sub-menus to methods for making payments, among other methods requested for the exercise, and others added for the program to be more coherent and complete. Within these methods, we should highlight the following:
- `manage_parking_lot`: This is where, after creating the client, we can choose the parking spot.
- `register_client`: Method used to register the client.
- `pay_for_parking`: Method used to make the parking payment. The PayPal function does not work because, in order to use it in a real program, we would have to implement the API.
- `historical_record`: Does not work because the intention was to use a database to store previous paid accounts, but I still don't know how to use it.
- `price_list`: Creates a table to show the price for each type of customer for every 15 minutes.

In summary, this class has many more implementations, but I believe these are the most important ones.

It's also worth noting that the program was created in the Visual Studio Code IDE, so I'm not sure if it will work correctly in other IDEs. This is my first major project, so I hope the code is clear. I used separate classes for better readability and ease of code modification if necessary.

The libraries used were tabulate, datetime, and random. I studied all the knowledge about them on the respective library websites, on Stack Overflow, and through YouTube videos explaining how they work.

The program may have bugs, so I tried to test it in various ways, and it ran without any problems.

                                   How to use the program:

                            1. Register a client (manually or automatically).
                            2. Search for the client by license plate if it's done automatically and copy the license plate.
                            3. Choose option A (Park Administration) in the main menu and option C in the submenu (Manage my parking lot).
                            4. After choosing this option, enter the requested information.
                            5. Accept parking in the shown option, as it will always be the best option for your type of client.
                            6. In the main menu, choose option D (Financial Management), then option A (Pay parking).
                            7. Enter the license plate and type "yes."
                            8. Choose the payment method.
                            9. Enter a random transfer number (it should be the actual transfer number if it were connected to an API).
                            10. After the payment is made, you can close the program as it's completed for that license plate.

Feel free to run the program and experiment with it in different ways. Sometimes it may give an error if you skip steps because some necessary data might be missing to proceed. Good testing!

Program created by Bruno Coelho.