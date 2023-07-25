import numpy.ma
import pandas as pd
import numpy as np
print(pd.__version__)

#TODO 3.C. Analiza wzrostu prezydentów
# Wczytaj plik zawierający wzrost prezydentów USA president_heights.csv i wylicz:
# Średni wzrost,
# Minimalny wzrost,
# Maksymalny wzrost,
# 25ty centyl,
# Medianę,
# 75ty centyl

import pandas as pd
data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)
#wynik
# [189 170 189 163 183 171 185 168 173 183 173 173 175 178 183 193 178 173
#  174 183 183 168 170 178 182 180 183 178 182 188 175 179 183 193 182 183
#  177 185 188 188 182 185 191 182]
print("Srednia ", heights.mean())
#wynik Srednia  180.04545454545453
print('Minimum: ',heights.min())
#wynik Minimum:  163
print('Maksimum:',heights.max())
#wynik Maksimum: 193
print('25%: ',np.quantile(heights,0.25))
#wynik 25%:  174.75
print('Mediana: ',np.quantile(heights,0.5))
#wynik Mediana:  182.0
print('75%: ',np.quantile(heights,0.75))
#wynik 75%:  183.5

#TODO 4. Szachownica
# Utwórz tablicę Numpy, która będzie wyrażała planszę szachową (8x8).
# HINT: białe pola oznacz jako 1, czarne jako 0

a = np.zeros((8,8))
print(a)
#wynik
# [[0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]]

a[0::2,0::2] = 1 #ustawienie 1 zaczynając od 0 wiersza z krokiem co 2
print(a)
#wynik
# [[1. 0. 1. 0. 1. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [1. 0. 1. 0. 1. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [1. 0. 1. 0. 1. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [1. 0. 1. 0. 1. 0. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]]

a[1::2,1::2] = 1 #ustawienie 1 co drugą pozycje rozpoczynając od 2 wiesza (1) z krokiem co 2
print(a)
#wynik
#
# [[1. 0. 1. 0. 1. 0. 1. 0.]
#  [0. 1. 0. 1. 0. 1. 0. 1.]
#  [1. 0. 1. 0. 1. 0. 1. 0.]
#  [0. 1. 0. 1. 0. 1. 0. 1.]
#  [1. 0. 1. 0. 1. 0. 1. 0.]
#  [0. 1. 0. 1. 0. 1. 0. 1.]
#  [1. 0. 1. 0. 1. 0. 1. 0.]
#  [0. 1. 0. 1. 0. 1. 0. 1.]]

import matplotlib.pyplot as plt

# plt.imshow(a, cmap='gray', interpolation='nearest')
# plt.show()
# wydrukowanie wizualizacji tablicy

#TODO 5. Indeksy i maski 5.A. Znajdź indeksy niezerowych elementów w tablicy: [1,2,0,0,4,0]

a =np.array([1,2,0,0,4,0])
print(np.where(a!=0))
#wynik array([0, 1, 4]),)

#TODO 5.B. Wygeneruj tablicę o wymiarach 5x5, zawierającą losowe liczby z przedziału 120-200. Nałóż maskę, która wyselekcjonuje wartości powyżej 180.

a = np.random.randint(120,200,25).reshape((5,5))
print(a)
#wynik
# [[186 141 121 143 197]
#  [123 148 165 174 147]
#  [123 130 143 162 126]
#  [169 181 188 154 144]
#  [129 127 122 153 193]]

treshhold = 180
# b[] #możemy w nawiasie wpisać wszystkie warunki które nas interesują

print(a[a>treshhold])
#wynik
# [186 197 181 188 193]

