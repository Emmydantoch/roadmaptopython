# while loop
value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1


while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("value is now equel to " + str(value))


# for loop
# for value in range(1, 11):
#     print(value)
#     if value == 5:
#         break
#     print(value)
# else:
#     print("value is now equel to " + str(value))

# names = [
#     "John",
#     "Jane",
#     "Jack",
#     "Jill" "Jane",
#     "Jack",
# ]
# for name in names:
#     print(name)
#     if name == "Jack":
#         break

# for name in names:
#     if name == "Jack":
#         continue
#     print(name)
# else:
#     print("name is now equel to " + str(name))


# for name in range(1, 11):
#     print(name)
#     if name == 5:
#         break

# nested loops
names = [
    "John",
    "Jane",
    "Jack",
    "Jill" "Jane",
    "Jack",
]
actions = [
    "eat",
    "drink",
    "sleep",
    "play",
    "work",
    "rest",
]
for name in names:
    for action in actions:
        print(name + " " + action)
        if name == "Jack":
            break
    else:
        print("name is now equel to " + str(name))
