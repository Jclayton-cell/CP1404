MIN_LENGTH = 2
MAX_LENGTH = 6


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,"letters.")
    password = get_password()
    print("Your " + str(len(password)) + " character password is valid: " + password)
    asterisk_count(password)


def get_password():
    password = input("> ")
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        print("Invalid password!")
        password = input("> ")
    return password


def asterisk_count(password):
    print(len(password) * "*")








main()
