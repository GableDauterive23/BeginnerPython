import numpy

# Initialize an empty list to store the numbers
numbers = []

# Loop to get 6 numbers from the user
for i in range(6):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate the average
average = sum(numbers) / len(numbers)

# Output the average
print(f"The average of the entered numbers is: {average}")

