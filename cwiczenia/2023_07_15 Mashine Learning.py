# import numpy as np
# import matplotlib.pyplot as plt
#
# # Wygenerowanie losowych danych
# losowe_dane = np.random.randint(1, 7, 1000000)  # 1000 wyników rzutu kostką sześcienną
#
#
# # Przykład obliczenia prawdopodobieństwa uzyskania 6 na kostce sześciennej
# prawdopodobienstwo = np.mean(losowe_dane == 6)
#
# # Wyświetlenie wyniku
# print(f'Prawdopodobieństwo uzyskania 6 na kostce sześciennej: {prawdopodobienstwo:.2f}')
#
#
# # Przykład ilustrujący przestrzeń próbkowania i zdarzenia
# przestrzen_probkowania = np.arange(1, 7)  # Przestrzeń próbkowania dla kostki sześciennej
# zdarzenie = (przestrzen_probkowania == 6) | (przestrzen_probkowania == 3)  # Zdarzenie polegające na uzyskaniu 6 lub 3
# wyniki = losowe_dane[np.isin(losowe_dane, przestrzen_probkowania[zdarzenie])]  # Wyodrębnienie wyników zdarzenia z losowych danych
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Funkcja obliczająca średnią próbkę
# def oblicz_srednia_probke(próbki):
#     return np.mean(próbki)
#
# # Przykładowe dane dotyczące rzutu monetą
# rzut_moneta = np.random.randint(0, 2, 10000)  # 0 - orzeł, 1 - reszka
#
# print(rzut_moneta)
#
# # Wyliczenie prawdopodobieństwa uzyskania orła lub reszki
# prawd_orzel = np.mean(rzut_moneta == 0)
# prawd_reszka = np.mean(rzut_moneta == 1)
#
# # Wyświetlenie wyników
# print(f'Prawdopodobieństwo uzyskania orła: {prawd_orzel}')
# print(f'Prawdopodobieństwo uzyskania reszki: {prawd_reszka}')
#
# # Wizualizacja danych
# fig, ax = plt.subplots()
# ax.hist(rzut_moneta, bins=2)
# ax.set_xticks([0, 1])
# ax.set_xticklabels(['Orzeł', 'Reszka'])
# ax.set_ylabel('Liczba wystąpień')
# ax.set_title('Wyniki rzutu monetą')
# plt.show()
#
# # Obliczenie średniej próbki w zależności od liczby próbek
# liczby_probek = [10, 50, 100, 500, 1000,1400,3000,4000, 5000, 10000, 50000, 100000,500000]
# srednie_probki = []
#
# for liczba_probek in liczby_probek:
#     próbki = np.random.randint(0, 2, liczba_probek)
#     srednia_probka = oblicz_srednia_probke(próbki)
#     srednie_probki.append(srednia_probka)
#
# # Wykres zależności średniej próbki od liczby próbek
# fig, ax = plt.subplots()
# ax.axhline(y=0.5, linestyle='--', color='r')
# ax.plot(liczby_probek, srednie_probki, label='Średnia próbki')
# ax.set_xscale('log')
# ax.set_xlabel('Liczba próbek')
# ax.set_ylabel('Prawdopodobieństwo orła')
# ax.set_title('Zbliżanie się średniej próbki do prawdziwego prawdopodobieństwa')
# ax.legend()
# plt.show()
#
# pip install plotly
#
# import plotly.graph_objs as go
# import numpy as np
#
# # Wygenerowanie przykładowych danych
# data = np.random.normal(0, 1, 1000)
#
# # Obliczenie średniej wartości dla różnych wielkości próbek
# means = [np.mean(data[:i]) for i in range(1, len(data)+1)]
#
# # Stworzenie interaktywnego wykresu średniej wartości
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=list(range(1, len(data)+1)), y=means,
#                          mode='lines', name='Średnia'))
# fig.update_layout(title='Średnia wartość dla próbki danych',
#                   xaxis_title='Wielkość próbki',
#                   yaxis_title='Średnia wartość')
# fig.show()
#
# import plotly.graph_objs as go
# import numpy as np
#
# # Wygenerowanie przykładowych danych
# data = np.random.normal(0, 1, 1000)
#
# # Obliczenie średniej wartości dla różnych wielkości próbek
# means = [np.mean(data[:i]) for i in range(1, len(data)+1)]
#
# # Stworzenie interaktywnego wykresu średniej wartości
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=list(range(1, len(data)+1)), y=means,
#                          mode='lines', name='Średnia'))
# fig.update_layout(title='Średnia wartość dla próbki danych',
#                   xaxis_title='Wielkość próbki',
#                   yaxis_title='Średnia wartość')
# fig.show()
#
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris
# import seaborn as sns
#
# # Wczytanie zbioru danych "iris"
# iris = load_iris()
# data = iris.data
# nazwy_cech = iris.feature_names
# nazwy_cech_pl = ['Długość działki kielicha', 'Szerokość działki kielicha',
#                  'Długość płatka', 'Szerokość płatka']
#
# # Obliczenie średniej arytmetycznej dla każdej cechy
# means = np.mean(data, axis=0)
#
# # Wyświetlenie średnich arytmetycznych
# for i, name in enumerate(nazwy_cech_pl):
#     print(f"Średnia arytmetyczna {name}: {means[i]}")
#
#
# # Obliczenie mediany dla każdej cechy
# medians = np.median(data, axis=0)
#
# # Wyświetlenie median
# for i, name in enumerate(nazwy_cech_pl):
#     print(f"Mediana {name}: {medians[i]}")
#
# # Obliczenie mody dla każdej cechy
# from scipy import stats
# modes = stats.mode(data, axis=0)
#
# # Wyświetlenie mod
# for i, name in enumerate(nazwy_cech_pl):
#     print(f"Moda {name}: {modes[0][i]}")

