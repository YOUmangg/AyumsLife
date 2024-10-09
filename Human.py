import Food
import random
import time
import msvcrt
import Games
from storage import save_game, load_game
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

class Ayum:

    #decide the max and min for each variable. Game should end when age reaches max age.

    health = 200 #max can be increased to 1000
    health_limit = 200
    hunger = 1  
    hunger_limit = 10  #max 30
    age = 1    #max age can be 10. Game will be over with a congrats message
    sleep = 10 #full of sleep = 10. The need will depend on the works ayum has done. if sleep == 0, game will switch off
    sleep_limit = 10
    attack = 10 #attack of ayum (random 10 to 10*3) max attack should go to 500
    attack_limit = 10
    food_inventory = []
    num_ops = 0

    def __init__(self) -> None:
        #All these variables will be taken from a saved file. SQLite will be used.
        self.health = 200
        self.hunger = 1
        self.age = 1
        self.sleep = 10
        self.attack = 10
        self.food_inventory = []
        self.num_ops = 0

    def increase_health(self, amount):
        if amount + self.health <= self.health_limit:
            self.health += amount
        else:
            self.health = self.health_limit

    def increase_hunger(self, amount):
        if(amount + self.hunger <=  self.hunger_limit):
            self.hunger += amount
        else:
            self.hunger = self.hunger_limit

    def increase_attack(self, amount):
        if(amount + self.attack <=  self.attack_limit):
            self.attack += amount
        else:
            self.attack = self.attack_limit

    def eat_food(self, f):
        if(self.hunger <= 0):
            self.hunger = 0
            print(Fore.YELLOW + "Ayum is full")
        else:
            self.hunger -= round(random.randint(int(f.energy / 1.5), int(f.energy)), 2)
            if(self.hunger < 0):
                self.hunger = 0
            self.food_inventory.remove(f)
            self.health_limit += (random.randint(min(20, f.energy*2), max(30, f.energy*3)))
            self.increase_health(random.randint(min(20, f.energy*2), max(30, f.energy*3)))
            self.attack_limit += random.randint(int(f.energy / 2), int(f.energy*2))
            self.increase_attack(random.randint(int(f.energy / 4), int(f.energy / 2)))
            print(Fore.GREEN + f"Ayum ate {f.name} and now has {self.hunger} hunger")

    def sleep_fully(self):
        print(Fore.CYAN + "Ayum is sleeping.... Press any key to wake up or let Ayum sleep fully")
        while self.sleep < self.sleep_limit:
            print(Fore.BLUE + Back.BLACK + "Ayum is sleeping....💤")
            self.sleep += 1
            self.health_limit += random.randint(5, 10)
            self.increase_health(random.randint(5*self.age, 10*self.age))
            self.increase_hunger(random.randint(0, 2))
            self.increase_attack(random.randint(1, 2))
            
            # Check for keypress for 1 second
            start_time = time.time()
            while time.time() - start_time < 1:
                if msvcrt.kbhit():
                    msvcrt.getch()  # Clear the key press
                    print(Fore.GREEN + "Ayum woke up!")
                    self.sleep = int(self.sleep)
                    return  # Exit the method if a key is pressed
            
        self.sleep = int(self.sleep)
        print(Fore.GREEN + f"Ayum slept and now has {int(self.sleep)} sleep")

    def search_food(self):
        print(Fore.CYAN + "Ayum is searching for food....")
        time.sleep(1)
        random_food = random.choice(Food.food_list)
        print(Fore.GREEN + f"Ayum found {random_food.name}!")
        self.health_limit += random.randint(1, 5)
        self.hunger += random.randint(1, random_food.energy) % 2
        self.food_inventory.append(random_food)
        self.sleep -= 0.25

    def hunt(self, animal):
        # additive_multiplier = self.age*2 - int(self.hunger*2)
        attack_power = random.randint(int(self.attack*(1.6)) + self.age*6 - min(int(self.hunger / 4), 10), int(self.attack*3.5) + self.age*6 - min(25, int((self.sleep_limit - self.sleep)*1.5)) - min(int(self.hunger / 4), 10))
        print(Fore.CYAN + f"{int(self.attack*1.5)} self.attack*1.5 {int(self.hunger / 3)} {self.attack*3}")
        if(self.sleep > 0):
            self.sleep -= min(0.02*attack_power, 2*(Ayum.age / 2))
        else:
            self.sleep = 0
        self.sleep = round(self.sleep, 2)
        self.increase_hunger(min(2, round(attack_power / 25, 2)))
        animal.health -= attack_power
        if(animal.health < 0):
            animal.health = 0
        return attack_power
        # if animal.health <= 0:
        #     print(f"{animal.name} has been defeated!")

    def check_for_stats(self):
        problem = False
        if(self.health < 0.1*self.health_limit):
            print(Fore.RED + "Ayum is very weak. He needs to eat something")
            problem = True
        if(self.hunger > 0.9*self.hunger_limit):
            print(Fore.RED + "Ayum is very hungry. He needs to eat something")
            problem = True
        if(self.sleep < 0.1*self.sleep_limit):
            print(Fore.RED + "Ayum is very tired. He needs to sleep")
            problem = True
        return problem
    
    def play_games(self):
        print(Fore.CYAN + "It seems Ayum wants to chill. Which game does he want to play?")
        games = ["Number Guessing", "7 up 7 down"]
        for i in range(0, len(games)):
            print(Fore.YELLOW + f"{i + 1} {games[i]}")
        
        print(Fore.YELLOW + f"{len(games) + 1} Exit Games")
        
        print(Fore.CYAN + "Which game would you like to play? Enter the game number: ")
        
        x = 0

        exec = False
        while(exec != True):
            try:
                x = int(input())
                exec = True
                if(x > len(games) + 1 or x < 1):
                    exec = False
            except:
                print(Fore.RED + "Invalid input. Please try again!")
                exec = False
        
        if(x == len(games) + 1):
            print(Fore.YELLOW + "Alright! We will play some other time :)")
            return
        
        print(Fore.GREEN + f"Let's play the {games[x - 1]} game!")

        if(x == 1):
            Games.Game.Number_guessing(self)
            return True
        if(x == 2):
            Games.Game.SevenUp(self)
            return True
        if(x == 3):
            return False

    def age_bonus(self):
        #Can add more to age bonus
        self.hunger_limit += random.randint(1, 3)
        self.health_limit += random.randint(self.age*25, self.age*50)
        self.increase_health(random.randint(100, 200))
        self.attack_limit += random.randint(5*self.age, 10*self.age)
        self.increase_attack(random.randint(10, 20))
    
    def save_state(self):
        save_game(self)
        print(Fore.GREEN + "Game saved successfully!")

    def load_state(self):
        game_state = load_game()
        if game_state:
            self.health = game_state['health']
            self.health_limit = game_state['health_limit']
            self.hunger = game_state['hunger']
            self.hunger_limit = game_state['hunger_limit']
            self.age = game_state['age']
            self.sleep = game_state['sleep']
            self.sleep_limit = game_state['sleep_limit']
            self.attack = game_state['attack']
            self.attack_limit = game_state['attack_limit']
            self.food_inventory = [Food.food.get_food_by_name(name) for name in game_state['food_inventory'] if name is not None]
            self.num_ops = game_state['num_ops']
            print(Fore.GREEN + "Game loaded successfully!")
            return True
        return False
    
    def __str__(self) -> str:
        return Fore.CYAN + "I am Ayum. Nice to meet you!"
    

    @staticmethod
    def progress_bar(value, max_value, width=20):
        filled = int(width * value / max_value)
        bar = '█' * filled + '░' * (width - filled)
        return f"[{bar}] {value}/{max_value}"
    # print(f"Health: {progress_bar(Ayum.health, Ayum.health_limit)}")
