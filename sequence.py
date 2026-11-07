# Program wyznaczający sumę n kolejnych liczb nieparzystych.
# Na przykład dla n = 3 program liczy sumę 1 + 3 + 5 i pisze 9.


def lista_liczb_nieparzystych(n):           # n - ile liczb
    return list(range(1, n * 2 , 2))        # [1,3,5...]


def suma_liczb(lista):
    return sum(lista)


def main():
    for i in range(1, 5):
        liczby = lista_liczb_nieparzystych(i)
        print(f"Ciąg liczb nieparzystych {liczby}. Suma liczb {suma_liczb(liczby)}")


# Poniższy kod wykona się TYLKO, gdy uruchomimy sequence.py bezpośrednio (python sequence.py)
if __name__ == "__main__":
    main()

