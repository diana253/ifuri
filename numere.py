def adunarecifre2():
    print("Introduceti va rog un numar de doua cifre:")
    a = input()
    a = int(a)
    z = a // 10
    u = a % 10
    print("suma zecilor si unitatilor este:", z+u)

def adunarecifre3():
    print("introduceti, va rog, un numar de trei cifre:")
    a = input()
    a = int(a)
    s = a // 100
    z = (a // 10) % 10
    u = a % 10
    print("suma cifrelor sutelor, zecilor si unitatilor este:", s+z+u)

def capetepicioare():
    print("introduceti numarul de gaini:")
    g = int(input())
    print("introduceti numarul de oi:")
    o = int(input())
    print("numarul de capete este:", g+o, ", iar numarul de picioare este:", 2*g + 4*o)

def oisigaini():
    # 2*g + 4*o = p; g + o = c
    print("introduceti numarul de picioare:")
    p = int(input())
    print("introduceti numarul de capete:")
    c = int(input())
    o = p - (2*c)//2
    g = c - o
    print("numarul de gaini este:", g, ", iar numarul de oi este:", o)


def eliminarecifre():
    print("introduceti, va rog, un numar de trei cifre:")
    a = input()
    a = int(a)
    s = a // 100
    z = (a // 10) % 10
    u = a % 10
    print("numarul rezultat prin eliminarea cifrei din mijloc este", str(s)+str(u))

def ariesivolum():
    print("introduceti valoarea laturii cubului:")
    l = input()
    l = int(l)
    s = 6 * l * l
    v= l ** 3
    print("suprafata cubului este:", s, ", iar volumul este:", v)

if __name__ == "__main__":
    adunarecifre2()
    adunarecifre3()
    capetepicioare()
    oisigaini()
    eliminarecifre()
    ariesivolum()

