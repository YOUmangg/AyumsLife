import Human, Food, Animals, Games
import random
import time
from storage import reset_game
from tabulate import tabulate
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

# Ayum = Human.Ayum()
def print_game_title():
    print(Fore.GREEN + """


     ___   ____    ____  __    __  .___  ___.  __     _______.    __       __   _______  _______ 
    /   \  \   \  /   / |  |  |  | |   \/   | (_ )   /       |   |  |     |  | |   ____||   ____|
   /  ^  \  \   \/   /  |  |  |  | |  \  /  |  |/   |   (----`   |  |     |  | |  |__   |  |__   
  /  /_\  \  \_    _/   |  |  |  | |  |\/|  |        \   \       |  |     |  | |   __|  |   __|  
 /  _____  \   |  |     |  `--'  | |  |  |  |    .----)   |      |  `----.|  | |  |     |  |____ 
/__/     \__\  |__|      \______/  |__|  |__|    |_______/       |_______||__| |__|     |_______|
                                                                                                 


""")

    
def start_new_game():
    return Human.Ayum()

print(Fore.GREEN + "Welcome to Ayum's Life!")
print(Fore.YELLOW + "1. Start New Game")
print(Fore.YELLOW + "2. Load Saved Game")
print(Fore.YELLOW + "3. Reset Saved Data")
choice = input(Fore.CYAN + "Enter your choice (1/2/3): ")
if choice == '1':
    Ayum = start_new_game()
elif choice == '2':
    Ayum = Human.Ayum()
    if not Ayum.load_state():
        print(Fore.RED + "No saved game found. Starting a new game.")
        Ayum = start_new_game()
elif choice == '3':
    reset_game()
    print(Fore.YELLOW + "Saved data has been reset. Starting a new game.")
    Ayum = start_new_game()
else:
    print(Fore.RED + "Invalid choice. Starting a new game.")
    Ayum = start_new_game()

# Abstraction increase. x == 1, 2 etc should all be methods defined in objects for better readability

# increase health based on time elapsed in saved files as well.

#time change, because saved game is also in place now
#Sleep is going to negative. Need to enforce sleep at that point

game = "Yes"

print_game_title()

# num_ops = 0

start_time = time.time()

