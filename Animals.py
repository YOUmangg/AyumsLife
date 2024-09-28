import random

class Animal:

    max_health = 0

    def __init__(self, name, attack_power, health, energy):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        self.energy = energy
        self.max_health = self.health

        #Will have to set health limits and curr_health type of thing.

    def attack(self, other):
        power = random.randint(self.attack_power, self.attack_power*2)
        other.health -= power
        return power


            