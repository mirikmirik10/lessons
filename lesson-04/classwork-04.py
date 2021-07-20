import random

while True:
    # Generate random int from 1 to 10
    my_int = random.randint(1, 10)

    # If element equals to 7 we stop cycle and exit program
    if my_int == 7:
        break

    # Else we print this element
    print(my_int)
