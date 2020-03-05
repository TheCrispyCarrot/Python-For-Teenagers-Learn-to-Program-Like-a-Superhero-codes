import random
import time

#varriables used to store super hero statistics
brains = 0
braun = 0
stamina = 0
wisdom = 0
power = 0
constitution = 0
dexterity = 0
speed = 0

answer = ' '

#super powers list
superPowers = ['Flying', 'Super Strength', 'Telepathy', 'Super Speed', 'Can Eat a Lot of Hot Dogs', 'Good at Skipping Rope']

#possible first names
superFirstName = ['Wonder', 'Whatta', 'Rabid', 'Incredable', 'Astonishing', 'Decent', 'Stupendous', 'Above-average', 'That Guy', 'Improbably']

#possible laxt names
superLastName = ['Boy', 'Man', 'Dingo', 'Beefcake', 'Girl', 'Woman', 'Guy', 'Hero', 'Max', 'Dream', 'Macho Man', 'Stallion']



#intorductory text for the user
print("Are you ready to crate a Super Hero using the Super Hero Generator 3000?")

#asks if the user is ready 
print("Enter Y/N")
answer = input()
answer = answer.upper()

#while loop that waits for the answer to be 'y'
while answer != 'Y':
    print("I'm sorry, but you have to choose Y to contenue.")
    print("Choose Y/N")
    answer = input()
    answer = answer.upper()
print("Excellent! Now lets get started!")



#creates the name for the superhero
print("Randomizing name...")
for i in range(3):
    print("..........")
    time.sleep(1)

superName = random.choice(superFirstName) + " " + random.choice(superLastName)
print("Your super name is: " + superName)




#creates a random power fo the hero
print("Generating your power...")
for i in range(2):
    print("..........")
    time.sleep(1)
print("nah... you wouldnt like THAT one...")
for i in range(2):
    print("..........")
    time.sleep(1)
power = random.choice(superPowers)
print("Your power is: " + power)



#randomly generates hero stats
print("Now lets generate your stats!")
for i in range(3):
    print("..........")
    time.sleep(1)

#randomly generates stats
brains = random.randint(1, 20)
braun = random.randint(i, 20)
stamina = random.randint(1, 20)
wisdom = random.randint(1, 20)
constitution = random.randint(1, 20)
dexterity = random.randint(1, 20)
speed = random.randint(1, 20)

#printing stats
print("Your new stasts are:")
print("Brains: ", brains)
print("Braun: ", braun)
print("Stamina: ", stamina)
print("Wisdom: ", wisdom)
print("Constitution: ", constitution)
print("Dexterity: ", dexterity)
print("Speed: ", speed)
print(" ")
time.sleep(1)

#puts it all in one cluster
print("Now lets put it all togehter!")
time.sleep(0.5)
print("..........")
time.sleep(1)
print("Name: " + superName)
print("Power: " + power)
print(" ")

print("Stats:")
print("Brains: ", brains)
print("Braun: ", braun)
print("Stamina: ", stamina)
print("Wisdom: ", wisdom)
print("Constitution: ", constitution)
print("Dexterity: ", dexterity)
print("Speed: ", speed)
print(" ")

print("Hope you like it!")
print("(If not you can always generate another hero)")
