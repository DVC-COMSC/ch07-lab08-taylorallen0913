numbers = list(map(int, input().split()))
number = int(input())

index_to_insert = -1

for i in range(1, len(numbers)):
    if number < numbers[0]:
        numbers.insert(0, number)
        break
    if number > numbers[len(numbers) - 1]:
        numbers.insert(len(numbers), number)
        break
    if number < numbers[i]:
        numbers.insert(i, number)
        break

print(numbers)