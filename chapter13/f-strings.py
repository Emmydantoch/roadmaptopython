# f_strings

# f-strings are a way to format strings in Python, introduced in Python 3.6.
# They allow you to embed expressions inside string literals, using curly braces `{}`.
person = "John"
coins = 30

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %d coins left." % (person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(person, coins)
print(message)

message = "\n{person} has {coins} coins left.".format(person=person, coins=coins)
print(message)

player = {"name": "John", "coins": 30}
message = "\n{name} has {coins} coins left.".format(**player)
print(message)
