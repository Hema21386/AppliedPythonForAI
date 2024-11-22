import random

# ACII values to get the dice picture as below.
#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

# creating the dictionary for the dice, a tuple made of strings
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"), 
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"), 
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")     
}

dice = []
total=0
num_of_dice=int(input("How many dice..? "))

#using random library to get the dice values from 1 till 6 where the randint method
random.randint(1, 6)

#looping through the number of dice to generate random values and appedinf to the dice
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

"""
for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)
"""
# looping through the dice design strings line by line
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") # end with value empty string - used to move to next line
    print()

for die in dice:
    total += die

print (f"total: {total}")

#print(dice)