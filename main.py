import Human, Food, Animals
import random
import time

Ayum = Human.Ayum()

# Have to add weighted random choice according to the age of Ayum

carrot = Food.food("Carrot", 10)
apple = Food.food("Apple", 20)
pasta = Food.food("Pasta", 7)
orange = Food.food("Orange", 15)

#How to increase age? 
#number of operations. For num_ops > age. [growing up should be dependent on age too, also decide on
# other limits based on age too!]

# Migrate the list generation for food and animals to the respective files

# Consider the case when Ayum is full but health is not full.
# Consider the case when Ayum is not full but health is full.

food_list = [carrot, apple, pasta, orange]

# initial level
wolf = Animals.Animal("Wolf", 10, 100, 10)
lion = Animals.Animal("Lion", 20, 150, 20)
wild_boar = Animals.Animal("Wild Boar", 15, 120, 10)
wild_dog = Animals.Animal("Wild Dog", 7, 80, 8)

# difficult level
dinosaur = Animals.Animal("Dinosaur", 30, 400, 20)
Dragon = Animals.Animal("Dragon", 50, 900, 20)
gorilla = Animals.Animal("Gorilla", 40, 350, 20)

animal_list = [wolf, lion, wild_boar, wild_dog]
difficult_animal_list = [dinosaur, Dragon, gorilla]

game = "Yes"

num_ops = 0

while game == "Yes":
    time.sleep(1)
    if(num_ops > Ayum.age):
        Ayum.age += 1
        num_ops = 0
        print("Congrats! Ayum is an year older now.")
    print("These are the current stats of Ayum: ")
    ayum_stats = Ayum.__dict__.copy()
    ayum_stats.pop("food_inventory", None)

    print(ayum_stats)

    check = Ayum.check_for_stats()

    time.sleep(1)
    print("What do you want to do? Type the option number: ")
    print("1. Eat")
    print("2. Sleep")
    print("3. Search for food")
    print("4. Hunt")
    print("5. Check inventory")
    print("6. Exit")

    if check == True:
        print("Ayum is too weak to do anything. You need to take care of him!")
        time.sleep(1)

    x = int(input())

    if x == 1:
        if len(Ayum.food_inventory) > 0:
            print("Ayum has the following food in his inventory: ")
            for i in range(len(Ayum.food_inventory)):
                print(f"{i+1}. {Ayum.food_inventory[i].name}")
            print("Which food do you want to eat? Type the food number: ")
            food_choice = int(input())
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
        animal = random.choice(animal_list)
        encounter_messages = [
            f"A violent {animal.name} has appeared!",
            f"You are being approached by a {animal.name}!",
            f"A hungry {animal.name} is enraged and coming at you, you must fight!",
        ]
        print(random.choice(encounter_messages))
        while animal.health > 0 and Ayum.health > 0:
            power = Ayum.hunt(animal)
            print(
                f"Ayum attacked {animal.name} with {power} damage. The animal has {animal.health} health left!"
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
            Ayum.attack += random.randint(
                int(animal.attack_power / 2), int(animal.attack_power * 2)
            )
            Ayum.health_limit += random.randint(int(animal.max_health / 10), int(animal.max_health))
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
        print(
            "Ayum has decided to go home. He is tired and wants to sleep. Goodbye! Your final stats are: "
        )
        print("Thanks for taking care of Ayum!")
        print(Ayum.__dict__)
        game = "No"
