import numpy as np
print(np.__version__)

l = [1, "2", True, 3.0, None] #wszystkie możliwe typy danych w liście - zadziała to
z = [type(item) for item in l]
print(z) # pokazujemy liste typów danych z tej listy
#Dla namPy trzeba narzucić jaki typ danych jest dla całej tablicy

#TODO tablica liczb całkowitych
np.array([1, 2, 3, 4, 5])
print(np.array([1, 2, 3, 4, 5]))

#TODO tablica liczb zmiennoprzecinkowych
np.array([4.1, 0, 1, 2, 3]) #nampy szuka wspólnego mianownika wiec zamieni typy danych i zapisze wszystko we floatach
print(np.array([4.1, 0, 1, 2, 3]))

print(np.array([range(i, i + 3) for i in [2, 4, 6]])) #tworzy tablice dwuwymiarową

#wynik [[2 3 4]
 # [4 5 6]
 # [6 7 8]]

#TODO sposoby tworzenia tablic w NumPy

# TODO 10 elementowa tablica wypełniona zerami

np.zeros(10, dtype=int) #pierwszy element pokazujemy ile ma być elementów w tablicy jesli damy x to jedzie jeden wymiar x miejsc; jeśli damy 4,3 to bedzie dwuwymiarowa tablica 4 w pierszym wymiarze i 3 w drugim wymairze

print(np.zeros(10, dtype=int))
#wynik
# [0 0 0 0 0 0 0 0 0 0]

#TODO Tablica o wymiarach 5x3, wypełniona 1. liczba wierszy * liczba kolumn !!!!slice, poziome, pionowe!!!!

np.ones((5, 3), dtype=float)
print(np.ones((5, 3), dtype=float))

#wynik
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

#TODO Tablica wypełniona ciągiem liniowym z krokiem 2 arange to krok który definiujemy w ostatniej kolumnie
np.arange(0, 20, 2)
print(np.arange(0, 20, 2))

#wynik
# [ 0  2  4  6  8 10 12 14 16 18]

#TODO  Tablica o wymiarach 3x3 z wartościami wylosowanymi z rozkładu N(0, 1)

np.random.normal(0, 1, (3, 3))

print(np.random.normal(0, 1, (3, 3)))
#wynik losowe wartości
# [[-0.34560214  0.07419746 -0.46350818]
#  [-0.4086412  -0.41546458  0.15908356]
#  [-0.48352511 -0.53570918  0.78407563]]

# Tablica o wymiarach 4x5 z liczbami całkowitymi wylosowanymi z przedziału [0, 10)
np.random.randint(0, 10, (4, 5))
print(np.random.randint(0, 10, (4, 5)))

#wynik
# [[4 9 3 1 4]
#  [7 8 6 2 0]
#  [4 9 2 4 6]
#  [8 3 1 4 7]]

#TODO typy danych w NumPy
# https://numpy.org/doc/stable/user/basics.types.html

# Trzy wymiarowa tablica o wymiarach 2x3x4
# z losowymi liczbami całkowitymi z przedziału [0, 100)
#pierwsza liczba to ilość pięter (z), druga to kolumny (y), trzecia to wiersze (x)
x = np.random.randint(100, size=(2, 3, 4))
print(x)

#wynik
# [[[ 2 87 55 99]
#   [51 41 80 48]
#   [50 16 51  7]]
#
#  [[45 30 28 21]
#   [66 79 84 78]
#   [ 0 93  7 62]]]

print(f"x ndim: {x.ndim}")  # liczba wymiarów ilość liczba wymiarów
print(f"x shape: {x.shape}")  # wymiary tablicy (z, y, z)
print(f"x size: {x.size}")  # całkowity rozmiar tablicy łączna liczba elementów w tablicy
#wynik
# x ndim: 3
# x shape: (2, 3, 4)
# x size: 24

print(f"x dtype: {x.dtype}")  # typ danych przechowywanych w tablicy
#wynik
# x dtype: int64

print(f"itemsize: {x.itemsize} bytes")  # rozmiar jednego elementu
#wynik
# itemsize: 8 bytes

print(f"nbytes: {x.nbytes} bytes")  # rozmiar całej tablicy (itemsize x size)
#wynik
# nbytes: 192 bytes

#TODO indeksowanie tablic jednowymiarowych
y = np.arange(0, 10)
print(y)
#wynik
# [0 1 2 3 4 5 6 7 8 9]
print(y[5]) #wyciągamy 5 alement z tablicy
#wynik
# 5
y[-1]
print(y[-1])
#wynik
# 9

