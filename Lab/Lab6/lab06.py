import sys

def print_args(args):
    for arg in args:
        print(arg)

def is_valid_flag(flag):
    return flag in ["-p", "-i", "-h", "-w", "-r"]

def flags(args):
    flag = args[1]
    if flag == "-p":
        # Print all arguments after "-p"
        print_args(args[2:])
    elif flag == "-i":
        # Print "Hello World"
        print("Hello World")
    elif flag == "-h":
        # Print help information
        print("Valid flags:")
        print("-p : prints out all the command line arguments after the -p")
        print("-i : prints \"Hello World\"")
        print("-h : prints out a help command")
    elif flag == "-w":
        if len(args) < 4:
            print("No Content Provided")
        else:
            write_to_file(args[2], args[3:])
    elif flag == "-r":
        read_from_file(args[2])

def write_to_file(filename, content):
    with open(filename, "w") as file:
        for line in content:
            file.write(line + "\n")

def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and is_valid_flag(sys.argv[1]):
        flags(sys.argv)
    else:
        print_args(sys.argv)