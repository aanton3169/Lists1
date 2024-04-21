n = int(input())

positive_nums = []
negative_nums = []
for i in range(n):
    number = int(input())

    if number > 0:
        positive_nums.append(number)
    else:
        negative_nums.append(number)

count_of_positive_numbers = len(positive_nums)
sum_of_negatives = sum(negative_nums)
print(positive_nums)
print(negative_nums)
print(count_of_positive_numbers)
print(sum_of_negatives)