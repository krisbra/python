###PETLA WHILE 20.06.2023
liczby = list() #[]
i = 2
while i < 11:
    liczby.append(i)
    i += 2  #i = i + 2
print(liczby)  #[2, 4, 6, 8, 10]

###wykonujemy to wtedy kiedy wiemy ile razy jest proces powtarzalny

lines = list()
# print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while line != '':
#     lines.append(line)
#     line = input('Następna linijka: ')  # reset
# print(lines)


lines = list()
print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while len(line):
#     lines.append(line)
#     line = input('Następna linijka: ')  # reset
# print(lines)
##STEROWANIE PTLAMI
#przerywanie


for val in "string":
    if val == "i":
        break
    print(val)

print("Koniec")