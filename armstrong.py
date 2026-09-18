def is_armstrong_number(number):
    table = [int(numer) for numer in str(number)]
    potega = len(table)

    suma = 0
    for x in table:
        suma += x ** potega

    return suma == number