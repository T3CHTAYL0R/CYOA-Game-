import sys

name = input("Type your name: ")
print("Welcome,", name)

while True:
    response = input("Are you ready for your adventure? (yes/no): ").strip().lower()
    if response == "yes":
        print("Let's Begin")
        break
    elif response == "no":
        print("Maybe next time!")
        sys.exit()

    else:
        print("Please enter 'yes' or 'no'.")
