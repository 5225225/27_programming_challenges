haswidth = False
hasheight = False

while True:
    try:
        if not haswidth:
            width = int(raw_input("Enter the width of the cuboid: "))
            haswidth = True

        if not hasheight:
            height = int(raw_input("Enter the height of the cuboid: "))
            hasheight = True
        depth = int(raw_input("Enter the depth of the cuboid: "))
        break
    except ValueError:
        print("You must enter numbers only")
        print("")

print("The volume of the cuboid with dimentions {}x{}x{} is {}".format(
    width,
    height,
    depth,
    width*height*depth))
