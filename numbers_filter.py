n = int(input())

numbers = []

for i in range(n):
    new_numbers = int(input())
    numbers.append(new_numbers)

command = input()
filtered_numbers = []

if command == 'even':
    for j in numbers:
        if j % 2 == 0:
            filtered_numbers.append(j)
elif command == 'odd':
    for j in numbers:
        if j % 2 != 0:
            filtered_numbers.append(j)
elif command == 'positive':
    for j in numbers:
        if j > 0:
            filtered_numbers.append(j)
elif command == 'negative':
    for j in numbers:
        if j < 0:
            filtered_numbers.append(j)

print(filtered_numbers)