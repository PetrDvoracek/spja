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
    lines = [[x for x in a if x]for a in [x.split(' ')for x in f.read().splitlines()]]

    area_calc = {'kruh': (lambda x: math.pi * (x[0]**2)),
                 'ctverec': (lambda x: x[0]**2),
                 'obdelnik': (lambda x: x[0] * x[1]),
                 'krychle': (lambda x: x[0]**3),
                 'kvadr': (lambda x: 2 * (x[0] * x[1] + x[2] * x[1] + x[0] * x[2]))}
    for i in lines:
        if i[0][0]=='#':
            print(' ')
            continue
        else:
            found_geometry = False
            for key, value in area_calc.items():
                if key==i[0]:
                    found_geometry=True
                    try:
                        print(value([float(x) for x in i[1:]]))
                    except IndexError as e:
                        print('spatne zadane vstupni parametry')
            if not found_geometry:
                print('tvar {0} neumim spocitat'.format(str(i[0])))

    #
    # for i in lines:
    #     found_geometry=False
    #     for key,value in area_calc.items():
    #         if not i[0][0]=='#':
    #             if i[0] == key:
    #                 found_geometry=True
    #                 try:
    #                     print(key + ' ' + str(value(i[1:])))
    #                 except Exception:
    #                     print('spatne vstupni hodnoty {0}'.format(str(i[:])))
    #         else:
    #             print(' ')
    #
    #     if not found_geometry:
    #         print('tvar {0} neumim spocitat'.format(str(i[0])))



if __name__ == "__main__":
    #mat = load_arena('/home/petr/tmp')
    #print(mat[3][1])
    my_area=area('area')