# import numpy as np
#
# # Generowanie losowych danych dotyczących wynagrodzeń w fikcyjnej firmie
# wynagrodzenia = np.random.randint(2000, 10000, size=150)
#
# # Obliczenie średniego wynagrodzenia
# srednie_wynagrodzenie = np.mean(wynagrodzenia)
# # Obliczenie mediany wynagrodzeń
# mediana_wynagrodzen = np.median(wynagrodzenia)
#
# # Dodanie kilku fikcyjnych bardzo wysokich wynagrodzeń
# wynagrodzenia[0] = 25000
# wynagrodzenia[1] = 30000
# wynagrodzenia[2] = 40000
# wynagrodzenia[3] = 50000
# wynagrodzenia[4] = 30000
# wynagrodzenia[5] = 25000
#
# # Obliczenie ponownie średniego wynagrodzenia
# nowe_srednie_wynagrodzenie = np.mean(wynagrodzenia)
# # Obliczenie ponownie mediany wynagrodzeń
# nowa_mediana_wynagrodzen = np.median(wynagrodzenia)
#
# print("Średnie wynagrodzenie przed dodaniem wartości odstających: ", srednie_wynagrodzenie)
# print("Średnie wynagrodzenie po dodaniu wartości odstających: ", nowe_srednie_wynagrodzenie)
#
# print("Mediana wynagrodzeń przed dodaniem wartości odstających: ", mediana_wynagrodzen)
# print("Mediana wynagrodzeń po dodaniu wartości odstających: ", nowa_mediana_wynagrodzen)
#
#TODO

