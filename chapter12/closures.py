# closures
## A closure is a function that remembers the environment in which it was created. it has acess to its parent function
# closures
## A closure is a function that remembers the environment in which it was created. it has acess to its parent function
def make_adder(n):
    def adder(x):
        return x + n

    return adder


# Create adder functions with different values of n
add_5 = make_adder(5)
add_10 = make_adder(10)

# Test the adder functions
print(add_5(3))  # Output: 8  (3 + 5)
print(add_10(3))  # Output: 13 (3 + 10)


# Multiplier example
def make_multiplier_of(n):
    def multiplier(x):
        return x * n

    return multiplier


# Create multiplier functions
times_3 = make_multiplier_of(3)
times_5 = make_multiplier_of(5)

# Test the multiplier functions
print(times_3(4))  # Output: 12 (4 * 3)
print(times_5(4))  # Output: 20 (4 * 5)


def parent_function(person):
    Coins = 3

    def play_game():
        nonlocal Coins
        Coins -= 1

        if Coins > 1:
            print("\n" + person + " has " + str(Coins) + " coins left.")
        elif Coins == 1:
            print("\n" + person + " has " + str(Coins) + " coin left.")
        else:
            print("\n" + person + " is out of  coins.")

    return play_game


tommy = parent_function("Tommy")
jenny = parent_function("Jenny")

tommy()
tommy()

jenny()

tommy()
