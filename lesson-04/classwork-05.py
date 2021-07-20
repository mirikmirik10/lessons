print("Enter start number:")
start_number = int(input())

print("Enter end number:")
end_number = int(input())

# Generate elements from start_number to end_number (including)
my_sum = 0
for element in range(start_number, end_number + 1):
    # Calculate element's cube powers
    my_sum += element ** 3

print(my_sum)
