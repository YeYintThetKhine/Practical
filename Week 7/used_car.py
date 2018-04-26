"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_07.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car",180)
    my_car.drive(115)
    my_car.add_fuel(20)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    # print("Car {}, {}".format(my_car.fuel, my_car.odometer))


    limo = Car("Limo",100)
    limo.drive(30)
    print("fuel =", limo.fuel)
    print("odo =", limo.odometer)
    print(limo)
    # print ("Limo {}, {}".format(limo.fuel, limo.odometer))




main()