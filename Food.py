class food:
    name = ""
    energy = 0

    def __init__(self, name, energy) -> None:
        self.name = name
        self.energy = energy

    @staticmethod
    def get_food_by_name(name):
        return next((food for food in food_list if food.name == name), None)

    def __str__(self) -> str:
        return self.name


carrot = food("Carrot", 10)
apple = food("Apple", 20)
pasta = food("Pasta", 7)
orange = food("Orange", 15)
banana = food("Banana", 10)
dhaniya = food("Dhaniya", 2)
berries = food("Berries", 12)
chicken = food("Chicken", 17)


food_list = [carrot, apple, pasta, orange, banana, dhaniya, berries, chicken]
