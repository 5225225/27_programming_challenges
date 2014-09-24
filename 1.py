import sys
import os
import random


class joke:
    def __init__(self, main, punchline):
        self.main = main
        self.punchline = punchline

jokes = [
    joke("Why did the chicken cross the road?", "To get to the other side!")
    ]

joke = random.choice(jokes)

print(joke.main)

raw_input()

if os.name == "posix":
    sys.stdout.write("\x1b[31m{}\x1b[m\n".format(joke.punchline))
else:
    print(joke.punchline)
