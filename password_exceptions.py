#FileNotFound Exception

try:
    with open("a_file.txt") as file:
        file.read()
except FileNotFoundError:
    with open("a_file.txt", "w") as file_2:
        file_2.write("Hello World")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    with open("a_file.txt") as file_3:
        print(file_3.read())
finally:
    print(f"{file_3.name} has been created")
    # Using raise keyword
    #raise KeyError("You typed the wrong key")