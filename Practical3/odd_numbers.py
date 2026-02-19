# Find all odd numbers between 1 to 100

odd_numbers = []

for i in range(1, 101):
    if i % 2 != 0:
        odd_numbers.append(i)

print("List of Odd Numbers:", odd_numbers)
print("Minimum Odd Number:", min(odd_numbers))
print("Maximum Odd Number:", max(odd_numbers))
print("Sum of Odd Numbers:", sum(odd_numbers))


# Odd numbers between 1 and 50

odd_numbers = []

for i in range(1, 51):
    if i % 2 != 0:
        odd_numbers.append(i)

# List of odd numbers
print("List of odd numbers between 1 and 50:")
print(odd_numbers)

# Minimum three odd numbers
print("Total three minimum odd numbers:")
print(odd_numbers[:3])

# Maximum three odd numbers
print("Total three maximum odd numbers:")
print(odd_numbers[-3:])

# Average of odd numbers
average = sum(odd_numbers) / len(odd_numbers)
print("Average of odd numbers between 1 and 50:")
print(average)
