"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Hero():
    def __init__(self, hero_health, hero_power):
        self.health = hero_health
        self.power = hero_power
    
    def attack(self,Goblin):
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ")
        user_input = input()
        if user_input =="1":
            Goblin.health -= self.power
            print("You do {} damage to the goblin.".format(self.power))
        elif Goblin.health <= 0:
            print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
        else:
            print("Invalid input %r" % user_input)

    def alive(self):
        self.health > 0
    
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))


class Goblin(): 
    def __init__(self, goblin_health, goblin_power):
        self.health = goblin_health
        self.power = goblin_power

    def attack(self, Hero):
        if self.health > 0:
            # Goblin attacks hero
            Hero.health -= self.power
            print("The goblin does {0} damage to you.".format(self.power))
        if Hero.health <= 0:
            print("You are dead.")

    def alive(self):
        self.health > 0
    
    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))





def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2
    myhero = Hero(10,5)
    mygoblin = Goblin(6,2)

    while mygoblin.alive and myhero.alive:
        myhero.attack(mygoblin)
        mygoblin.attack(myhero)

        myhero.print_status
        mygoblin.print_status

main()
