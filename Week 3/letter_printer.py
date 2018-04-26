def main():
    name = get_name()
    letter_frequency = int(input("What frequency of letters? "))
    frequency_of_letters(name,letter_frequency)
    print(frequency_of_letters(name,letter_frequency))


def frequency_of_letters(name,letter_frequency):
    name_no_space = name.replace(" ", "")
    letter_picker = name_no_space[0:len(name_no_space):letter_frequency]
    return letter_picker


def get_name():
    name = input('What is your name? ')
    while len(name) == 0:
        print("error,blank")
        name = input('What is your name? ')
    return name


main()
