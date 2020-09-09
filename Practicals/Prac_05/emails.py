def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirm = input("Is your name {}? (Y/n) ".format(name))
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email (Enter blank when finished): ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name(email):
    separation = email.split('@')[0]
    parts = separation.split('.')
    name = " ".join(parts).title()
    return name

main()