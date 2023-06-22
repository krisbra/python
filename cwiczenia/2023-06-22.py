def simple_function():
    print('Hello world!')
    print('Wikipedia')


simple_function()
print()
simple_function()

def my_function():
    return 3 + 3 # może być wartość krotka, strong wszystko, kończy funkcje

###pamiętajmy żeby wrzucając printa użyć wewnątrz funkcji a nie odnosić sie do zmienych bo na nich nie da się potem robić działań na princie - a na fukcji już tak.

print(my_function())

 #######
def add(x, y): ###możemy wpisać y=10 wtedy bedzie defaultowo 10 i tez zadziała)
    print('x =', x, ', y =', y)
    return x + y


print(add(2, 3))
# print(add(x=2, y=3)) - tak też można zrobić i mówiąc wprost kolejność wpriowadzania znaków nie ma znaczenia
# print(add(int(input('x=')), int(input('y=')))) też zadziała i mozeny wprowadzać z ręki rzeczy
### definiujemy wywołanie i podstawiamy te dane pod wzór
add(2,3)

##### DOCSTRING

def my_function():
    """Dokumentacja funkcji"""

help(my_function())

### rekurencja/rekursja (recursion)

