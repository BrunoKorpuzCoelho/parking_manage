# Aqui temos a classe veiculo mas como quis colocar mais variaveis achei melhor chamar a mesma de client pois ela guarda toda a informação daquele cliente
from tabulate import tabulate
import datetime
import random
from parking import Floor , Parking

class Client:

    historical_costs = {}

    def __init__(self, name, id_number, brand, model, fuel, license_plate, historical_cost, client_type):
            self.name = name
            self.id_number = id_number
            self.brand = brand
            self.model = model
            self.fuel = fuel
            self.license_plate = license_plate
            self.historical_cost = historical_cost
            self.client_type = client_type
            self.entry_time = None
            self.current_charge = 0.0

    
        
        

    

    

    def add_cost_to_history(self, cost):
        if self.id_number not in Client.historical_costs:
            Client.historical_costs[self.id_number] = 0
        Client.historical_costs[self.id_number] += cost
        
    # Método estático para realizar o registro de clientes de forma manual ou automatica utilizando random
    @staticmethod
    def registration(clients):
        while True:
            while True:
                create_random = input("Do you want to create a client randomly? (yes/no): ").lower()
                if create_random == "yes":
                    num_random_clients = 0
                    while not num_random_clients:
                        try:
                            num_random_clients = int(input("How many random clients do you want to create? "))
                        except ValueError:
                            print("Please enter a valid number.")
                    
                    for _ in range(num_random_clients):
                        name = random.choice(["Alice", "Bob", "Charlie", "David", "Eve"])
                        id_number = random.randint(100000, 999999)
                        brand = random.choice(["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"])
                        model = random.choice(["Corolla", "Civic", "Focus", "Malibu", "Sentra"])
                        fuel = random.choice(["Gasoline", "Diesel", "Electric"])
                        license_plate = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(7))
                        client_type = random.choice(["VIP", "Handicap", "Normal", "Motorcycle", "Electric"])
                        historical_cost = 0.0
                        
                        client = Client(name, id_number, brand, model, fuel, license_plate, historical_cost, client_type)
                        clients.append(client)
                        
                    print(f"{num_random_clients} random clients created successfully!\n")
                    break  
                    
                elif create_random == "no":
                    name = input("Enter client's name: ")
                    id_number = input("Enter client's ID number (6 digits): ")
                    if not id_number.isdigit() or len(id_number) != 6:
                        print("Invalid ID number. Please enter a 6-digit id.")
                        continue
                    id_number = int(id_number)
                    brand = input("Enter your car brand: ")
                    model = input("Enter your car model: ")
                    fuel = input("Enter your car fuel type: ")
                    license_plate = input("Enter your car license plate: ")
                    historical_cost = 0.0
                    while True:
                        client_type = input("Enter client type (VIP/Handicap/Normal/Electric/Motorcycle)").upper()
                        if client_type not in ["VIP", "HANDICAP", "NORMAL", "MOTORCYCLE", "ELECTRIC"]:
                            print("What you have written is invalid, please try again.")
                        else:
                            break    
                    client = Client(name, id_number, brand, model, fuel, license_plate, historical_cost, client_type)
                    clients.append(client)
                    print("Client registered successfully!\n")
                    break  
                    
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
                    
            choice = input("Do you want to register another client? (yes/no): ").lower()
            if choice != "yes":
                break


    

    


    
    @staticmethod          
    def show_clients(clients):


        def search_name():
            for client in clients:  
                print(f"Name: {client.name}")
        
                
                


        

        def search_idnumber():
            for client in clients:
                print(f"ID Number: {client.id_number}")
            
                


        def search_platenumber():
            for client in clients:
                print(f"License Plate: {client.license_plate}")

        
        
        
        
        def leave():
            print("Option E - Leave")



        #   

        a_choices = {
            "A" : search_name,               # Aqui vemos quantos lugares estão disponiveis
            "B" : search_idnumber,      # Aqui vemos quantos lugares por tipo estão disponiveis
            "C" : search_platenumber,                    # Aqui gerenciamos o nosso estacionamento (Valor e tempo)
            "D" : leave,                                 # Aqui retorna para o menu anterior sem sair do programa
        }

        data = [
          ["A","Search for Name"],
          ["B","Search for Id Number"],
          ["C","Searche for Plate Number"],
          ["D","Leave"]  
        ]

        header = ["Option", "Description"]

        tabela_formatada = tabulate(data , headers=header, tablefmt = "grid")

        while True:
            print(tabela_formatada)
            user_choice = input("Enter your choice: ").upper()
            if user_choice in a_choices:
                a_choices[user_choice]()
                if user_choice == 'D':
                    break
            else:
                print("Invalid option. Please choose a valid option, A, B, C, D.")  
    

    @staticmethod
    def choose_parking_spot(clients, floors_list, client):
        Floor.display_table()
        floor_choice = int(input("Enter the floor number where you want to park: "))

        if 0 <= floor_choice < len(Floor.floors_list):
            selected_floor = Floor.floors_list[floor_choice]
            
            spot_type = None  

            
            if client.client_type == "VIP" and selected_floor.vip_spots > 0:
                if input("Do you want to park in a VIP spot? (Y/N): ").lower() == 'y':
                    selected_floor.vip_spots -= 1
                    spot_type = "VIP"

            elif client.client_type == "Handicap" and selected_floor.handicap_spots > 0:
                if input("Do you want to park in a Handicap spot? (Y/N): ").lower() == 'y':
                    selected_floor.handicap_spots -= 1
                    spot_type = "Handicap"

            elif client.client_type == "Normal" and selected_floor.normal_spots > 0:
                if input("Do you want to park in a Normal spot? (Y/N): ").lower() == 'y':
                    selected_floor.normal_spots -= 1
                    spot_type = "Normal"

            elif client.client_type == "Motorcycle":
                if input("Do you want to park in a Motorcycle spot? (Y/N): ").lower() == 'y':
                    if selected_floor.motor_spots > 0:
                        selected_floor.motor_spots -= 1
                    spot_type = "Motorcycle"
                
            elif client.client_type == "Electric": 
                if input("Do you want to park in an Electric spot? (Y/N): ").lower() == 'y':
                    if selected_floor.electric_spot < 0:
                        selected_floor.electric_spot -= 1
                    spot_type = "Electric"
            
            if spot_type:
                initial_charge = 0.20
                client.current_charge += initial_charge
                current_time = datetime.datetime.now()
                client.entry_time = current_time
                hours = current_time.hour
                minutes = current_time.minute
                entry_date = current_time.strftime("%d/%m/%Y")
                print(f"You can park at the {spot_type} spot on this floor.")
                print(f"Your parking time starts at: {entry_date}, {hours:02}:{minutes:02}.")
                return spot_type
            
            else:
                print("Sorry, no spots available of your type on this floor. Please select another floor.")
        
        else:
            print("Invalid floor choice. Please choose again.")
     

            






    @staticmethod
    def customer_exists(clients, selected_floor):
        license_plate = input("Enter your car license plate: ")

        for client in clients:
            if client.license_plate == license_plate:
                print(f"Welcome back, {client.name}!")
                return

        print("License plate not found. Please register.")
        Client.registration(clients)

    def payment_done(self):
    
        self.historical_cost += 0.20
        print(f"Payment has been completed for {self.name}. Total cost: {self.historical_cost}")

    def payment_coupon():
        print("Coupon use successfully.")
        print("Payment successfully")
    


    
         
        

    
        



  
        
