"""CP1404 practical do it yourself """
from Practicals.Prac_06.guitar import Guitar


def main():
    """Guitar program that uses a class"""
    guitars = []
    print("My guitar collection")
    name = input("Name of guitar: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_details = Guitar(name, year, cost)
        guitars.append(guitar_details)
        print(guitar_details, "added to collection.")
        name = input("Name of guitar: ")

    if guitars:
        print("This is my collection")
        for i, guitar in enumerate(guitars):
            is_vintage = ""
            if guitar.is_vintage():
                is_vintage = "vintage"
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, is_vintage))
    else:
        print("You have no guitars")

main()
