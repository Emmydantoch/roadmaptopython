# def add_one(num):
#     if num >= 9:
#         return num + 1

#     total = num + 1
#     print(total)

#     return add_one(total)


# mynewtotal = add_one(0)
# print(mynewtotal)


def ask_user(value="Y"):
    if value.upper() != "Y":
        print("Goodbye!")
        return

    user_input = input("Do you want to continue? (Y/N): ").upper()
    ask_user(user_input)


# Start the recursion
ask_user()
