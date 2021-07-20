print("Enter divider:")
my_number = int(input())

# Generate 100 random elements from 1 to 100 (last element not included)
for element in range(1, 101):
    if element % my_number == 0:
        print(element)
