def squared(num):
    return num * num


print(squared(5))  # Output: 25


def addTwo(num):
    return num + 2


print(addTwo(5))  # Output: 7


def sum(a, b):
    return a + b


print(sum(5, 10))  # Output: 15


########################## Lambda functions
def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)
print(addTen(5))  # Output: 15
print(addTwenty(5))  # Output: 25

lambda num: num + num
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda num: num * num, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


lambda num: num % 2 != 0

odd_numbers = list(filter(lambda num: num % 2 != 0, numbers))
print(odd_numbers)  # Output: [1, 3, 5]


# creating a loop

from functools import reduce

lambda acc, curr: acc + curr
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda acc, curr: acc + curr, numbers)
print(total)  # Output: 15

names = ["Alice", "Bob", "Charlie"]

char_count = reduce(lambda acc, curr: acc * len(curr), names, 0)

print(char_count)  # Output: 15 (5 + 3 + 7)
# Using lambda functions with map, filter, and reduce
