# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def sumanumere():
    print('introduceti primul numar, a=')
    a = int(input())
    print('numarul introdus a fost', a)
    print('introduceti al doilea numar, b=')
    b = int(input())
    print('numarul introdus a fost', b)
    print('suma numerelor a si b este a+b, adica', a+b)


def inmultireanr():
    print('introduceti primul numar, a=')
    a = int(input())
    print('numarul introdus a fost', a)
    print('introduceti al doilea numar, b=')
    b = int(input())
    print('numarul introdus a fost', b)
    print('inmultirea numerelor a si b este a*b, adica', a*b)


def impartireanr():
    print('introduceti primul numar, a=')
    a = int(input())
    print('numarul introdus a fost', a)
    print('introduceti al doilea numar, b=')
    b = int(input())
    print('numarul introdus a fost', b)
    print('impartirea numerelor2 a si b este a/b, adica', a/b)


def impartirea2():
    print('introduceti primul numar, a=')
    a = int(input())
    print('numarul introdus a fost', a)
    print('introduceti al doilea numar, b=')
    b = int(input())
    print('numarul introdus a fost', b)
    print('impartirea numerelor2 a si b este a//b, adica', a//b)


def perimetrul():
    print('introduceti prima latura, AB=')
    AB = int(input())
    print('prima latura este', AB)
    print('introduceti a doua latura, BC=')
    BC = int(input())
    print('a doua latura este', BC)
    print('introduceti a treia latura, AC=')
    AC = int(input())
    print('a treia latura este', AC)
    print('perimetrul triunghiului este:', AB+BC+AC)


def aria():
    print('introduceti prima cateta, c1=')
    c1 = int(input())
    print('prima cateta este', c1)
    print('introduceti a doua cateta, c2=')
    c2 = int(input())
    print('a doua cateta este', c2)
    print('aria triunghiului dreptunghic este:', (c1*c2)/2)

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    sumanumere()
    inmultireanr()
    impartirea2()
    impartireanr()
    perimetrul()
    aria()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
