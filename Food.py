class food:
    name = ""
    energy = ""

    def __init__(self, name, energy) -> None:
        self.name = name
        self.energy = energy
    
    def __str__(self) -> str:
        return self.name
carrot = food("Carrot", 10)
apple = food("Apple", 20)
pasta = food("Pasta", 7)

food_list = [carrot, apple, pasta]    