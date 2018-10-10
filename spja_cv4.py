

class Counter(object):

    no_of_counter=0

    def __init__(self, count=0):
        self.count=count
        Counter.no_of_counter+=1

    def set_counter(self,count):
        self.count=count

    def get_counter(self):
        return self.count

    counter=property(get_counter, set_counter)

    def inc_counter(self):
        self.counter+=1

    def __add__(self, other):
        new_counter=Counter(self.count+other.count)
        return new_counter

    @staticmethod
    def print_no_of_counters():
        print(str(Counter.no_of_counter))


if __name__=='__main__':
    pass
