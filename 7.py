import time
import string
import json

alpha = string.ascii_lowercase
alpha = "test"

raw_input("Press enter when ready to type the alphabet")
start = time.time()

useralpha = raw_input("Alphabet: ")

if useralpha == alpha:
    score = time.time() - start
    print("You typed the alphabet in {0:.2} seconds!".format(score))
    hs = open("highscore", "r+")
    newscore = False
    x = {}
    try:
        x = json.load(hs)

        if x["score"] > score:
            newscore = True
    except ValueError: 
        newscore = True
    

    if newscore:
        print("That's a new highscore!")
        name = raw_input("Enter your name: ")
        newscore = {
            "name": name,
            "score": score,
        }
        json.dump(newscore, hs)
    else:
        print("You were beaten by {}, they got {:.2} seconds".format(
            x["name"],
            x["score"]
        ))
    hs.close()
