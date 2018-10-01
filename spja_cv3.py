import math


def add(tuple_first, tuple_second):
    tmp = []
    [tmp.append(x + y)for x, y in zip(tuple_first, tuple_second)]
    return tuple(tmp)


def load_arena(folder_path):
    f = open(folder_path, 'r')
    lines = f.read().splitlines()
    novy = list(map(lambda x: [1 if i == 'x' else 0 for i in x], lines))
    return novy


def area(folder_path):
    f = open(folder_path, 'r')
    lines = f.read().readlines()
    area_calc = {'kruh': (lambda x: math.pi * (x**2)),
                 'ctverec': (lambda x: x**2),
                 'obdelnik': (lambda x, y: x * y),
                 'krychle': (lambda x: x**3),
                 'kvadr': (lambda x, y, z: 2 * (x * y + z * y + x * z))}


if __name__ == "__main__":
    mat = load_arena('/home/petr/tmp')
    print(mat[3][1])
