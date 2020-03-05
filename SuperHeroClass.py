import random
import time



# creates the superhero class as a template for our superheros
class Superhero():

    # initializes class and sets the attributes\
    def _init_(self):
        self.superName = " "
        self.power = " "
        self.brains = brains
        self.braun = braun
        self.stamina = stamina
        self.wisdom = wisdom
        self.constitution = constitution
        self.deterity = dexterity
        self.speed = speed

    # adding random values to the attributes
    brains = random.randint(1, 20)
    braun = random.randint(1, 20)
    stamina = random.randint(1, 20)
    wisdom = random.randint(1, 20)
    constitution = random.randint(1, 20)
    dexterity = random.randint(1, 20)
    speed = random.randint(1, 20)

    #super powers list
    superPowers = ['Flying', 'Super Strength', 'Telepathy', 'Super Speed', 'Can Eat a Lot of Hot Dogs', 'Good at Skipping Rope']

    #chooses a random power
    power = random.choice(superPowers)
    
    #possible first names
    superFirstName = ['Wonder', 'Whatta', 'Rabid', 'Incredable', 'Astonishing', 'Decent', 'Stupendous', 'Above-average', 'That Guy', 'Improbably']
    #possible laxt names
    superLastName = ['Boy', 'Man', 'Dingo', 'Beefcake', 'Girl', 'Woman', 'Guy', 'Hero', 'Max', 'Dream', 'Macho Man', 'Stallion']

    #chooses a random name
    superName = random.choice(superFirstName) + " " + random.choice(superLastName)

# creates a mutate superhero subclass
class Mutate(Superhero):
    def __init__(self):
        Superhero.__init__(self)
        print("You created a Mutate")
        self.speed = self.speed + 10
    
#creates a robot superhero subclass
class Robot(Superhero):
    def __init__(self):
        Superhero.__init__(self)
        print("You created a Robot")
        self.braun = self.braun + 10
        

###########################################################################################################

print("Are you ready to create a superhero witht the Super Hero Generator 3000?")
# ask user for ansewr (make it all caps tho so its ez)
print("Enter Y/N:")
answer = input('> ')
answer = (answer.upper())

#loop that doesent pass until Y is enteres
while answer != "Y":
    print("I'm soyy, but you have to enter Y to contenue!")
    print("Choose Y/N:")
    answer = input('> ')
    answer = (answer.upper())
print("Great, lets get started!")
print(" ")

# lets the user thier class of superhero
print("Choose form the following hero opitons:")
print("Press 1 for a Regular Superhero")
print("Press 2 for a Mutate Superhero")
print("Press 3 for a Robot Superhero")
answer2 = input('> ')

if answer2 == '1': 
    #creates the superhero object
    hero = Superhero()

    # prints out result of created object and paramenters
    print("you chose to crate a Regular Superhero!")
    print("Generating name, power, and stats:")
    
    # creating dramatic effect
    for i in range(1):
        print("..........")
        time.sleep(1)
        print("Nah... you wouldnt like THAT one...")
        time.sleep(1)
    for i in range(2):
        print("..........")
        time.sleep(1)
    print(" ")
    # print the hero object random stats
    print("Your name is %s." % (hero.superName))
    print("Your super power is: %s." % (hero.power))
    print("Your new stats are:")
    print("Brains:", hero.brains)
    print("Braun:", hero.braun)
    print("Stamina:", hero.stamina)
    print("Wisdom:", hero.wisdom)
    print("Constitution:", hero.constitution)
    print("Dexterity:", hero.dexterity)
    print("Speed:", hero.speed)
    print(" ")

elif answer2 == '2':
    #creates the mutate object
    hero2 = Mutate()

    # prints out result of created object and paramenters
    print("you chose to crate a Mutate Superhero!")
    print("Generating name, power, and stats:")
    
    # creating dramatic effect
    for i in range(1):
        print("..........")
        time.sleep(1)
        print("Nah... you wouldnt like THAT one...")
        time.sleep(1)
    for i in range(2):
        print("..........")
        time.sleep(1)
    print(" ")
    print("Your name is %s." % (hero2.superName))
    print("Your super power is: %s." % (hero2.power))
    print("Your new stats are:")
    print("Brains:", hero2.brains)
    print("Braun:", hero2.braun)
    print("Stamina:", hero2.stamina)
    print("Wisdom:", hero2.wisdom)
    print("Constitution:", hero2.constitution)
    print("Dexterity:", hero2.dexterity)
    print("Speed:", hero2.speed)
    print(" ")
        
elif answer2 == '3':
    #creates the robot object
    hero3 = Robot()

    # prints out result of created object and paramenters
    print("you chose to crate a Robot Superhero!")
    print("Generating name, power, and stats:")
    
    # creating dramatic effect
    for i in range(1):
        print("..........")
        time.sleep(1)
        print("Nah... you wouldnt like THAT one...")
        time.sleep(1)
    for i in range(2):
        print("..........")
        time.sleep(1)
    print(" ")
    # print the hero object random stats
    print("Your name is %s." % (hero3.superName))
    print("Your super power is: %s." % (hero3.power))
    print("Your new stats are:")
    print("Brains:", hero3.brains)
    print("Braun:", hero3.braun)
    print("Stamina:", hero3.stamina)
    print("Wisdom:", hero3.wisdom)
    print("Constitution:", hero3.constitution)
    print("Dexterity:", hero3.dexterity)
    print("Speed:", hero3.speed)
    print(" ")

else:
    print("You did not choose the proper answer! Program will no self-destruct in...")
    for i in range(5, 0, -1):
        time.sleep(1)
        print(i,"...")
    time.sleep(1)
    print("BOOM!!!")




    
