import random   #imports the random function

#randomly generates the heros status
strength = random.randint(1, 20)
intelligence = random.randint(1, 20)
endurance = random.randint(1, 20)
wisdom = random.randint(1, 20)

#prints the players statistics
print("Your character's statistics are:")
print("Strength:", strength)
print("Intelligence:", intelligence)
print("Endurance:", endurance)
print("Wisdom:", wisdom)
