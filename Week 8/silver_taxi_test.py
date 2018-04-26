from prac_08.silver_taxi_service import SilverTaxiService

def main():

    hummer = SilverTaxiService("Hummer", 200, 2)
    hummer.drive(18)
    print(hummer)
    print("${:.2f}".format(hummer.get_fare()))


main()