#TODO indeksowanie tablic wielowymiarowych
print(x)
# #wynik
# [[[15 12 75 32]
#   [39 48 54 87]
#   [30 44 21 59]]
#
#  [[68 80 87 18]
#   [50 90 23 88]
#   [10 49  9 88]]]
print(x[0,1,2]) #odczytanie elementu o współrzędnych
#wynik 54
x[0,1,2]=42 #podmieniliśmy wartość w tablicy o danych współrzadnych
print(x)
#wynik
# [[[71 45 64 64]
#   [28 60 42 63]
#   [58 18 95 15]]
#
#  [[79 81 89 58]
#   [65 59 96 70]
#   [67 90 14 81]]]

print(y[:5]) #wycinanie pierwszych 5 elementów
#wynik [0 1 2 3 4]

print(y[4:7:2])  # wycinek ze środka tablicy od 4 do 7 otwarte co 2 czyli 4 i 6
#wynik [4 6]

print(y[::-1])  # tablica odczytana od tyłu
#wynik [9 8 7 6 5 4 3 2 1 0]

#TODO wycinanie slice kawałki wielowymiarowe
print(x)
# wynik
# [[89 12 96 75]
#  [32 93 38 85]
# [54 81 65 76]]]

print(x[:1, :, :3]) # dwukropek bez argumentów oznacza wybranie wszystkich elementów z danego wymiaryu!
#wynik
# [[[ 7 10 55]
#   [ 8 50 42]
#   [53 72 49]]]

#TODO podczas wycinania fragmentu listy tworzymy widok - nie tworzy kopi tylko inny widok tej samej tablicy danych

l1 = [1, 2, 3] #lista 1 2 3
l2 = l1[2:] #tworzymy fragment listy od drugiego elementu do końca  (czyli 2)
l2[0] = 4 # modyfikujemy sobie l2 z dwa na 4
print(l1)  # l1 pozostaje nie zmienione!
print(l2)  # l1 pozostaje nie zmienione!
#wynik
# [1, 2, 3]
# [4]

# NumPy
x = np.zeros((2, 3))
y = x[ 0, :] #tworzymy widok z tablicy x i przypisujemy go do y
y[0] = 1 #w wymiarze zerowym pierwszy element
print(x)  # x i y reprezentują tą samą tablicę!
print(y)  # x i y reprezentują tą samą tablicę!
#wynik
# [[1. 0. 0.]
#  [0. 0. 0.]]
# [1. 0. 0.]

#
# inny przykład
# x = np.array([1, 2, 2])
# print(x)
# y = x[:2]
# print(y)
# y[0] = 5
# print(x)
# print(y)

#TODO metoda copy - tylko w tym przypadku tworzymy kopie danych i mamy dwie odrębne tablice arrey
print(x)
x_copy = x[:2, :2].copy()
x_copy[0, 0] = 42

print(x)
print(x_copy)  # zmiana x_copy nie zmieniła x
#wynik
# [[1. 0. 0.]
#  [0. 0. 0.]]
# [[42.  0.]
#  [ 0.  0.]]

#TODO zmiana wymiarów tablicy - komenda RESHAPE pozwala inaczej ułozyć dane w tablicy

np.arange(1,10)
print(np.arange(1,10))
#wynik [1 2 3 4 5 6 7 8 9]
np.arange(1, 10).reshape((3, 3))
print(np.arange(1, 10).reshape((3, 3)))
#wynik
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

#TODO RESHAPE tylko można zrobić dla dokładnie takich samcyh wartości - trzeba wykorzystać wszystkie liczmy
x = np.array([1,2,3]) #trzy wartości
print(x)
print(x.reshape((1, 3))) # dwuwymiarowa tablica z jednym wierszem i trzema kolumnami
#wynik [[1 2 3]] tablica dwówymiarowa
print(x.reshape((3, 1))) # dwuwymiarowa tablica z trzema wierszami i jedną kolumną
#wynik
# [[1]
# [2]
# [3]]

#TODO Łączenie tablic plus w przypadku list oznacza konkatenacje - działania na macieżach
# np.concatenate podajemy liste array w nawiasach kwadrawotych
# np.vstack
# np.hstack


x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(np.concatenate([x, y]))
#wynik
# [1 2 3 3 2 1]

grid = np.array([[1, 2, 3],
                 [4, 5, 6]])

print(np.concatenate([grid, grid]))
#wynik [[1 2 3]
 # [4 5 6]
 # [1 2 3]
 # [4 5 6]]
print(np.concatenate([grid, grid], axis=1))  # łączenie wzdłuż drugiego wymiaru axis=0; byłoby ten sam wymiar
#wynik [[1 2 3 1 2 3]
# [4 5 6 4 5 6]]

#TODO vstack i hstack

# V - vertical (góra dół)
# h - horisontal (prawo lewo)

x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

print(np.vstack([x, grid])) #dokleił poniżej wartości drugiego i trzeciego wiersza
#wynik
# [[1 2 3]
#  [9 8 7]
#  [6 5 4]]

y = np.array([[99],
              [99]])

