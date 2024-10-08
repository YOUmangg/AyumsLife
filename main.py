import Human, Food, Animals, Games
import random
import time
from storage import reset_game
from tabulate import tabulate

# Ayum = Human.Ayum()
def print_game_title():
    print("""

     ___   ____    ____  __    __  .___  ___.  __     _______.    __       __   _______  _______ 
    /   \  \   \  /   / |  |  |  | |   \/   | (_ )   /       |   |  |     |  | |   ____||   ____|
   /  ^  \  \   \/   /  |  |  |  | |  \  /  |  |/   |   (----`   |  |     |  | |  |__   |  |__   
  /  /_\  \  \_    _/   |  |  |  | |  |\/|  |        \   \       |  |     |  | |   __|  |   __|  
 /  _____  \   |  |     |  `--'  | |  |  |  |    .----)   |      |  `----.|  | |  |     |  |____ 
/__/     \__\  |__|      \______/  |__|  |__|    |_______/       |_______||__| |__|     |_______|
                                                                                                 

""")
    
def start_new_game():
    return Human.Ayum()

print("Welcome to Ayum's Life!")
print("1. Start New Game")
print("2. Load Saved Game")
print("3. Reset Saved Data")
choice = input("Enter your choice (1/2/3): ")
if choice == '1':
    Ayum = start_new_game()
elif choice == '2':
    Ayum = Human.Ayum()
    if not Ayum.load_state():
        print("No saved game found. Starting a new game.")
        Ayum = start_new_game()
elif choice == '3':
    reset_game()
    print("Saved data has been reset. Starting a new game.")
    Ayum = start_new_game()
else:
    print("Invalid choice. Starting a new game.")
    Ayum = start_new_game()

# Abstraction increase. x == 1, 2 etc should all be methods defined in objects for better readability

# increase health based on time elapsed in saved files as well.

# Consider the case when Ayum is full but health is not full.
# Consider the case when Ayum is not full but health is full.

#Health limit should increase while eating and searching for food too?
#num_ops increase when playing games?
#check where health and attack stats are increasing. health needs to increase more
#time change, because saved game is also in place now

game = "Yes"

print_game_title()

num_ops = 0

start_time = time.time()

