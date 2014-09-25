gates = [
    "OR",
    "AND",
    "XOR",
    "NAND",
    "NOR",
]

def tobool(x):
    if x == 0:
        return False
    elif x == 1:
        return True

gate = raw_input("Enter logic gate : ")
if not gate in gates:
    print("Invalid gate")
    quit()

i1 = tobool(int(raw_input("Enter first input : ")))
i2 = tobool(int(raw_input("Enter second input : ")))

result = -1

if gate == "OR":
    result = i1 or i2

elif gate == "AND":
    result = i1 and i2

elif gate == "XOR":
    result = i1 ^ i2

elif gate == "NAND":
    result = not i1 and i2

elif gate == "NOR":
    result = not i1 or i2

print(result)
