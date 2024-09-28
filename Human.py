import Food
import random
import time
import msvcrt

class Ayum:

    #decide the max and min for each variable. Game should end when age reaches max age.

    health = 200 #max can be increased to 1000
    health_limit = 200
    hunger = 1   #max 10
    hunger_limit = 10
    age = 1    #max age can be 100. Game will be over with a congrats message
    sleep = 10 #full of sleep = 10. The need will depend on the works ayum has done. if sleep == 0, game will switch off
    sleep_limit = 10
    attack = 10 #attack of ayum (random 10 to 10*5) max attack can go to 100
    attack_limit = 10
    food_inventory = []

    #starting with basic functions. food eating first

    def __init__(self) -> None:
        #All these variables will be taken from a saved file. Pandas dataframe will be used.
        self.health = 200
        self.hunger = 1
        self.age = 1
        self.sleep = 10
        self.attack = 10
        self.food_inventory = []
        # pass

    def eat_food(self, f):
        if(self.hunger < 0):
            self.hunger = 0
            print("Ayum is full")
        else:
            self.hunger -= f.energy 
            if(self.hunger < 0):
                self.hunger = 0
            self.food_inventory.remove(f)
            self.health += random.randint(10, f.energy*2)
            print(f"Ayum ate {f.name} and now has {self.hunger} hunger")

    def sleep_fully(self):
        print("Ayum is sleeping.... Press any key to wake up or let Ayum sleep fully")
        while self.sleep < 10:
            print("Ayum is sleeping....")
            self.sleep += 1
            if(self.health < self.health_limit):
                self.health += random.randint(1, 20)
                if(self.health > self.health_limit):
                    self.health = self.health_limit
            
            # Check for keypress for 1 second
            start_time = time.time()
            while time.time() - start_time < 1:
                if msvcrt.kbhit():
                    msvcrt.getch()  # Clear the key press
                    print("Ayum woke up!")
                    self.sleep = int(self.sleep)
                    return  # Exit the method if a key is pressed
            
        print(f"Ayum slept and now has {int(self.sleep)} sleep")

    def search_food(self):
        print("Ayum is searching for food....")
        time.sleep(1)
        random_food = random.choice(Food.food_list)
        print(f"Ayum found {random_food.name}!")
        self.hunger += random.randint(1, random_food.energy) % 2
        self.food_inventory.append(random_food)
        self.sleep -= 0.25

    def hunt(self, animal):
        attack_power = random.randint(self.attack*2, self.attack*5 - int(self.sleep_limit - self.sleep)*2)
        if(self.sleep > 0):
            self.sleep -= 0.02*attack_power
        else:
            self.sleep = 0
        self.sleep = round(self.sleep, 2)
        animal.health -= attack_power
        return attack_power
        # if animal.health <= 0:
        #     print(f"{animal.name} has been defeated!")

    def check_for_stats(self):
        problem = False
        if(self.health < 0.1*self.health_limit):
            print("Ayum is very weak. He needs to eat something")
            problem = True
        if(self.hunger > 0.9*self.hunger_limit):
            print("Ayum is very hungry. He needs to eat something")
            problem = True
        if(self.sleep < 0.1*self.sleep_limit):
            print("Ayum is very tired. He needs to sleep")
            problem = True
        return problem

    def __str__(self) -> str:
        return "Hello"
    
