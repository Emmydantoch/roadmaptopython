# r = Read
# w = Write
# a = Append
# x = Exclusive creation
# b = Binary mode
# t = Text mode
# + = Read and write
# r+ = Read and write (file must exist)
# w+ = Write and read (creates file if it doesn't exist, truncates if it does)
# a+ = Append and read (creates file if it doesn't exist)
# x+ = Exclusive creation and read (fails if file exists)


# Read - error if it doesn't exist

# f = open("chapter22/bill number five.txt")
# print(f.read())


# #print(f.read(5))


# # print(f.readline())


# for line in f:
#     print(line)

# f.close()

# try:
#     f = open("chapter22/bill number five.txt")
#     print(f.read())
# except FileNotFoundError:
#     print("File not found")
# finally:
#     f.close()

# #append mode - to create a new file if it doesn't exist
# f = open("chapter22/bill number five.txt", "a")
# f.write("\nThis is a new line added to the file.")
# f.close()

# #read a file
# f = open("chapter22/bill number five.txt", "r")
# print(f.read())
# f.close()

# # write to a file
# f = open("chapter22/bill number five.txt", "w")
# f.write("i deleted all of the content.")
# f.close()

# # read the file again
# f = open("chapter22/bill number five.txt", "r")
# print(f.read())
# f.close()

# two ways to create a new file, create a new file if it doesn't exist
# f = open("chapter22/new_file.txt", "x")  # Exclusive creation
# f.write("This is a new file created with exclusive creation mode.")
# f.close()


# Delete a file
import os

if os.path.exists("chapter22/new_file.txt"):
    os.remove("chapter22/new_file.txt")
    print("File deleted successfully.")
