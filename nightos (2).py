import os
import time

# A simple function to simulate a shell command execution
def execute_command(command):
    if command == "help":
        print("""
Available commands:
    help        - Show this help message
    list        - List files in the current directory
    time        - Show the current system time
    create FILE - Create a new empty file
    delete FILE - Delete a specified file
    exit        - Exit the OS simulation
        """)
    elif command == "list":
        print("\n".join(os.listdir(".")))
    elif command.startswith("create "):
        filename = command.split(" ", 1)[1]
        with open(filename, "w") as f:
            pass
        print(f"File '{filename}' created.")
    elif command.startswith("delete "):
        filename = command.split(" ", 1)[1]
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File '{filename}' deleted.")
        else:
            print(f"File '{filename}' does not exist.")
    elif command == "time":
        print(f"Current time: {time.ctime()}")
    elif command == "exit":
        print("Thank you for using NightOS. Goodbye!")
        return False
    else:
        print(f"Unknown command: {command}")
    return True

# Main loop for the OS
def run_os():
    print("Welcome to NightOS")
    print("Type help for more options.")
    while True:
        command = input(">> ")
        if not execute_command(command):
            break

# Start the simulated OS
if __name__ == "__main__":
    run_os()
import os
import time

# A simple function to simulate a shell command execution
def execute_command(command):
    if command == "help":
        print("""
Available commands:
    help        - Show this help message
    list        - List files in the current directory
    time        - Show the current system time
    create FILE - Create a new empty file
    delete FILE - Delete a specified file
    exit        - Exit the OS simulation
        """)
    elif command == "list":
        print("\n".join(os.listdir(".")))
    elif command.startswith("create "):
        filename = command.split(" ", 1)[1]
        with open(filename, "w") as f:
            pass
        print(f"File '{filename}' created.")
    elif command.startswith("delete "):
        filename = command.split(" ", 1)[1]
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File '{filename}' deleted.")
        else:
            print(f"File '{filename}' does not exist.")
    elif command == "time":
        print(f"Current time: {time.ctime()}")
    elif command == "exit":
        print("Thank you for using NightOS. Goodbye!")
        return False
    else:
        print(f"Unknown command: {command}")
    return True

# Main loop for the OS
def run_os():
    print("Welcome to NightOS")
    print("Type help for more options.")
    while True:
        command = input(">> ")
        if not execute_command(command):
            break

# Start the simulated OS
if __name__ == "__main__":
    run_os()
import os
import time

# A simple function to simulate a shell command execution
def execute_command(command):
    if command == "help":
        print("""
Available commands:
    help        - Show this help message
    list        - List files in the current directory
    time        - Show the current system time
    create FILE - Create a new empty file
    delete FILE - Delete a specified file
    exit        - Exit the OS simulation
        """)
    elif command == "list":
        print("\n".join(os.listdir(".")))
    elif command.startswith("create "):
        filename = command.split(" ", 1)[1]
        with open(filename, "w") as f:
            pass
        print(f"File '{filename}' created.")
    elif command.startswith("delete "):
        filename = command.split(" ", 1)[1]
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File '{filename}' deleted.")
        else:
            print(f"File '{filename}' does not exist.")
    elif command == "time":
        print(f"Current time: {time.ctime()}")
    elif command == "exit":
        print("Thank you for using NightOS. Goodbye!")
        return False
    else:
        print(f"Unknown command: {command}")
    return True

# Main loop for the OS
def run_os():
    print("Welcome to NightOS")
    print("Type help for more options.")
    while True:
        command = input(">> ")
        if not execute_command(command):
            break

# Start the simulated OS
if __name__ == "__main__":
    run_os()
vvimport os
import time

# A simple function to simulate a shell command execution
def execute_command(command):
    if command == "help":
        print("""
Available commands:
    help        - Show this help message
    list        - List files in the current directory
    time        - Show the current system time
    create FILE - Create a new empty file
    delete FILE - Delete a specified file
    exit        - Exit the OS simulation
        """)
    elif command == "list":
        print("\n".join(os.listdir(".")))
    elif command.startswith("create "):
        filename = command.split(" ", 1)[1]
        with open(filename, "w") as f:
            pass
        print(f"File '{filename}' created.")
    elif command.startswith("delete "):
        filename = command.split(" ", 1)[1]
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File '{filename}' deleted.")
        else:
            print(f"File '{filename}' does not exist.")
    elif command == "time":
        print(f"Current time: {time.ctime()}")
    elif command == "exit":
        print("Thank you for using NightOS. Goodbye!")
        return False
    else:
        print(f"Unknown command: {command}")
    return True

# Main loop for the OS
def run_os():
    print("Welcome to NightOS")
    print("Type help for more options.")
    while True:
        command = input(">> ")
        if not execute_command(command):
            break

# Start the simulated OS
if __name__ == "__main__":
    run_os()



