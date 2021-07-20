import random
my_list = []

# Generate 10 random elements from 0 to 100 and append to list
for _ in range(10):
    my_list.append(random.randint(0, 100))

# Show only elements that are greater than 10
for element in my_list:
    if element > 10:
        print(element)
