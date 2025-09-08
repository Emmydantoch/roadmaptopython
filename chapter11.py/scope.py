# scope
name = "John"


def greeting(firstname):
    color = "blue"
    print(color)  # This will print "blue" because 'color' is defined in this scope
    print(name)


# greeting("Doe")
# print(color)  # This will raise an error because 'color' is not defined in this scope


def another():
    greeting("John")


another()  # print(name)  # This will not raise an error because 'name' is defined in the global scope
#caling a function inside another function
def another():
    color = "blue"

    def greeting(firstname):
        print(color)  # This will print "blue" because 'color' is defined in this scope
        print(name)

#     greeting("John")


# another()

count = 1


def another():
    color = "blue"
    global count
    count += 1  # Increment the global count variable
    print(count)

    def greeting(firstname):
        nonlocal color
        color = "red"  # Uncommenting this line would change the 'color' variable in the enclosing scope
        print(color)  # This will print "blue" because 'color' is defined in this scope
        print(name)

    greeting("John")


# another()