#TODO 6. Analiza opadu deszczu w Seattle¶
# Wczytaj plik Seattle2014.csv i przeprowadź analizę opadów deszczu.
# Wczytaj dane korzystając z biblioteki pandas i zamień jednostki na cale, korzystając z kodu poniżej:
# import pandas as pd
# rainfall = pd.read_csv('data/Seattle2014.csv')['PRCP'].values
# inches = rainfall / 254.0  # 1/10mm -> inches
# inches.shape
# Możemy zwizualizować dane za pomoca biblioteki matplotlib:
# import matplotlib.pyplot as plt
# plt.hist(inches, 40);

import pandas as pd
rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
inches = rainfall / 254.0  # 1/10mm -> inches
inches.shape
print(inches.shape)
print(rainfall)
# import matplotlib.pyplot as plt
# plt.hist(inches, 40) #wszystkie dane podzieli na 40 koszyków do których przydziela dane z tablicy
# plt.show()
# print(plt.hist(inches, 40))

#TODO Korzystając z zaimportowanych danych podaj LICZBĘ DNI kiedy:
# nie padało
# padało
# spadło powyżej 0.5 cala deszczu
# spadło poniżej 0.2 cala deszczu, ale padało!

print(f'Dni w których nie padało {len(inches[inches==0])}')
#wynik Dni w których nie padało 215
print(f'Dni w których padało {len(inches[inches!=0])}')
#wynik Dni w których padało 150
print(f'Dni w których spadło powyzej 0.5 cala deszczu {len(inches[inches>0.5])}')
#wynik Dni w których spadło powyzej 0.5 cala deszczu 37

print(f'Dni kiedy padało poniżej o.2 cala deszczu: {len(inches[(inches<0.2)&(inches>0)])}')

#wynik Dni kiedy padało poniżej o.2 cala deszczu: 75
#
# #alternatywa ostatniego elementu
rain = inches[inches>0]
print(len(rain[rain<0.2]))
#wynik 75

#TODO Korzystając z maskowania policz następujące statystyki:
# Medianę opadów w deszczowe dni w 2014 roku
# Medianę opadów latem w 2014 roku (czyli dni pomiędzy dniem 172 a 262)
# Maksymalne opady latem 2014 roku
# Mediana opadów poza latem 2014 roku (czyli wiosna, jesień i zima)

print(f'Medianę opadów w deszczowe dni w 2014 roku {round(np.median(rain),2)}')
#wynik Medianę opadów w deszczowe dni w 2014 roku 0.19
lato = inches[172:262]
print(f'Medianę opadów latem w 2014 roku (czyli dni pomiędzy dniem 172 a 262) {np.median(lato)}')
#wynik Medianę opadów latem w 2014 roku (czyli dni pomiędzy dniem 172 a 262) 0.0

print(f'Maksymalne opady latem 2014 roku {lato.max()}')
#wynik Maksymalne opady latem 2014 roku 0.8503937007874016

poza_latem = np.delete(inches,slice(172,263))
# print(poza_latem)
print(f'Medianę opadów poza latem 2014 roku {round(np.median(poza_latem),10)}')
#wynik
# Medianę opadów poza latem 2014 roku 0.0
rain_pozalatem = poza_latem[poza_latem>0]
print(f'Medianę opadów poza latem 2014 roku w dni deszczowe {round(np.median(rain_pozalatem),2)}')
#wynik
#Medianę opadów poza latem 2014 roku w dni deszczowe 0.2

#TODO Mając dwa wektory:
# A = [0,3,2,5]
# B = [0,3,1,4]
# Dodaj A i B
# Odejmij B od A
# Pomnóż wektor A przez skalar a =4
# Oblicz iloczyn skalarny wektorów A i B
# Znajdź długość wektora B

A = [0,3,2,5]
B = [0,3,1,4]

arr_a = np.array(A)
arr_b = np.array(B)
print(arr_a)
print(arr_b)
print(arr_a + arr_b)
print(arr_a - arr_b)
print(arr_a * 4) #Pomnóż wektor A przez skalar a =4
print(arr_a * arr_b.transpose())
print(np.dot(arr_a,arr_b)) # iloczyn skalarny
print(arr_b.size) #długość wektora b
