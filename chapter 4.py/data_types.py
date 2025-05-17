# # literal assignment
# first = "Dave"
# last = "Daniel"

# print(type(first))


# # constructor function
# fish = str("meat")
# print(type(fish))

# # concatenation
# full_name = first + " " + last
# print(full_name)

# full_name += "!"
# print(full_name)

# full_name = f"{first} {last}"
# print(full_name)

# # casting a number to a string
# age = 45
# age = str(age)
# print(type(age))

# decade = str(1960)
# print(type(decade))
# print(decade)

# statement = "since The year " + decade + "and below"
# print(statement)

# # multi-line string
# multiline = """
# Hey, how are you?
#                         all good?
# """
# print(multiline)


# # Escaping special characters
# sentence = 'I\'m a "Python" programmer'
# print(sentence)

# sentence = "I'm back at work!\n\nwhere's this at\\located?"
# print(sentence)

# # string methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", "ok"))
# print(multiline)

# print(len(multiline))
# multiline += "                              "
# multiline = "           " + multiline
# print(len(multiline))

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

# # Build a menu
# title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, "=") + "$4".rjust(4))
# print("Muffin".ljust(16, "=") + "$8".rjust(4))
# print("Tea".ljust(16, "=") + "$6".rjust(4))

# # string index values
# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[1:])

# Boalean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# integer data type
price = 100
best_price = int(99)
print(type(price))
print(isinstance(best_price, int))
# print(isinstance(price, float))
# print(isinstance(price, str))
# print(isinstance(price, bool))
# print(isinstance(price, complex))
# print(isinstance(price, list))
# print(isinstance(price, tuple))
# print(isinstance(price, dict))
# print(isinstance(price, set))
# print(isinstance(price, range))
# print(isinstance(price, bytes))
print(isinstance(price, bytearray))
# print(isinstance(price, memoryview))
# print(isinstance(price, object))
# print(isinstance(price, type))

# a brief explanation of each data type you're checking with isinstance():

# ✅ complex
# A complex number has a real and imaginary part.

# Example: z = 3 + 4j

# Used in scientific computing or simulations.

# ✅ tuple
# A tuple is an immutable (unchangeable) sequence of items.

# Example: my_tuple = (1, "hello", 3.5)

# Useful for grouping different types of data.

# ✅ dict (dictionary)
# A dictionary stores data as key-value pairs.

# Example: my_dict = {"name": "Dave", "age": 30}

# Used for structured data and fast lookup by keys.

# ✅ bytes
# A bytes object is an immutable sequence of bytes (like a string, but for binary data).

# Example: b = b"hello"

# Used for file I/O, networking, or working with binary formats.

# ✅ bytearray
# Similar to bytes, but mutable (you can change it).

# Example: ba = bytearray([65, 66, 67]) # ABC

# Used when you need to modify binary data.

# ✅ memoryview
# A memoryview lets you access the internal data of bytes or bytearray without copying.

# Example: mv = memoryview(b"hello")

# Efficient for large data processing, like image/video buffers.

# float type
gpa = 3.58
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 3 + 4j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Buit-in functions
print(abs(gpa))
print(round(gpa))


import math

print(math.pi)

print(math.sqrt(16))
print(math.ceil(gpa))
print(math.floor(gpa))
print(math.pow(2, 3))

# casting a string to a number
zip_code = "12345"
zip_value = int(zip_code)
print(type(zip_value))
