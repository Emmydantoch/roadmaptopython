# # List of tuples
# users = ["Alice", "Bob", "Charlie"]

# data = ["Alice", 25, "Engineer"]

# emptylist = []

# print("Dave" in emptylist)  # False
# print("Alice" in users)  # True
# print("Alice" not in users)  # False
# print(users.index("Alice"))  # 0
# print(users.index("Bob"))  # 1

# print(users[0:2])  # ['Alice', 'Bob']
# print(users[0:3])  # ['Alice', 'Bob', 'Charlie']
# print(users[1:])  # ['Bob', 'Charlie']
# print(users[:2])  # ['Alice', 'Bob']
# print(users[1:2])  # ['Bob']
# print(users[1:3])  # ['Bob', 'Charlie']
# print(users[-3:-1])  # ['Alice', 'Bob']


# print(len(data))

# users += ["jason"]
# print(users)

# users.extend(["eddy", "alex"])
# print(users)

# users.append("Dave")
# print(users)  # ['Alice', 'Bob', 'Charlie', 'Dave']

# users.insert(0, "Eve")
# print(users)  # ['Eve', 'Alice', 'Bob', 'Charlie', 'Dave']

# users.remove("Alice")
# print(users)  # ['Eve', 'Bob', 'Charlie', 'Dave']

# users[2:2] = ["Bob", "Charlie"]
# print(users)

# users.pop()
# print(users)  # ['Bob', 'Charlie']

# users.sort()
# print(users)  # ['Bob', 'Charlie']

# users.reverse()
# print(users)  # ['Charlie', 'Bob']

# del users[1]
# print(users)  # ['Charlie']

# users.clear()
# print(users)  # []

nums = [10, 20, 30, 40, 50]
nums.reverse()
print(nums)  # [50, 40, 30, 20, 10]

# nums.sort(reverse=True)
# print(nums)  # [50, 40, 30, 20, 10]

print(sorted(nums))  # [10, 20, 30, 40, 50]
print(sorted(nums, reverse=True))  # [50, 40, 30, 20, 10]

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)  # [50, 40, 30, 20, 10]
print(mynums)  # [50, 40, 30, 20, 10]
mycopy.sort()
print(mycopy)  # [10, 20, 30, 40, 50]
print(nums)  # [50, 40, 30, 20, 10]

print(type(nums))  # <class 'list'>

mylist = list([1, "neil", True])
print(mylist)  # [1, 'neil', True]

# tuple
mytuple = tuple([12, "Emma", True])

anothertuple = (1, 2, 3, 8)

print(mytuple)  # (12, 'Emma', True)
print(type(anothertuple))  # <class 'tuple'>

newlist = list(mytuple)
newlist.append("sun")
newtuple = tuple(newlist)
print(newtuple)  # (12, 'Emma', True, 'sun')


# packing and unpacking new tuples (assigning values to a tuple)
(one, two, *hey) = anothertuple
print(one)  # 1
print(two)  # 2
print(hey)  # [3, 8]

print(anothertuple.count(1))  # 1
