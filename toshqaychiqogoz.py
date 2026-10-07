import random


choices = {
    1: "tosh",
    2: "qaychi",
    3: "qogoz"
}


def get_random_choice():
    return random.randint(1, 3)


def main():
    print("TOSH QAYCHI QOGOZ o'yiniga xush kelibsiz!")
    print("=" * 30)
    while True:
        print("Tanlang:")
        for i, k in choices.items():
            print(f"{i}) {k}")
        user = int(input(">>>"))
        computer = get_random_choice()
        if user == computer:
            print("DURRANG!!!")
            continue

        if (
            (user == 1 and computer == 2) or 
            (user == 2 and computer == 3) or
            (user == 3 and computer == 1)
        ):
            print("Siz galaba qozondingiz!")
            print("Men tanlagan edim", choices[computer])
        else:
            print("Siz yutqazdingiz!!!")
            print("Men tanlagan edim", choices[computer])


main()