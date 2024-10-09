import random
import time
from colorama import Fore, Back, Style

class Animal:

    max_health = 0

    def __init__(self, name, attack_power, health, energy):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        self.energy = energy
        self.max_health = self.health

        # Will have to set health limits and curr_health type of thing.

    def attack(self, other):
        power = random.randint(self.attack_power, int(self.attack_power * (2.5)))
        other.health -= power
        if other.health < 0:
            other.health = 0
        return power

    @staticmethod
    def select_animal(age):
        an_list = []
        weights = []
        if age <= 3:
            an_list = animal_list
            weights = [1] * len(animal_list)
        elif age < 6:
            an_list = animal_list + difficult_animal_list
            weights = [1] * len(animal_list) + [8] * len(difficult_animal_list)
        elif age <= 9:
            an_list = (
                animal_list + difficult_animal_list + extremely_difficult_animal_list
            )
            weights = (
                [1] * len(animal_list)
                + [1] * len(difficult_animal_list)
                + [16] * len(extremely_difficult_animal_list)
            )
        else:
            an_list = impossible_list
            weights = [100]
            print(Fore.RED + """
                     /^\/^\  
                   _|__|  O| 
          \/     /~     \_/ \  
           \____|__________/  \
                  \_______      \
                          `\     \                 \
                            |     |                  \
                           /      /                    \
                          /     /                       \\
                        /      /                         \ \
                       /     /                            \  \
                     /      /                              \   \
                    /     /                                 \    \
                  /      /                                   \    \
                 /     /                                      \   \
                /     /                                         \  \
               /____ /                                           \__\
""" + Style.RESET_ALL)
        return random.choices(an_list, weights=weights, k=1)[0]

    @staticmethod
    def fight_titanoboa(Ayum):
        print(Fore.RED + """
                     /^\/^\  
                   _|__|  O| 
          \/     /~     \_/ \  
           \____|__________/  \
                  \_______      \
                          `\     \                 \
                            |     |                  \
                           /      /                    \
                          /     /                       \\
                        /      /                         \ \
                       /     /                            \  \
                     /      /                              \   \
                    /     /                                 \    \
                  /      /                                   \    \
                 /     /                                      \   \
                /     /                                         \  \
               /____ /                                           \__\
""" + Style.RESET_ALL)
        animal = Titanoboa_Carni
        encounter_messages = [
            f"A violent {animal.name} has appeared!",
            f"You are being approached by a {animal.name}!",
            f"A hungry {animal.name} is enraged and coming at you, you must fight!",
        ]

        print(Fore.YELLOW + random.choice(encounter_messages) + Style.RESET_ALL)
        while animal.health > 0 and Ayum.health > 0:
            power = Ayum.hunt(animal)
            print(Fore.GREEN +
                f"Ayum attacked {animal.name} with {power} damage. The {animal.name} has {animal.health} health left!"
                + Style.RESET_ALL)
            time.sleep(2)
            if animal.health > 0:
                power = animal.attack(Ayum)
                print(Fore.RED +
                    f"The {animal.name} attacked Ayum with {power} damage. Ayum has {Ayum.health} health left!"
                    + Style.RESET_ALL)
                time.sleep(2)
            if Ayum.health <= 0:
                print(Fore.RED + f"Game Over. The {animal.name} defeated Ayum" + Style.RESET_ALL)
                return False
        if animal.health <= 0:
            print(Fore.GREEN +
                f"Ayum defeated {animal.name}. The animal has been added to his inventory!"
                + Style.RESET_ALL)
            Ayum.sleep_limit += 3
            Ayum.attack_limit += random.randint(
                int(animal.attack_power / 3), int(animal.attack_power)
            )
            Ayum.attack += random.randint(
                int(animal.attack_power / 3), int(animal.attack_power)
            )
            if Ayum.attack > Ayum.attack_limit:
                Ayum.attack = Ayum.attack_limit
            Ayum.health_limit += random.randint(
                int(animal.max_health / 10), int(animal.max_health / 2)
            )
            Ayum.food_inventory.append(animal)
            return True


# Animal.select_animal = select_animal

# initial level
wolf = Animal("Wolf", 10, 100, 10)
lion = Animal("Lion", 20, 150, 20)
wild_boar = Animal("Wild Boar", 15, 120, 10)
wild_dog = Animal("Wild Dog", 7, 80, 8)
bear = Animal("Bear", 25, 200, 15)
tiger = Animal("Tiger", 22, 180, 18)
hyena = Animal("Hyena", 12, 90, 12)

# difficult level
dinosaur = Animal("Dinosaur", 30, 400, 20)
Dragon = Animal("Dragon", 50, 900, 20)
gorilla = Animal("Gorilla", 40, 350, 20)
griffin = Animal("Griffin", 45, 500, 25)
chimera = Animal("Chimera", 55, 600, 30)
manticore = Animal("Manticore", 60, 700, 35)

# extremely difficult level
kraken = Animal("Kraken", 120, 4000, 40)
hydra = Animal("Hydra", 110, 3500, 45)
phoenix = Animal("Phoenix", 70, 6000, 50)
Titanoboa_Carni = Animal("Titanoboa_Carni", 400, 25000, 100)

animal_list = [wolf, lion, wild_boar, wild_dog, bear, tiger, hyena]
difficult_animal_list = [dinosaur, Dragon, gorilla, griffin, chimera, manticore]
extremely_difficult_animal_list = [kraken, hydra, phoenix]
impossible_list = [Titanoboa_Carni]
