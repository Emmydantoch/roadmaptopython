# commandline arguments
# What Is a Command-Line Argument in Python?
# Command-line arguments are inputs passed to a Python script when you run it from the terminal or command prompt. They allow your script to accept dynamic input without hardcoding values inside the script.
# Example:If you have a file called greet.py, and you run: python greet.py Dave,   You just passed "Dave" as a command-line argument.

# How to Access Them in Python:
# You use the sys module.

import sys

print("Script name:", sys.argv[0])  # Name of the script
print("Argument passed:", sys.argv[1])  # First argument
# If you run python greet.py Dave, it will output:

# Script name: greet.py
# Argument passed: Dave

# note You can pass multiple arguments like:python script.py arg1 arg2 arg3

# example 2
# Using sys.argv (Basic Command-Line Argument Handling)
#

# Run this from terminal:

# python script.py Alice 25


# Using argparse (User-Friendly, Validated Arguments)

# import argparse

# # Create the parser
# parser = argparse.ArgumentParser(description="Greet a user with their name and age.")

# # Add arguments
# parser.add_argument("name", type=str, help="Your name")
# parser.add_argument("age", type=int, help="Your age")

# # Parse arguments
# args = parser.parse_args()

# # Use the arguments
# print(f"Hello, {args.name}! You are {args.age} years old.")

# Run this from terminal:

# python script.py Daniel 30


# framename; hello_person.py
import argparse

# parser = argparse.ArgumentParser(description="provides a personal greeting.")
# parser.add_argument("-n", "--name", metavar="name", help="the name of the person to greet", required=True)
# args = parser.parse_args()
# msg = f"Hello, {args.name}!"
# print(msg)


# example 2
import argparse


def hello(name, lang):
    greetings = {
        "english": "Hello",
        "spanish": "Hola",
        "french": "Bonjour",
        "german": "Hallo",
    }
    greeting = greetings.get(lang.lower(), "Hello")
    if not name.strip():
        raise ValueError("Name cannot be empty")
    return f"{greeting}, {name}!"


parser = argparse.ArgumentParser(description="provides a personal greeting.")
parser.add_argument(
    "-n",
    "--name",
    metavar="name",
    help="the name of the person to greet",
    required=True,
)
parser.add_argument(
    "-l",
    "--lang",
    metavar="language",
    required=False,
    default="english",
    choices=["english", "spanish", "french", "german"],
    help="language for greeting (default: english)",
)

args = parser.parse_args()
try:
    result = hello(args.name, args.lang)
    print(result)
except ValueError as e:
    print(f"Error: {e}")

# hello(args.name, args.lang)

# Why argparse is better:
# Gives help messages automatically (-h or --help)

# Validates data types

# Supports optional flags (like --verbose)

# Easier to scale for complex CLI tools

# Examples of CLI Tools:
# git – for version control

# python – to run Python scripts

# pip – to install Python packages

# django-admin – to manage Django projects

# ls, cd, mkdir – basic shell commands
