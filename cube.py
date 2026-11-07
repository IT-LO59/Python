# Program szacujący prawdopodobieństwo rzutu kostką,
# w którym liczba oczek należy do ciągu Fibonacciego
import random


def isDiceFibonacci(x):
    return x in [1, 2, 3, 5]


def probability(n):
    NUMBER_OF_SIDES = 6
    count = 0
    for _ in range(n):
        count += isDiceFibonacci(random.randint(1, NUMBER_OF_SIDES))
    return count / n


def main():
    for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
        print(f"Szacowane prawdopodobieństwo ma podstawie {n} losowań = {probability(n)}")


# Poniższy kod wykona się TYLKO, gdy uruchomimy cube.py bezpośrednio (python cube.py)
if __name__ == "__main__":
    main()
