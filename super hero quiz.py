wonderBoyScore = 82

#intro text
print("aCongrats on finnishing your Super-Hero Intelligence and Reasoniong Test.")
print("or, S Q U I R T for short.")
print("lets see if you passed.")
print("A passing score means you are liscenced to be a sidekick.")

#checks to see if Wonder Boy passed or not
if wonderBoyScore > 60:
    print("Here are your results:")

    if wonderBoyScore > 60 and wonderBoyScore < 70:
        print("Well, you passed by the skin of your teeth.")
    elif wonderBoyScore >= 70 and wonderBoyScore < 80:
        print("You passed... average isnt so bad. Im sure youll make up for it with heart.")
    elif wonderBoyScore >= 80 and wonderBoyScore < 90:
        print("Wow, not bad at all! Youre a regular B+ player!")
    elif wonderBoyScore >= 90:
        print("Great job! A+")
else:
    print("Sorry buddy, you failed.")
