from prac_08.silver_taxi_service import SilverTaxiService
from prac_08.taxi import Taxi

def main():
    MENU = "C: Choose Taxi \nD: Drive \nQ: Quit"
    taxis = [Taxi("Prius", 100), SilverTaxiService("Limo", 100, 2),
             SilverTaxiService("Hummer", 200, 4)]

    fare = 0
    print(MENU)
    user_choice = input(">>>").upper()
    while user_choice != "Q":
        if user_choice == "C":
            taxi_number = 0
            print("Taxi's Avalaiable")
            for taxi in taxis:
                print("{} - {}".format(taxi_number, taxi))
                taxi_number += 1
            taxi_choice = int(input("Choose Taxi:"))
            print("Bill to date ${:.2f}".format(fare))

        elif user_choice == "D":
            distance = int(input("Drive how far? "))
            taxis[taxi_choice].drive(distance)
            fare += taxis[taxi_choice].get_fare()
            print("your taxi will cost you ${:.2f}".format(fare))
        print(MENU)
        user_choice = input(">>>").upper()

    print("Total trip costs ${:.2f}".format(fare))
    print("Taxi's are now:")
    for taxi in taxis:
        taxi_number = 0
        print("{} - {}".format(taxi_number, taxi))
        taxi_number += 1

        # elif user_choice == "D":
main()