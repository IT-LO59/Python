# Funkcja, która kompresuje tekst metodą rls bazującą
# na zliczaniu powtarzających się znaków (jeden znak może powtarzać się maksymalnie 9 razy).
# Na przykład wynikiem dla łańcucha aaabbcaa będzie a3b2c1a2.


def rle(text):      # text - tekst przed zakodowaniem
    MAX_COUNT = 9
    sign = text[0]
    cnt = 0
    code = ""       # code - zakodowany ciąg wyjściowy
    for i in range(0, len(text)):
        if (text[i] == sign) and cnt < MAX_COUNT:
            cnt += 1
        else:
            code += sign + str(cnt)
            sign = text[i]
            cnt = 1
    code += sign + str(cnt)
    return code


def main():
    text = "aaaaaaaaaabbcaa"
    print(f"Ciąg wejściowy: {text}, Ciąg zakodowany: {rle(text)}")


# Poniższy kod wykona się TYLKO, gdy uruchomimy run_length_encoding.py bezpośrednio (python run_length_encoding.py)
if __name__ == "__main__":
    main()
