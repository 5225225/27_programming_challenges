import random

num = random.randint(1,13)
nextnum = -1

print("Starting number: {}".format(num))

tries = 10
lives = 2
while True:
    guess = raw_input("(H)igher or (L)ower: ")
    nextnum = random.randint(1,13)
    print("Next number: {}".format(nextnum))
    if guess == "H":
        if nextnum > num:
            tries -= 1
        else:
            lives -= 1
            tries -= 1
            if lives == 1:
                print("You have one life left!")
    elif guess == "L":
        if nextnum < num:
            tries -= 1
        else:
            tries -= 1
            lives -= 1
            if lives == 1:
                print("You have one life left!")
    num = nextnum
    if tries == 0:
        print("You win!")
        quit()
    if lives == 0:
        print("You ran out of lives!")
        quit()
