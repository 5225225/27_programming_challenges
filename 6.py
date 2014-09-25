import time
raw_input("Press enter when ready")
start = time.time()
raw_input("Press enter after 10 seconds")
delay = time.time() - start

print("You were {0:.2f} seconds off 10 seconds".format(abs(delay - 10)))
