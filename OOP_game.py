class Ninja:
    def __init__(self, name, speed, attack_power,defense, ability, health):
        self.name = name 
        self.speed = speed 
        self.attack_power = attack_power 
        self.defense = defense
        self.ability = ability 
        self.ability = health
    def attack(self, target, amount):
        target.make_withdrawl(target.health)
        target.health -= self.attack_power

class Viking:
    def __init__(self, name, speed, attack_power,defense, ability, health):
        self.name = name 
        self.speed = speed 
        self.attack_power = attack_power 
        self.defense = defense
        self.ability = ability 
        self.health = health
    def attack(self, target, amount):
        target.make_withdrawl(target.health)
        target.health -= self.attack_power 

class Pirate:
    def __init__(self, name, speed, attack_power,defense, ability, health):
        self.name = name 
        self.speed = speed 
        self.attack_power = attack_power 
        self.defense = defense
        self.ability = ability 
        self.health = health

    def attack(self, target, amount):
        target.make_withdrawl(target.health)
        target.health -= self.attack_power



ninja1 = Ninja("Ciso", 70, 50, 70, "stealth", 100)
pirate1 = Pirate("Captain Jack", 30, 65, 90, "cannon blast", 100 )
viking1 = Viking("Ragnahr", 40, 60, 60, "berserk", 100)

# Make a function that 

