from prac_07.guitar import Guitar

def main():
    my_guitars = []

    guitar_name = input("Name: ")
    while guitar_name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar =  Guitar(guitar_name,year,cost)
        my_guitars.append(new_guitar)
        print(new_guitar,"added")
        guitar_name = input("Name: ")
    #
    # my_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # my_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars")
    guitar_number=0
    for guitar in my_guitars:
        vintage_string = ""
        guitar_number += 1
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(guitar_number,
                    guitar.name, guitar.year, guitar.cost, vintage_string))


main()