import Pyro4


uri = input("Jakie jest Pyro uri? ").strip()

date_receiver = Pyro4.Proxy(uri)	#podlaczenie do servera z uzyciem uri



def main():
    print("Podaj dwie liczby, na których wybrana operacja zostanie wykonana")
    x = int(input())
    y = int(input())
    print("Wybierz operacje, która chcesz wykonac na dwóch liczbach")
    print(" 1- dodawanie\n 2- odejmowanie\n 3- iloczyn\n 4- iloraz")
    z = int(input())
    if z>=1 and z<5:

        if z==1:
            return print("Oto wynik dzialania:",date_receiver.sum(x, y))
        if z==2:
            return print("Oto wynik dzialania:",date_receiver.difference(x, y))
        if z==3:
            return print("Oto wynik dzialania:",date_receiver.product(x, y))
        if z==4:
            return print("Oto wynik dzialania:",date_receiver.quotient(x, y))
    else:
        print("Wybór jest niepoprawny! Spobuj jeszcze raz")
        return False



while True:
    main()
    print("Czy chcesz dokonaæ nastepnej operacji? Prosze wybrac y/n")
    if input() == "y":
        main()
    else:
        print("Dziekujmy za skorzystanie z uslug naszego serwisu :)")
        break

#proba GITHUB







