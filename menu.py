from tabulate import tabulate;
from parking import Parking
import datetime
from parking import Floor
from client import Client
import random


class Menu:

    

    def __init__(self, clients):
        self.clients = clients
        self.parking = Parking()
        self.choices = {
            'A': self.park_administration,
            'B': self.register_client,
            'C': self.client_list,
            'D': lambda: self.financial_management(self.clients, datetime.datetime.now()),
            'E': self.historical_record,
            'F': self.price_list,
            'G': self.leave,
        }

        

    def show_menu(self):
        menu_table = [
            ["(A)", "Park Administration"],
            ["(B)", "Register new client"],
            ["(C)", "Client List"],
            ["(D)", "Financial Management"],
            ["(E)", "Historical Record"],
            ["(F)", "Price list"],
            ["(G)", "Leave"]
        ]        
# Aqui criamos um Loop infinto ate que o utilizador clique em uma das opções para poder prosseguir o programa
        while True:
            print(tabulate(menu_table, headers=["Option", "Description"]))
            user_choice = input("Enter your choice: ").upper()   # Aqui o utilizador introduz a opção que deseja e o .upper garante que mesmo que ponha em letra minuscula o programa recebera em maiuscula
# Aqui criamos um if else para se a opção escrita pelo utilizador ñ estiver na lista 
            if user_choice in self.choices:
                self.choices[user_choice]()
                if user_choice == "G":
                    break
            else:
                print("Invalid option. Please choose a valid option, A, B, C, D, E, F, G.")
    def park_administration(self):

        print("Option A - Park Administration selected.")
        print()
        print("Please choose one of the following options:")
        print()
        def verify_park_availability():
            print("Option A - Verify park availability selected.")
                # Aqui vemos a disponibilidade do parque inteiro ou seja todos os lugares possiveis
            if Parking.its_full:
                print("The parking lot is full.")
            else:
                print("The parking lot has available spots.")
                print("Available spots:", Parking.avai_vehi_spots)
            print()
            print()
        def verify_park_availability_by_type():
            # Aqui vemos a disponibilidade por tipo de todos os andares do parque
            print("Option B - Verify park availability by type selected.")
            print()
            print()
            for floor in Floor.floors_list:
                floor.verify_park_availability_by_type()
            
        def manage_parking_lot(self, clients):
            print("Option C - Manage my parking lot selected.")
            print()
            
            Floor.display_table()
            floor_number = input("Enter the selected floor: ")

            try:
                selected_floor = Floor.floors_list[int(floor_number)]
            except (ValueError, IndexError):
                print("Invalid floor number.")
                return

            license_plate = input("Enter your car license plate: ")
            
            
            client = None
            for c in clients:
                if c.license_plate == license_plate:
                    client = c
                    break
            
            if client:
                client.choose_parking_spot(clients, selected_floor, client)  
            else:
                print("No matching client found.")



        def leave():
            print("Option D - Leave ...")
                

        
          

        a_choices = {
            "A" : verify_park_availability,                         # Aqui vemos quantos lugares estão disponiveis
            "B" : verify_park_availability_by_type,                 # Aqui vemos quantos lugares por tipo estão disponiveis
            "C" : lambda: manage_parking_lot(self, self.clients),  # Aqui gerenciamos o nosso estacionamento
            "D" : leave,                                           # Aqui retorna para o menu anterior sem sair do programa
        }

        data = [
            ["(A)", "Verify park availability"],
            ["(B)", "Verify park availability, all floors and types"],
            ["(C)", "Manage my parking lot."],
            ["(D)", "Leave"]
        ]

        header = ["Option" , "Description"]
        
        tabela_formatada = tabulate(data , headers=header, tablefmt = "grid")

        while True:
            print(tabela_formatada)
            user_choice = input("Enter your choice: ").upper()
            if user_choice in a_choices:
                a_choices[user_choice]()
                if user_choice == 'D':
                    break
            else:
                print("Invalid option. Please choose a valid option, A, B, C, D, E.")
    
    def register_client(self):
        print("Option B - Register new client selected.")
        Client.registration(self.clients)  # Chama o método estático registration() na classe Client
        print()




    def client_list(self):
        print("Option C - Client list selected.")
        Client.show_clients(self.clients)
        print()


          

        








    def financial_management(self, clients, time):
        total_amount_due = 0


        def pay_for_parking():
            print("Option A - Pay parking.")
            print()
            license_plate = input("Enter your car license plate: ")
            client = [c for c in self.clients if c.license_plate == license_plate]

            if client:
                client = client[0]
                current_time = datetime.datetime.now()
                parked_time = current_time - client.entry_time
                parked_minutes = parked_time.total_seconds() / 60

                initial_charge = 0.20
                additional_charge = Parking().calculate_charge(client.client_type, parked_minutes)
                total_amount_due = initial_charge + additional_charge

                print(f"Total amount due for {license_plate}: ${total_amount_due:.2f}")  # Mostra com duas casas decimais
                payment = input("Do you want to proceed with the payment? (yes/no): ")

                if payment.lower() == "yes":
                    
                    payment_options = [
                        ("MBWAY", "Enter your phone number:"),
                        ("Credit Card", "Enter your credit card number (8 digits):"),
                        ("Entity and Reference", None),
                        ("Paypal", None),
                        ("Crypto Payment", None),
                        ("Leave", None)
                    ]

                    print("Choose a payment method:")
                    for index, (method, _) in enumerate(payment_options, 1):
                        print(f"{index}. {method}")

                    choice = int(input())
                    if choice == 1:
                        phone = input(payment_options[0][1])
                        trans_num = input("Enter your transfer number: ")
                        print("Thank you!")

                    elif choice == 2:
                        card_num = input(payment_options[1][1])
                        while len(card_num) != 8:
                            card_num = input("Invalid. Enter your credit card number (8 digits): ")
                        card_name = input("Enter name on the card: ")
                        print("Payment successful!")
                        print("Thank you!")

                    elif choice == 3:
                        entity = str(random.randint(10000000, 99999999))
                        reference = str(random.randint(100000000000000, 999999999999999))
                        print(f"Entity: {entity}\nReference: {reference}\nAmount: {total_amount_due:.2f}")
                        trans_num = input("Enter your transfer number: ")
                        print("Thank you!")

                    elif choice == 4:
                        print("Error: Paypal is temporarily unavailable. Please choose another option.")

                    elif choice == 5:
                        crypto_options = [
                            ("BITCOIN", "37LTttGNjAeYodHLRMvYGSQ8r4TQstwhY5", "BTC", "a"),
                            ("ETHERUM", "0xb3F9D84af15bD48c77228F8Ec2CC4979d3869C87", "ERC 20", "b"),
                            ("USDT", "0x9677baac5920eb689b1d61a7b67e18825879f6ea", "Polygon", "c"),
                        ]
                        print(tabulate(crypto_options, headers=["Currency", "Code", "Network", "Option"], tablefmt="grid"))
                        crypto_choice = input("Choose an option: ")
                        if crypto_choice in ['a', 'b', 'c']:
                            trans_num = input("Enter your transfer number: ")
                            print("Thank you!")

                    elif choice == 6:
                        return

                    Parking.register_payment(total_amount_due)
                    client.payment_done()
                    print(f"Payment of ${total_amount_due:.2f} done successfully!")

                else:
                    print("Payment cancelled.")

            else:
                print(f"No records found for license plate {license_plate}")
            return total_amount_due
            




        def parking_time():
            print("Option B - See parking time.")   
            print()
            license_plate = input("Enter your car license plate: ")
            client = None
            for c in clients:
                if c.license_plate == license_plate:
                    client = c
                    break
            
            if client:
                Parking.time(time)
            else:
                print("No matching client found.")
                
            
            






        def use_free_coupon(total_amount_due):
            print("Option C - Use a free coupon.")
            coupon = ["SUMMERFREE", "CHRISTMASFREE", "HAPPYNEWYEARFREE"]
            user_coupon = input("Please use your coupon here: ").upper()
            if user_coupon in coupon:
                Client.payment_coupon()
                total_amount_due[0] = 0
            else:
                print("The coupon used doesn't exist.")
                    
             





        def leave():
            print("Option D - Leaving")

        a_choices = {
            "A": pay_for_parking,
            "B": parking_time,
            "C": lambda: use_free_coupon(total_amount_due),
            "D": leave,
        }

        data = [
            ["(A)", "Pay parking"],
            ["(B)", "See parking time"],
            ["(C)", "Use a free coupon"],
            ["(D)", "Leave"]    
        ]

        header = ["Option", "Description"]
        tabela_formatada = tabulate(data, headers=header, tablefmt="grid")

        while True:
            print(tabela_formatada)
            user_choice = input("Enter your choice: ").upper()
            if user_choice in a_choices:
                a_choices[user_choice]()
                if user_choice == 'D':
                    break
            else:
                print("Invalid option. Please choose a valid option, A, B, C, D.")





    def historical_record(self):
        print("Option C - Historical Record selected.")
        print("Option unavailable.")




    def price_list(self):
        dados = [
            [1.0, "$",  "15 Min", "Normal"],
            [2.0, "$", "15 Min", "Handicap"],
            [5.0, "$", "15 Min", "VIP"],
            [0.50, "$", "15 Min", "Bike"],
        ]
        header = ["Price", "Currency", "Time", "Category"]
        tabela_formatada = tabulate(dados, headers=header, tablefmt="grid")
        print("Option D - Price list selected.")
        print()
        print(tabela_formatada)
        




    def leave(self):
        print("Option E - Leave selected. Byeeee...")
        print()





        


    

