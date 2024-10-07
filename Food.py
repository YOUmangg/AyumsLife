class food:
    name = ""
    energy = 0

    def __init__(self, name, energy) -> None:
        self.name = name
        self.energy = energy
    
    def __str__(self) -> str:
        return self.name
    
carrot = food("Carrot", 10)
apple = food("Apple", 20)
pasta = food("Pasta", 7)
orange = food("Orange", 15)
banana = food("Banana", 10)
dhaniya = food("Dhaniya", 2)
berries = food("Berries", 12)


food_list = [carrot, apple, pasta, orange, banana, dhaniya, berries]    