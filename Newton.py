import math
liczby = input()
cyfry = liczby.split()
n=0
liczba1 = int(cyfry[0])
liczba2 = int(cyfry[1])
liczba3 = int(cyfry[0]) - int(cyfry[1])
liczba1=math.factorial(liczba1)
liczba2=math.factorial(liczba2)
liczba3=math.factorial(liczba3)
wynik = liczba1/(liczba2*liczba3)
print(round(wynik))