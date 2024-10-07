import Human, Food, Animals, Games
import random
import time

Ayum = Human.Ayum()

# Have to add weighted random choice according to the age of Ayum

# How to increase age?
# number of operations. For num_ops > age. [growing up should be dependent on age too, also decide on
# other limits based on age too!]

# Abstraction increase. x == 1, 2 etc should all be methods defined in objects for better readability

# increase health based on time elapsed in saved files as well.

# Consider the case when Ayum is full but health is not full.
# Consider the case when Ayum is not full but health is full.

game = "Yes"

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
    ayum_stats = Ayum.__dict__.copy()
    ayum_stats.pop("food_inventory", None)

    print(ayum_stats)

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
        ayum_stats = Ayum.__dict__.copy()
        ayum_stats.pop("food_inventory", None)
        print(ayum_stats)
        break

    time.sleep(1)
    print("What do you want to do? Type the option number: ")
    print("1. Eat")
    print("2. Sleep")
    print("3. Search for food")
    print("4. Hunt")
    print("5. Check inventory")
    print("6. Play Games")
    print("7. Exit")

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
            print("Ayum has the following food in his inventory: ")
            for i in range(len(Ayum.food_inventory)):
                print(f"{i+1}. {Ayum.food_inventory[i].name}")
            print("Which food do you want to eat? Type the food number: ")
            food_choice = int(input())
            if food_choice <= 0 or food_choice > len(
                Ayum.food_inventory
            ):  # handling the invalid input case.
                print("Please enter a valid food choice number.")
            else:
                food_choice = Ayum.food_inventory[food_choice - 1]
                Ayum.eat_food(food_choice)
        else:
            print(
                "Ayum has no food in his inventory. You need to search for food first!"
            )
    elif x == 2:
        Ayum.sleep_fully()
        num_ops += 1
    elif x == 3:
        Ayum.search_food()
        num_ops += 1
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
            for i in range(len(Ayum.food_inventory)):
                print(f"{i+1}. {Ayum.food_inventory[i].name}")
        else:
            print(
                "Ayum has no food in his inventory. You need to search for food first!"
            )
    elif x == 6:
        Ayum.play_games()

    elif x == 7:
        print(
            "Ayum has decided to go home. He is tired and wants to sleep. Goodbye! Your final stats are: "
        )
        # print(Ayum.__dict__)
        ayum_stats = Ayum.__dict__.copy()
        ayum_stats.pop("food_inventory", None)

        print(ayum_stats)
        print("Thanks for taking care of Ayum!")
        game = "No"