while game == "Yes":
    time.sleep(1)
    if num_ops > Ayum.age:
        Ayum.age += 1
        Ayum.age_bonus()
        num_ops = 0
        print("Congrats! Ayum is an year older now.")
    print("These are the current stats of Ayum: ")
    stats = [
    ["Health", Ayum.health, Ayum.progress_bar(Ayum.health, Ayum.health_limit)],
    ["Hunger", Ayum.hunger, Ayum.progress_bar(Ayum.hunger, Ayum.hunger_limit)],
    ["Age", Ayum.age],
    ["Sleep", Ayum.sleep, Ayum.progress_bar(Ayum.sleep, Ayum.sleep_limit)],
    ["Attack", Ayum.attack, Ayum.progress_bar(Ayum.attack, Ayum.attack_limit)]
    ]
    print(tabulate(stats, headers=["Attribute", "Value"], tablefmt="fancy_grid"))

    check = Ayum.check_for_stats()

    if Ayum.age == 10:
        print(
            """Huge congratulations to Ayum on completing an incredible journey and surviving against all odds! As Ayum reaches the milestone of 10 years old, they emerge victorious from the wilderness, a testament to their strength, resilience, and determination."""
        )
        time.sleep(3)
        print("""From the scorching deserts to the icy tundras, Ayum has faced every environment and overcome countless challenges, whether it was foraging for food, dodging dangers, or building shelter. And yet, they have persevered, grown, and thrived.
              This achievement is not just a testament to Ayum's survival skills, but also to their exploration, creativity, and adaptability. They have explored uncharted territories, discovered new resources, and made friends and allies along the way."""
        )
        time.sleep(3)
        print(
            """As Ayum looks out at the world they've conquered, they can take pride in knowing that they've truly earned their place as a survivor, a leader, and a master of their domain. Well done, Ayum! May your journey be a reminder that with hard work, determination, and a spirit of adventure, anything is possible!"""
        )
        time.sleep(2)
        end_time = time.time()
        print("These are your final stats for Ayum. You finished the game in: {} minutes".format(round((end_time - start_time) / 60), 2))
        game = "No"
        ayum_stats = {
            'health': Ayum.health,
            'hunger': Ayum.hunger,
            'age': Ayum.age,
            'sleep': Ayum.sleep,
            'attack': Ayum.attack
        }
        print(ayum_stats)
        break

    time.sleep(1)
    print("┌─────────────────────┐")
    print("│ What do you want to │")
    print("│        do?          │")
    print("├─────────────────────┤")
    print("│ 1. Eat              │")
    print("│ 2. Sleep            │")
    print("│ 3. Search for food  │")
    print("│ 4. Hunt             │")
    print("│ 5. Check inventory  │")
    print("│ 6. Play Games       │")
    print("│ 7. Save Game        │")
    print("│ 8. Exit             │")
    print("└─────────────────────┘")

    if check == True:
        print("Ayum is too weak to do anything. You need to take care of him!")
        time.sleep(1)

    exec = False
    while exec != True:
        try:
            x = int(input())
            exec = True
        except:
            print("Invalid input. Please try again!")
            exec = False

    if x == 1:
        if len(Ayum.food_inventory) > 0:
            print("Ayum has the following food in his inventory:")
            for i, food in enumerate(Ayum.food_inventory):
                if food is not None:
                    print(f"{i+1}. {food.name}")
                else:
                    print(f"{i+1}. Empty slot")
                    pass

            print("Which food do you want to eat? Type the food number: ")
            while True:
                try:
                    food_choice = int(input())
                    if food_choice <= 0 or food_choice > len(Ayum.food_inventory):
                        print("Please enter a valid food choice number.")
                    else:
                        food_choice = Ayum.food_inventory[food_choice - 1]
                        Ayum.eat_food(food_choice)
                        break
                except ValueError:
                    print("Please enter a valid integer for the food choice.")
        else:
            print(
                "Ayum has no food in his inventory. You need to search for food first!"
            )
    elif x == 2:
        Ayum.sleep_fully()
        num_ops += 0.5
    elif x == 3:
        Ayum.search_food()
        num_ops += 0.5
    elif x == 4:
        animal = Animals.Animal
        animal = Animals.Animal.select_animal(Ayum.age)
        encounter_messages = [
            f"A violent {animal.name} has appeared!",
            f"You are being approached by a {animal.name}!",
            f"A hungry {animal.name} is enraged and coming at you, you must fight!",
        ]

        print(random.choice(encounter_messages))
        while animal.health > 0 and Ayum.health > 0:
            power = Ayum.hunt(animal)
            print(
                f"Ayum attacked {animal.name} with {power} damage. The {animal.name} has {animal.health} health left!"
            )
            time.sleep(2)
            if animal.health > 0:
                power = animal.attack(Ayum)
                print(
                    f"The {animal.name} attacked Ayum with {power} damage. Ayum has {Ayum.health} health left!"
                )
                time.sleep(2)
            if Ayum.health <= 0:
                print(f"Game Over. The {animal.name} defeated Ayum")
                game = "No"
                break
        if animal.health <= 0:
            print(
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
        num_ops += 1

    elif x == 5:
        if len(Ayum.food_inventory) > 0:
            print("Ayum has the following food in his inventory: ")
            for i, food in enumerate(Ayum.food_inventory):
                if food is not None:
                    print(f"{i+1}. {food.name}")
                else:
                    print(f"{i+1}. Empty slot")
        else:
            print(
                "Ayum has no food in his inventory. You need to search for food first!"
            )
    elif x == 6:
        Ayum.play_games()

    elif x == 7:
        Ayum.save_state()

    elif x == 8:
        print(
            "Ayum has decided to go home. He is tired and wants to sleep. Goodbye! Your final stats are: "
        )
        ayum_stats = {
            'health': Ayum.health,
            'hunger': Ayum.hunger,
            'age': Ayum.age,
            'sleep': Ayum.sleep,
            'attack': Ayum.attack
        }
        print(ayum_stats)
        print("Thanks for taking care of Ayum!")
        game = "No"

stats = [
    ["Health", Ayum.health, Ayum.progress_bar(Ayum.health, Ayum.health_limit)],
    ["Hunger", Ayum.hunger, Ayum.progress_bar(Ayum.hunger, Ayum.hunger_limit)],
    ["Age", Ayum.age],
    ["Sleep", Ayum.sleep, Ayum.progress_bar(Ayum.sleep, Ayum.sleep_limit)],
    ["Attack", Ayum.attack, Ayum.progress_bar(Ayum.attack, Ayum.attack_limit)]
    ]
print(tabulate(stats, headers=["Attribute", "Value"], tablefmt="fancy_grid"))


