numbers = [1, 2, 3, 2, 4,2 ,67, 5, 4, 7, 9]
max_n = numbers[0]

for n in numbers:
    if n > max_n:
        max_n = n
print(max_n)

result = 0

for num in range(101):
    if num % 5 == 0:
        print(num)
        result += num
print ("Sum is: ", result)