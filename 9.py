import random

suits = [
    "Hearts",
    "Spades",
    "Diamonds",
    "Clubs",

]

ranks = [
    "Ace",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
]

while True:
    raw_input("Press enter for a card")
    print("{} of {}".format(random.choice(ranks), random.choice(suits)))
