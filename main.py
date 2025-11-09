from random import choice


def print_welcome_message():
    print("===========================================================")
    print('Welcome to the Python Student Management System Menu')
    print("===========================================================\n")

if __name__ == '__main__':
    print_welcome_message()

while True:
    print("1. Add new student")
    print("2. Edit")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == 1:
        print("1. Add new student")
    elif choice == 2:
        print("2. Edit Details")
    elif choice == 3:
        print("3. Exit")
    else:
        print(" Option:\n")
        exit()






