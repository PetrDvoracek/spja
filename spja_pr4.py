# OOP muzebyt i bez dedicnosti. jedine co je treba je polymorfismus
# polymorfismus neni dedeni! viz v pythonu nic nemusim dedit, staci kdyz maji tridy metody stejne
#protoze python je oop ale dynamicky typovany. zavola - metodu na jakemkoliv objektu
#dedeni jako takove nezajisti polymorfismus.
# pokud nemusim dedit, nededim!!!
#typovani: dynamicke(python) vs staticke(C# C++); implicitni(C# var, C++ auto, Haskell+staticky) vs explicitni(c++, C#)
#C# slabe typovani - int -> float muzu pretypovavat (unmanaged, z virtualniho stroje vyjdu do unmanage kodu a menim mu to pod rukama)
#Haskell nedovoli zkompilovat pokud saham mimo index pole
# spravnost software (americka bezpecnost..) sedokazuje matematickym dukazem - nikdy neudelam v dynamicky typovanem jazyku
# burza - haskel, ocamel zajistuji automaticky korektnost
# john mcCarthy

import datetime
class Dog:
    def __init__(self,name):
        self.name=name

    def make_sound(self):
        return "haf"

class Cat:
    def __init__(self,name):
        self.name=name

    def make_sound(self):
        return "mau"
animals=[Dog('neco'),Cat('jineho')]
for a in animals:
    pass
# decorator


def logger(f):
    def wrapped():
        print(datetime.datetime.now())
        f()
        print(datetime.datetime.now())
    return wrapped

@logger
def test_fun():
    print('long')

test_fun = logger(test_fun)
test_fun
#36,37 <=> 32,33
#|||
# + je treba vnuceni argumentu

def logger(f):
    def wrapped(*args, **kw):
        print(datetime.datetime.now())
        f(*args, **kw)
        print(datetime.datetime.now())
    return wrapped

@logger
def test_fun(greetings):
    print('long' + greetings)

#test_fun = logger(test_fun)
test_fun
#|||
# + argumenty dekoratoru

def logger(prefix):
    def read_decorator(f):
        def wrapped(*args, **kw):
            print(prefix, datetime.datetime.now())
            f(*args, **kw)
            print(prefix, datetime.datetime.now())
        return wrapped
    return read_decorator()

@logger('neco')
def test_fun(greetings):
    print('long' + greetings)
