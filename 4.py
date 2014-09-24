answer = raw_input("Want to calculate time, distance or speed: ")

if answer == "time":
    try:
        distance = int(raw_input("Miles: "))
        speed = int(raw_input("Miles Per Hour: "))
        print("It will take {} hours to travel {} miles".format(speed/distance))
    except ValueError:
        print("You must enter numbers only")
        quit()


elif answer == "distance":
    try:
        time = int(raw_input("Hours: "))
        speed = int(raw_input("Miles Per Hour: "))
        print("You can go {} miles".format(time*speed))
    except ValueError:
        print("You must enter numbers only")
        quit()

elif answer == "speed":
    try:
        time = int(raw_input("Hours: "))
        distance = int(raw_input("Miles: "))
        print("You will have to travel {} MPH".format(distance/time))
    except ValueError:
        print("You must enter numbers only")
        quit()

else:
    print("Don't understand your answer")
