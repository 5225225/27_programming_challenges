import random

def whowon(p1, p2):
    if p1 == "rock":
        if p2 == "rock":
            return "draw"
        if p2 == "paper":
            return "p2"
        if p2 == "scissors":
            return "p1"

    elif p1 == "paper":
        if p2 == "rock":
            return "p1"
        if p2 == "paper":
            return "draw"
        if p2 == "scissors":
            return "p2"

    elif p1 == "scissors":
        if p2 == "rock":
            return "p2"
        if p2 == "paper":
            return "p1"
        if p2 == "scissors":
            return "draw"

choices = [
    "rock",
    "paper",
    "scissors",
]

scores = {
    "win": 0,
    "lose": 0,
    "draw": 0,
}
while True:
    choice = raw_input("Choose either rock, paper or scissors: ")
    if not choice in choices:
        print("invalid choice")
        quit()
    CPUchoice = random.choice(choices)
    winner = whowon(choice, CPUchoice)
    if winner == "p1":
        scores["win"] += 1
        print("You win. WINS: {}".format(scores["win"]))
    elif winner == "p2":
        scores["lose"] += 1
        print("You lose! LOSSES: {}".format(scores["lose"]))
    elif winner == "draw":
        scores["draw"] += 1
        print("It's a draw! DRAWS: {}".format(scores["draw"]))

