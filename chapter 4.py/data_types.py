# literal assignment
first = "Dave"
last = "Daniel"

print(type(first))


# constructor function
fish = str("meat")
print(type(fish))

# concatenation
full_name = first + " " + last
print(full_name)

full_name += "!"
print(full_name)

full_name = f"{first} {last}"
print(full_name)

# casting a number to a string
age = 45
age = str(age)
print(type(age))

decade = str(1960)
print(type(decade))
print(decade)

statement = "since The year " + decade + "and below"
print(statement)

# multi-line string
multiline = """
Hey, how are you?
                        all good?
"""
print(multiline)


# Escaping special characters
sentence = 'I\'m a "Python" programmer'
print(sentence)

sentence = "I'm back at work!\n\nwhere's this at\\located?"
print(sentence)
