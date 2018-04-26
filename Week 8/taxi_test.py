from prac_08.taxi import Taxi

def main():
    prius = Taxi("Prius 1", 100 )
    prius.drive(40)
    print(prius)
    print("Fair cost's ${:.2f}".format(prius.get_fare()))
    prius.start_fare()
    prius.drive(100)
    print(prius)
    print("Fair cost's ${:.2f}".format(prius.get_fare()))
main()