import random

def cpurem(num):
    return random.choice([1,2,3])

number = random.randrange(20,30)

print("Starting number: {}".format(number))

while True:
    rem = int(raw_input("How many do you want to remove(1,2,3): "))
    if rem in [1,2,3]:
        number -= rem
        if number < 1:
            print("You lose!")
            quit()
        print("{} left".format(number))
        crem = cpurem(number)
        print("CPU removes {}".format(crem))
        number -= crem
        print("{} left".format(number))
        if number < 1:
            print("You win!")
            quit()
    
