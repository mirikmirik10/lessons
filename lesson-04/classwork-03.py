print("Enter elements count:")
my_number = int(input())

# Generate elements from 1 to my_number (including)
my_sum = 0
for element in range(1, my_number + 1):
    # Calculate element's cube powers
    my_sum += element ** 3

print(my_sum)
