import sys

def parser(arg):
    args={}
    for i in arg[1:]:
        a=i.split('=')
        args.update({a[0] : a[1]})
    return args

class Counter:

    number_of_counters = 0      #tridni promenna


    def __init__(self, count = 0):
        self.counter = count    #instancni promenna
        Counter.number_of_counters +=1
        self.__privatni = count #privatni promenna menena pouze pres metody
    #
    # def get_count(self):
    #     return self.__privatni
    #
    # def set_count(self, count):
    #     self.__privatni = count
    # count = property(get_count, set_count)
    @property   #kdyz neni @property tak to vytiskne funkci
    def count(self):
        return self.__privatni

    @count.setter
    def count(self, count):
        self.__privatni = count

    def __add__(self, other):
        return Counter(self.counter + other.count)



if __name__=="__main__":
    pass