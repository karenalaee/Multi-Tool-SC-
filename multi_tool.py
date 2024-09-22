import os
import sys
import time
import subprocess

print(" ▄▀▀▄ ▄▀▄  ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄     ▄▀▀▀█▀▀▄  ▄▀▀█▀▄        ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄     ")
print("█  █ ▀  █ █   █    █ █    █     █    █  ▐ █   █  █      █    █  ▐ █      █ █      █ █    █      ")
print("▐  █    █ ▐  █    █  ▐    █     ▐   █     ▐   █  ▐      ▐   █     █      █ █      █ ▐    █      ")
print("  █    █    █    █       █         █          █            █      ▀▄    ▄▀ ▀▄    ▄▀     █       ")
print("▄▀   ▄▀      ▀▄▄▄▄▀    ▄▀▄▄▄▄▄▄▀ ▄▀        ▄▀▀▀▀▀▄       ▄▀         ▀▀▀▀     ▀▀▀▀     ▄▀▄▄▄▄▄▄▀ ")
print("█    █                 █        █         █       █     █                             █         ")
print("▐    ▐                 ▐        ▐         ▐       ▐     ▐                             ▐         ")
print("")
print("                                  writen by Single Core")
def main_menu():
    print("Welcome to the Multi-Tool Program!")
    print("Please select an option:")
    print("1. Calculator")
    print("2. File Manager")
    print("3. System Info")
    print("4. Hacking Tools")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    return choice

def calculator():
    print("Welcome to the Calculator Module!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        result = num1 + num2
        print("Result:", result)
    elif choice == '2':
        result = num1 - num2
        print("Result:", result)
    elif choice == '3':
        result = num1 * num2
        print("Result:", result)
    elif choice == '4':
        result = num1 / num2
        print("Result:", result)
    else:
        print("Invalid choice. Please try again.")

def file_manager():
    print("Welcome to the File Manager Module!")
    print("Please select an option:")
    print("1. Create a new file")
    print("2. Read a file")
    print("3. Write to a file")
    print("4. Delete a file")

    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        filename = input("Enter the filename: ")
        with open(filename, 'w') as file:
            pass
        print("File created successfully.")
    elif choice == '2':
        filename = input("Enter the filename: ")
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("File Content:")
                print(content)
        except FileNotFoundError:
            print("File not found. Please try again.")
    elif choice == '3':
        filename = input("Enter the filename: ")
        content = input("Enter the content to write: ")
        with open(filename, 'w') as file:
            file.write(content)
        print("Content written to the file successfully.")
    elif choice == '4':
        filename = input("Enter the filename: ")
        try:
            os.remove(filename)
            print("File deleted successfully.")
        except FileNotFoundError:
            print("File not found. Please try again.")
    else:
        print("Invalid choice. Please try again.")

def system_info():
    print("Welcome to the System Info Module!")
    print("System Information:")
    print("Operating System:", os.name)
    print("Python Version:", sys.version)
    print("Current Working Directory:", os.getcwd())
    print("Time:", time.ctime())

def hacking_tools():
    print("Welcome to the Hacking Tools Module!")
    print("Please select an option:")
    print("1. Port Scanner")
    print("2. Network Scanner")
    print("3. Password Cracker")
    print("4. Back to Main Menu")

    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        target = input("Enter the target IP or domain: ")
        ports = input("Enter the ports to scan (e.g., 22,80,443): ")
        command = f"nmap -p {ports} {target}"
        subprocess.run(command, shell=True)
    elif choice == '2':
        target = input("Enter the target IP or domain: ")
        command = f"nmap -sP {target}"
        subprocess.run(command, shell=True)
    elif choice == '3':
        password_file = input("Enter the password file path: ")
        command = f"john --wordlist={password_file} --format=raw-md5"
        subprocess.run(command, shell=True)
    elif choice == '4':
        main_menu()
    else:
        print("Invalid choice. Please try again.")

def exit_program():
    print("Exiting the program...")
    time.sleep(1)
    sys.exit()

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            calculator()
        elif choice == '2':
            file_manager()
        elif choice == '3':
            system_info()
        elif choice == '4':
            hacking_tools()
        elif choice == '5':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