# import numpy as np
# from sklearn.datasets import load_iris
#
# # Wczytanie zbioru danych "iris"
# iris = load_iris()
# data = iris.data
# feature_names = iris.feature_names
# nazwy_cech_pl = ['Długość działki kielicha', 'Szerokość działki kielicha',
#                  'Długość płatka', 'Szerokość płatka']
#
# # Obliczenie macierzy kowariancji
# covariance_matrix = np.cov(data.T)
#
# # Wyświetlenie macierzy kowariancji
# print("Macierz kowariancji:")
# print(covariance_matrix)
#
# # Obliczenie macierzy korelacji
# correlation_matrix = np.corrcoef(data.T)
#
# # Wyświetlenie macierzy korelacji
# print("Macierz korelacji:")
# print(correlation_matrix)
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Generating correlated data
# np.random.seed(0)
# x =y = np.random.normal(0, 1, 100)
# x + np.random.normal(0, 0.5, 100)
#
# # Creating a scatter plot
# plt.scatter(x, y)
# plt.xlabel('X values')
# plt.ylabel('Y values')
# plt.title('Scatter plot of correlated data')
# plt.show()
#
# import seaborn as sns
#
# # Wizualizacja macierzy korelacji
# sns.set(style="white")
# mask = np.zeros_like(correlation_matrix, dtype=bool)
# mask[np.triu_indices_from(mask)] = True
# sns.heatmap(correlation_matrix, mask=mask, square=True,
#             xticklabels=nazwy_cech_pl, yticklabels=nazwy_cech_pl,
#             cmap="coolwarm", annot=True)
# plt.title("Macierz korelacji")
# plt.show()
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Liczba możliwych wartości zmiennej losowej
# n = 6
#
# # Zdefiniujmy rozkład jednostajny dyskretny
# def uniform_distribution(x):
#     return 1/n * np.ones_like(x)
#
# # Wygenerujmy próbki
# samples = np.random.randint(1, n+1, size=10000)
#
# #TODO
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Liczba prób
# n = 10
#
# # Prawdopodobieństwo uzyskania orła
# p = 0.5
#
# # Generowanie próby 10000 rzutów monetą
# sample = np.random.binomial(n, p, 100000)
#
# # Wykres histogramu częstości liczby orłów
# plt.hist(sample, bins=np.arange(0,n+2)-0.5, density=True, color='skyblue', alpha=0.7)
# plt.xticks(np.arange(n+1))
# plt.xlabel('Liczba orłów')
# plt.ylabel('Częstość')
# plt.title('Rozkład dwumianowy (n=10, p=0.5)')
# plt.show()
#
# #TODO
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Liczba prób
# n = 10
#
# # Prawdopodobieństwo uzyskania orła
# p = 0.5
#
# # Generowanie próby 10000 rzutów monetą
# sample = np.random.binomial(n, p, 100000)
#
# # Wykres histogramu częstości liczby orłów
# plt.hist(sample, bins=np.arange(0,n+2)-0.5, density=True, color='skyblue', alpha=0.7)
# plt.xticks(np.arange(n+1))
# plt.xlabel('Liczba orłów')
# plt.ylabel('Częstość')
# plt.title('Rozkład dwumianowy (n=10, p=0.5)')
# plt.show()
#
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import poisson
#
# # ustal wartość oczekiwaną dla rozkładu Poissona
# lam = 5
#
# # wygeneruj próbkę danych dla godziny szczytu
# data = poisson.rvs(mu=lam, size=1000)
#
# # wyznacz liczbę zdarzeń w zakresie od 0 do 30
# k = np.arange(0, 31)
#
# # wyznacz wartości prawdopodobieństwa dla rozkładu Poissona
# poisson_pmf = poisson.pmf(k, mu=lam)
#
# # wykreśl histogram próbki danych
# plt.hist(data, bins=range(30), density=True, alpha=0.5, color='b')
#
# # wykreśl wykres funkcji prawdopodobieństwa rozkładu Poissona
# plt.plot(k, poisson_pmf, 'bo-', ms=8, label='Poisson PMF')
#
# # dodaj etykiety osi i legendę
# plt.xlabel('Liczba samochodów')
# plt.ylabel('Prawdopodobieństwo')
# plt.title('Symulacja ruchu na skrzyżowaniu')
# plt.legend()
#
# # wyświetl wykres
# plt.show()
#
# # wykreśl histogram próbki danych
# plt.hist(data, bins=range(30), density=True, alpha=0.5, color='b')
#
# # wykreśl wykres funkcji prawdopodobieństwa rozkładu Poissona
# plt.plot(k, poisson_pmf, 'bo-', ms=8, label='Poisson PMF')
#
# # dodaj etykiety osi i legendę
# plt.xlabel('Liczba samochodów')
# plt.ylabel('Prawdopodobieństwo')
# plt.title('Symulacja ruchu na skrzyżowaniu')
# plt.legend()
#
# # wyświetl wykres
# plt.show()
#
#
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm
#
# # Średni wzrost
# mean_heigh_men = 175
# mean_heigh_women = 165
#
# # Odchylenie standardowe dla kobiet i mężczyzn
# std_dev_women = 6.35
# std_dev_men =  7.62
#
# # Tworzenie siatki wartości x
# x = np.linspace(145, 210, 1000)
#
# # Generowanie wykresów funkcji gęstości prawdopodobieństwa dla kobiet i mężczyzn
# y_women = norm.pdf(x, loc=mean_heigh_women, scale=std_dev_women)
# y_men = norm.pdf(x, loc=mean_heigh_men, scale=std_dev_men)
#
# # Tworzenie wykresu dla kobiet
# plt.plot(x, y_women, label='Kobiety')
#
# # Tworzenie wykresu dla mężczyzn
# plt.plot(x, y_men, label='Mężczyźni')
#
# # Dodawanie legendy i etykiet osi
# plt.xlabel('Wzrost')
# plt.legend()
# plt.ylabel('PDF(Wzrost)')
# plt.title('Rozkład normalny wzrostu')
# plt.show()

#TODO W medycynie dokładność testów diagnostycznych jest bardzo ważna. Przeprowadźmy analizę dla hipotetycznego testu, który wykrywa chorobę układu oddechowego. Zakładamy, że 5% populacji choruje na tę chorobę. Test diagnostyczny ma dokładność 85% i 90% dla pacjentów chorych i zdrowych, odpowiednio. Na podstawie tych danych należy obliczyć prawdopodobieństwo, że osoba z wynikiem pozytywnym testu faktycznie choruje na tę chorobę.

#A
# p_chory = 0.05
# #B
# p_pozytywny_chory = 0.85
# p_pozytywny_zdrowy = 0.1
# p_negatywny_zdrowy = 0.9
# p_zdrowy = 0.95
# p_pozytywny = p_pozytywny_chory * p_chory + p_pozytywny_zdrowy * p_zdrowy
# p_chory_pozytywny = p_pozytywny_chory * p_chory / p_pozytywny
# print(p_chory_pozytywny)

#link z opisem https://pl.wikipedia.org/wiki/Paradoks_wyniku_fa%C5%82szywie_pozytywnego

#TODO Przeprowadzamy badania na populacji studentów w celu zbadania ich średniego wzrostu. Zakładamy, że wzrost studentów ma rozkład normalny o średniej wartości 170 cm i odchyleniu standardowym 6 cm. Napisz program w Pythonie, który obliczy prawdopodobieństwo, że losowo wybrany student będzie miał wzrost pomiędzy 165 a 175 cm.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#sredni wzrost
sredni_wzrost = 170
#sigma - odchylenie standardowe
sigma = 6

w = norm.cdf(175, loc = sredni_wzrost, scale = sigma)
n = norm.cdf(165, loc = sredni_wzrost, scale = sigma)
print("Prawdopodobieństwo ", round((w-n),2))
