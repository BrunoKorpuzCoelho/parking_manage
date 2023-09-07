# Aqui será a classe que faz o gerenciamento do parque

import datetime
from tabulate import tabulate

class Parking:
     
# Variaveis

    its_full = False
    vip = 0
    handicap = 0
    parking_time = 45
    cost = 1.0
    avai_vehi_spots = 250
    matriculas = []
    total_earnings = 0


    def __init__(self):
         self.its_full = Parking.its_full
         self.vip = Parking.vip
         self.handicap = Parking.handicap
         self.parking_time = Parking.parking_time
         self.cost = Parking.cost
         self.avai_vehi_spots = Parking.avai_vehi_spots
         self.matriculas = Parking.matriculas.copy()


    @staticmethod
    def time_to_minutes(hours, minutes):
        time = hours * 60 + minutes
        return time
    
    def calculate_charge(self, parking_type, time_in_minutes):
        parking_rates = {"vip": self.vip, "handicap": self.handicap}
        rate = parking_rates.get(parking_type, 0)
        return (time_in_minutes / 15) * rate
    
    def time(time):
        formatted_time = time.strftime("%Y-%m-%d %H:%M")
        print(formatted_time)

    

    



    def check_parking_full(self):

        if self.avai_vehi_spots < 0:
            self.avai_vehi_spots = 0
        if self.avai_vehi_spots == 0:
            print("Parking is full.")
            self.its_full = True
        else:
            print("Paking isn't full.")
            self.its_full = False

    @classmethod
    def register_payment(cls, amount):
        cls.total_earnings += amount

    
   

        
        
        












#Alguma duvida sobre as variaveis tem no glossario a explicação
class Floor:

# Variaveis
    
    vip_spots = 3
    motor_spots = 10
    handicap_spots = 2
    normal_spots = 25
    electric_spot = 10
    floor_levels = {
        0 : "ground",
        1 : "1st",
        2 : "2nd",
        3 : "3rd",
        4 : "4th",
        5 : "5th"
    }
    floors_list = []
    

# Metodos

    def __init__(self, vip, motor_spots, handicap, normal_spots, electric_spot, floor):
        
        self.vip_spots = vip
        self.handicap_spots = handicap
        self.motor_spots = motor_spots
        self.normal_spots = normal_spots
        self.electric_spot = electric_spot
        self.floor = floor
        Floor.floors_list.append(self)

# Aqui criamos um metodo para mostrar a disponibilidade por andar e por tipo de lugar dentro de cada andar
    def verify_park_availability_by_type(self): 
        floor_level = self.floor_levels.get(self.floor, f"{self.floor}")
        print()
        print()
        print(f"On the {floor_level.capitalize()} floor, we have the following spots.")
        print(f"VIP Spots: {self.vip_spots}")
        print(f"Motorcycle Spots: {self.motor_spots}")
        print(f"Handicap Spots: {self.handicap_spots}")
        print(f"Spots: {self.normal_spots}")
        print(f"Eletric car Spots: {self.electric_spot}")

# Aqui criamos um metodo estatico para criação de uma tabela baseada nos lugares disponiveis no nosso parque de estacionamento de forma a ser mais facil a vereficação dos mesmos
    @staticmethod
    def display_table():
        headers = ["VIP", "MOTORCYCLE", "HANDICAP", "NORMAL", "ELECTRICAL", "FLOOR"]
        data = []
        for floor in Floor.floors_list:
            floor_data = [floor.vip_spots, floor.motor_spots, floor.handicap_spots, floor.normal_spots, floor.electric_spot, floor.floor]
            data.append(floor_data)
        
        table = tabulate(data, headers=headers, tablefmt="grid")
        print(table)

#Aqui criamos os andares existentes na nossa infraestrutura
floor_0 = Floor(3,10,2,25,10,0)
floor_1 = Floor(3,10,2,25,10,1)        # Atenção aqui podemos modificar os lugares para ver a funcionar o programa vá na classe readme estara la a informação do o que é cada coluna
floor_2 = Floor(3,10,2,25,10,2)
floor_3 = Floor(3,10,2,25,10,3)
floor_4 = Floor(3,10,2,25,10,4)
floor_5 = Floor(3,10,2,25,10,5)     # Se quiserem criar um andar a mais basta copiar e colar alterar o valor do floor_5 para floor_6 e adicionar ao dicionario uma nova key 
                                            # com o valor 6 e uma nova value com o valor "6th", adicionar tambem na lista abaixo criar o nome da nova variavel







        


        





        


    