print(np.hstack([grid, y])) #dokleił po prawej stronie wartości
#wynik
# [[ 9  8  7 99]
#  [ 6  5  4 99]]

#TODO Split
x = np.arange(10)
print(x)
#wynik [0 1 2 3 4 5 6 7 8 9]
x1, x2, x3 = np.split(x, [3, 5]) #krotka poszczególnych wtciętych rzeczy podajemy tablicę "x" następnie listę miejsc gdzie ucinamy ładujemy ją do trzech wartości x1 x2 x3
print(x1, x2, x3)  # zauważ, że dwa punkty dzielenia tworzą trzy tablice
#wynik
# [0 1 2] [3 4] [5 6 7 8 9]

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i, value in enumerate(values):
        output[i] = 1.0 / value
    return output
values = np.random.randint(1, 10, size=5)

print(values)
#wynik [7 9 5 9 9]
compute_reciprocals(values)
big_array = np.random.randint(1, 100, size=1_000_000)
print(big_array)
#wynik
# [18 65 96 ... 17 70 31]
# %timeit compute_reciprocals(big_array) #działa tylko na jupitera
# %timeit 1.0 / big_array  # ta sama operacja wykonana w sposób wektorowy


x = np.arange(4)

#TODO dziąłania na macierzach są takie same jak na zwykłych liczbach
print("x      =", x)
#wynik
# x      = [0 1 2 3]
print("x + 5  =", x + 5)
#wynik
# x + 5  = [5 6 7 8]
print("x - 5  =", x - 5)
#wynik
# x - 5  = [-5 -4 -3 -2]
print("x * 2  =", x * 2)
#wynik
# x * 2  = [0 2 4 6]
print("x / 2  =", x / 2)
#wynik
# x / 2  = [0.  0.5 1.  1.5]
print("x // 2 =", x // 2)
#wynik
# x // 2 = [0 0 1 1]
print("-x     =", -x)
#wynik -x     = [ 0 -1 -2 -3]
print("x ** 2 =", x ** 2)
#wynik x ** 2 = [0 1 4 9]
print("x % 2  =", x % 2)
#wynik x % 2  = [0 1 0 1]

#TODO Agregacje na tablicach
L = np.random.random(100)
print(L)
#wynik
# [0.99196518 0.62950748 0.69812956 0.51319699 0.87686375 0.87421792
#  0.52255025 0.65928788 0.66886609 0.8414968  0.49496844 0.67593078
#  0.55062421 0.42721576 0.78763369 0.34693205 0.42025762 0.48916816
#  0.58171753 0.99743156 0.61144007 0.31230449 0.37460684 0.57530255
#  0.50716231 0.690619   0.4652012  0.34170588 0.56852411 0.30759451
#  0.02953639 0.67997046 0.33858001 0.71014826 0.25991922 0.93907776
#  0.72160721 0.15009969 0.85950573 0.53342023 0.75882392 0.78578255
#  0.79666477 0.65211083 0.59676162 0.6897461  0.62922684 0.85057039
#  0.61945547 0.74603002 0.14793659 0.51318554 0.04445219 0.68523058
#  0.84924474 0.41917316 0.55619813 0.22744637 0.5866589  0.79658169
#  0.36087825 0.27606333 0.41200682 0.44284541 0.38780137 0.26185644
#  0.40251391 0.3691013  0.74071457 0.57740964 0.64544508 0.2935054
#  0.57877993 0.0129236  0.70702066 0.6507079  0.35645103 0.5801018
#  0.80585863 0.02054099 0.03312922 0.2663062  0.08157697 0.99662905
#  0.64672237 0.0217613  0.36877784 0.17889184 0.04191506 0.40866022
#  0.62561761 0.68576146 0.12051073 0.70639823 0.00963718 0.2363796
#  0.02135346 0.48987812 0.33781108 0.68178807]
print(np.sum(L), np.min(L), np.max(L))
#wynik
# 50.81759964580499 0.009637179507803184 0.9974315568412309

# %timeit np.sum(L)
# %timeit sum(L)
# korzystanie z funkcji NumPy jest 3x szybsze niż z puthona

M = np.random.randint(10, size=(3, 4))
print(M)
#wynik
# [[9 0 5 3]
#  [2 4 0 8]
#  [6 4 6 0]]
print(M.sum(axis=0))
#wynik [17  8 11 11] suma kolumn
print(M.sum(axis=1))
#wynik [17 14 16] suma wierszy
print(M.min(axis=0))
#wynik [2 0 0 0] min w kolumnach
print(M.min(axis=1))
#wynik [0 0 0] min w wierszach

#TODO PORÓWNYWANIE, MASKI porównywanie jest na wartościach boolinowych

x = np.array([1, 2, 3, 4, 5])
x<3
print(x<3)
#wynik [ True  True False False False]
print(x>3)
#wynik [False False False  True  True]
print(x==3)
#wynik [False False  True False False] bo powyżej są przedziały otwarte wiec tylko tak zobaczymy czy coś zawiera 3 - jest to wpisywane do kolejnej macierzy

x = np.random.randint(10, size=(4, 4))
print(x)
# #wynik
# [[5 3 9 8]
#  [1 4 0 9]
#  [2 8 8 4]
#  [4 6 6 3]]
print(x<6)
#wynik
# [[ True  True False False]
#  [ True  True  True False]
#  [ True False False  True]
#  [ True False False  True]]
# Ile wartości w tablicy jest mniejszych niż 6?
print(np.count_nonzero(x<6)) #w pythonie false oznacza 0 a true 1.
#wynik
# 9
# Ile wartości w każdej kolumnie jest mniejsze niż 6?
print(np.sum(x<6, axis=0))
#wynik
# [[2,2,1, 2]]
# Czy jest wartość mniejsza niż 0?
print(np.any(x < 0))
#wynik true lub false

print(x)
#wynik
# [[4 7 4 5]
#  [3 8 0 5]
#  [7 4 0 0]
#  [3 4 5 1]]
print(x<5)
#wynik
# [[ True False  True False]
#  [ True False  True False]
#  [False  True  True  True]
#  [ True  True False  True]]
#indeksujemy te wartości tworzyma arrey jeden ciag w którym są same true
print(x[x<5])
#wynik
# [4 4 3 0 4 0 0 3 4 1]

#TODO FANCY Indexing

x = np.random.randint(100, size=10)
print(x)
#wynik
# [96 40 48 10 26 32 81 42 27 31]
#Chcemy wybrać 3, 7 i 2 lement - jak to zrobić
print([x[3], x[7], x[2]])
#wynik
# [10, 42, 48]
#sposób z fancy indexingiem
ind = [3,7,2]
print(x[ind])
#wynik
# [10 42 48]


print(x)
# #wynik
# [52 31  6 73  0 81 48 47 11 59]
ind = np.array([[3, 7],
                [4, 5]])
print(x[ind])
#wynik
# [[73 47]
#  [ 0 81]]

#TODO można łączyć oba sposób wylllko w różnych wymiarach

x = np.random.randint(100, size=(5, 5))
print(x)
#wynik
# [[83 64 92 37 94]
#  [21 81 36 35 13]
#  [ 2 17  5 32 71]
#  [ 6  7 34 32 98]
#  [79 54 26 52  8]]
print(x[2, [0, 1, 2]])
#wynik
# [ 2 17  5]
print(x[1:, [2, 0, 1]])
#wynik
# [[36 21 81]
#  [ 5  2 17]
#  [34  6  7]
#  [26 79 54]]

#TODO SORTOWANIE TABLIC
x = np.random.randint(100, size=(5))
print(x)
#wynik [32 53 62  2 52]
print(np.sort(x))
#wynik [ 2 32 52 53 62]
# sortowanie można również przeprowadzać w miejscu
print(x)
#wynik [13 72  5 66 87]
x.sort()
print(x)
#wynik [ 5 13 66 72 87]

#TODO sortowanie np.argsort który zwraca indeksy posortowanych elementów
x = np.random.randint(100, size=(5))
print(x)
#wynik [68 88 69 35 83]
i = np.argsort(x)
print(i)
#wynik [3 0 2 4 1]
print(x[i])
#wynik [35 68 69 83 88]

#TODO Cwiczenie 1

matrix = np.ones((5, 5))
print(matrix)
#wynik
#  [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]
zeros = np.zeros((3, 3))
print(zeros)
#wynik
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
zeros[1, 1] = 9
print(zeros)
#wynik
 # [[0. 0. 0.]
 # [0. 9. 0.]
 # [0. 0. 0.]]
matrix[1:-1,1:-1] = zeros
print(matrix)
#wynik
# [[1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 9. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 1. 1. 1. 1.]]

#TODO Cwiczenie 2
array = np.array([[ 1,  2,  3,  4,  5],
                  [ 6,  7,  8,  9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25],
                  [26, 27, 28, 29, 30]])
# print 11, 12 and 16, 17
aa=array[2:4, 0:2]
print(aa)
#wynik
# [[11 12]
#  [16 17]]
# chcemy uzyskać 2, 8, 14, 20
ss= array[[0, 1, 2, 3], [1, 2, 3, 4]]
print(ss)
#wynik
# [ 2  8 14 20]
# chcemy uzyskać 4,5 i 24,25 i 29,30
dd=array[[0, 4, 5], 3:]
print(dd)
#wynik
# [[ 4  5]
#  [24 25]
#  [29 30]]
x = np.array([1, 2, 3, 4])

# 2, 4, 8, 16
print(2 ** x)
#wynik użyliśmy potęgowania żeby
# [ 2  4  8 16]