while game == "Yes":
    time.sleep(1)
    if Ayum.num_ops > Ayum.age:
        Ayum.age += 1
        Ayum.age_bonus()
        Ayum.num_ops = 0
        print(Fore.GREEN + "Congrats! Ayum is an year older now.")
        time.sleep(1)
    time.sleep(0.3)
    print(Fore.CYAN + "These are the current stats of Ayum: ")
    stats = [
    ["Health", Ayum.health, Ayum.progress_bar(Ayum.health, Ayum.health_limit)],
    ["Hunger", Ayum.hunger, Ayum.progress_bar(Ayum.hunger, Ayum.hunger_limit)],
    ["Age", Ayum.age],
    ["Sleep", Ayum.sleep, Ayum.progress_bar(Ayum.sleep, Ayum.sleep_limit)],
    ["Attack", Ayum.attack, Ayum.progress_bar(Ayum.attack, Ayum.attack_limit)]
    ]
    print(Fore.WHITE + Back.BLUE + Style.BRIGHT + tabulate(stats, headers=["Attribute", "Value"], tablefmt="fancy_grid"))
    time.sleep(1)

    check = Ayum.check_for_stats()

    if Ayum.age == 10:
        battle  = Animals.Animal.fight_titanoboa(Ayum)
        if(battle != True):
            print(Fore.RED + "Game Over. Ayum couldn't defeat the Titanoboa Carni.")
            game = "No"
            break
        print(Fore.GREEN +
            """Huge congratulations to Ayum on completing an incredible journey and surviving against all odds! As Ayum reaches the milestone of 10 years old, they emerge victorious from the wilderness, a testament to their strength, resilience, and determination."""
        )
        time.sleep(5)
        print(Fore.YELLOW + """From the scorching deserts to the icy tundras, Ayum has faced every environment and overcome countless challenges, whether it was foraging for food, dodging dangers, or building shelter. And yet, they have persevered, grown, and thrived.
              This achievement is not just a testament to Ayum's survival skills, but also to their exploration, creativity, and adaptability. They have explored uncharted territories, discovered new resources, and made friends and allies along the way."""
        )
        time.sleep(5)
        print(Fore.CYAN +
            """As Ayum looks out at the world they've conquered, they can take pride in knowing that they've truly earned their place as a survivor, a leader, and a master of their domain. Well done, Ayum! May your journey be a reminder that with hard work, determination, and a spirit of adventure, anything is possible!"""
        )
        time.sleep(3)
        end_time = time.time()
        print(Fore.GREEN + "These are your final stats for Ayum. You finished the game in: {} minutes".format(round((end_time - start_time) / 60), 2))
        game = "No"
        ayum_stats = {
            'health': Ayum.health,
            'hunger': Ayum.hunger,
            'age': Ayum.age,
            'sleep': Ayum.sleep,
            'attack': Ayum.attack
        }
        print(Fore.CYAN + str(ayum_stats))
        break

    time.sleep(1)
    print(Fore.YELLOW + "┌─────────────────────┐")
    print(Fore.YELLOW + "│ What do you want to │")
    print(Fore.YELLOW + "│        do?          │")
    print(Fore.YELLOW + "├─────────────────────┤")
    print(Fore.YELLOW + "│ 1. Eat              │")
    print(Fore.YELLOW + "│ 2. Sleep            │")
    print(Fore.YELLOW + "│ 3. Search for food  │")
    print(Fore.YELLOW + "│ 4. Hunt             │")
    print(Fore.YELLOW + "│ 5. Check inventory  │")
    print(Fore.YELLOW + "│ 6. Play Games       │")
    print(Fore.YELLOW + "│ 7. Save Game        │")
    print(Fore.YELLOW + "│ 8. Exit             │")
    print(Fore.YELLOW + "└─────────────────────┘")
    # print(Fore.CYAN + f"Ayum.num_ops: {Ayum.num_ops}")
    if check == True:
        print(Fore.RED + "Ayum is too weak to do anything. You need to take care of him!")
        time.sleep(1)

    exec = False
    while exec != True:
        try:
            x = int(input(Fore.CYAN + "Enter your choice: "))
            exec = True
        except:
            print(Fore.RED + "Invalid input. Please try again!")
            exec = False

    if x == 1:
        if len(Ayum.food_inventory) > 0:
            print(Fore.YELLOW + "Ayum has the following food in his inventory:")
            for i, food in enumerate(Ayum.food_inventory):
                if food is not None:
                    print(Fore.CYAN + f"{i+1}. {food.name}")
                else:
                    print(Fore.CYAN + f"{i+1}. Empty slot")
                    pass

            print(Fore.YELLOW + "Which food do you want to eat? Type the food number: ")
            while True:
                try:
                    food_choice = int(input(Fore.CYAN + "Enter food number: "))
                    if food_choice <= 0 or food_choice > len(Ayum.food_inventory):
                        print(Fore.RED + "Please enter a valid food choice number.")
                    else:
                        food_choice = Ayum.food_inventory[food_choice - 1]
                        Ayum.eat_food(food_choice)
                        Ayum.num_ops += 0.25
                        break
                except ValueError:
                    print(Fore.RED + "Please enter a valid integer for the food choice.")
        else:
            print(Fore.RED +
                "Ayum has no food in his inventory. You need to search for food first!"
            )
    elif x == 2:
        Ayum.sleep_fully()
        Ayum.num_ops += 0.5
    elif x == 3:
        Ayum.search_food()
        Ayum.num_ops += 0.5
    elif x == 4:
        animal = Animals.Animal
        animal = Animals.Animal.select_animal(Ayum.age)
        encounter_messages = [
            f"A violent {animal.name} has appeared!",
            f"You are being approached by a {animal.name}!",
            f"A hungry {animal.name} is enraged and coming at you, you must fight!",
        ]

        print(Fore.RED + random.choice(encounter_messages))
        while animal.health > 0 and Ayum.health > 0:
            power = Ayum.hunt(animal)
            print(Fore.YELLOW +
                f"Ayum attacked {animal.name} with {power} damage. The {animal.name} has {animal.health} health left!"
            )
            time.sleep(2)
            if animal.health > 0:
                power = animal.attack(Ayum)
                print(Fore.RED +
                    f"The {animal.name} attacked Ayum with {power} damage. Ayum has {Ayum.health} health left!"
                )
                time.sleep(2)
            if Ayum.health <= 0:
                print(Fore.RED + f"Game Over. The {animal.name} defeated Ayum")
                game = "No"
                break
        if animal.health <= 0:
            print(Fore.GREEN +
                f"Ayum defeated {animal.name}. The animal has been added to his inventory!"
            )
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
        Ayum.num_ops += 1

    elif x == 5:
        if len(Ayum.food_inventory) > 0:
            print(Fore.YELLOW + "Ayum has the following food in his inventory: ")
            for i, food in enumerate(Ayum.food_inventory):
                if food is not None:
                    print(Fore.CYAN + f"{i+1}. {food.name}")
                else:
                    print(Fore.CYAN + f"{i+1}. Empty slot")
        else:
            print(Fore.RED +
                "Ayum has no food in his inventory. You need to search for food first!"
            )
        time.sleep(2)
    elif x == 6:
        play = Ayum.play_games()
        if(play == True):
            Ayum.num_ops += 0.25

    elif x == 7:
        Ayum.save_state()

    elif x == 8:
        print(Fore.YELLOW +
            "Ayum has decided to go home. He is tired of the expedition and wants to rest. Goodbye! Your final stats are: "
        )
        game = "No"
    
    else:
        print("Please enter a valid input.")

print(Fore.CYAN + "Ayum's stats are: ")
stats = [
    ["Health", Ayum.health, Ayum.progress_bar(Ayum.health, Ayum.health_limit)],
    ["Hunger", Ayum.hunger, Ayum.progress_bar(Ayum.hunger, Ayum.hunger_limit)],
    ["Age", Ayum.age],
    ["Sleep", Ayum.sleep, Ayum.progress_bar(Ayum.sleep, Ayum.sleep_limit)],
    ["Attack", Ayum.attack, Ayum.progress_bar(Ayum.attack, Ayum.attack_limit)]
    ]
print(Fore.WHITE + Back.BLUE + tabulate(stats, headers=["Attribute", "Value"], tablefmt="fancy_grid"))

print(Fore.GREEN + "Thanks for taking care of Ayum!")
