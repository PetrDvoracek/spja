# -*- coding: utf-8 -*-

'''
Úloha č. 1

Vytvořte funkci load_sets, která má jeden parametr - název souboru a vrátí slovník
obsahující jednotlivé záznamy Lego setů ze zadaného souboru ve formátu
{'set_num': {'name': str, 'year': int, 'theme_id': int, 'num_parts': int}, ...}

Popis atributů uložených v csv souborech najdete také zde
https://rebrickable.com/downloads/
'''


def load_sets(file_name):
    sets = {}
    with open(file_name, 'rt') as f:
        next(f)
        lines = [a.split(',')for a in [x.strip()for x in f.read().splitlines()]]
        for i in lines:
            # if not (is_int(i[2]) or is_int(i[3]) or is_int(i[4])):
            #     continue
            # else:
            #     sets.update(str(i[0]):{'name':i[1], 'year':int(i[2]), 'theme_id':int(i[3]),'num_parts':int(i[4])}})
            try:
                sets.update({str(i[0]):{'name':i[1], 'year':int(i[2]), 'theme_id':int(i[3]),'num_parts':int(i[4])}})
            except  ValueError:
                pass
    return sets

def is_int(i):
    try:
        int(i)
        return True
    except TypeError as e:
        return False

'''
Úloha č. 2

Vytvořte funkci, která vrátí slovník obsahující jen ty záznamy z načtených
Lego setů, jejichž číslo setu set_num (reprezentované jako string) začíná na
zadané set_num_start.

V případě, že vám úloha č. 1 nefunguje, můžete použít následující slovník:
sets = {'75884-1': {'name': '1968 Ford Mustang Fastback', 'year': 2018, 'theme_id': '601', 'num_parts': 183}, '75885-1': {'name': 'Ford Fiesta M-Sport WRC', 'year': 2018, 'theme_id': '601', 'num_parts': 205}, '75886-1': {'name': 'Ferrari 488 GT3 Scuderia Corsa', 'year': 2018, 'theme_id': '601', 'num_parts': 182}, '75887-1': {'name': 'Porsche 919 Hybrid', 'year': 2018, 'theme_id': '601', 'num_parts': 166}, '75888-1': {'name': 'Porsche 911 RSR & 911 TURBO 3.0', 'year': 2018, 'theme_id': '601', 'num_parts': 394},}
'''


def get_set(set_num_start, sets):
    return {k:v for k,v in sets.items() if str(k).startswith(set_num_start)}



'''
Úloha č. 3

Vytvořte funkci load_themes, která má jeden parametr - název souboru a vrátí slovník
obsahující jednotlivé záznamy Lego témat ze zadaného souboru ve formátu
{id: {'name': str, 'parent_id': int}, ...}
Bude nutné ošetřit načítání řádků, které nemají uvedené 'parent_id'.
U neuvedených parent_id nastavte jejich hodnotu na -1
'''


def load_themes(file_name):
    themes = {}
    with open('themes.csv','rt') as f:
        next(f)
        lines = [a.split(',') for a in [x.strip() for x in f.read().splitlines()]]
        lines = [[x for x in a if x]for a in lines]
        for i in lines:
            try:
                themes.update(
                    {int(i[0]): {'name': i[1], 'parent_id': int(i[2])}})
            except  IndexError:
                themes.update({int(i[0]): {'name': i[1], 'parent_id': -1}})
    return themes





'''
Úloha č. 4

Vytvořte funkci print_info, která pro zadaný model Lega (např. 6876) vypíše
informace v předepsaném formátu

'''


def print_info(set_num_start, sets, themes):
    the_set=get_set(sets,set_num_start)
    the_set.update(get_set(themes,set_num_start))

    print("┌───────────┬──────────────────────────┬──────────────────────────┬───────┬──────┐")
    print("│ Set ID    │ Name                     │ Theme                    │ Parts │ Year │")
    print("├───────────┼──────────────────────────┼──────────────────────────┼───────┼──────┤")
    for k,v in the_set:
        print("| {:>13d} | {:<20s} | {:>13d} | {:>14d} | {:>")
    print("└───────────┴──────────────────────────┴──────────────────────────┴───────┴──────┘")


'''
Úloha č. 5

Vytvořte funkci print_stats, která pro modely Lega uložené ve slovniku sets
vytiskne jednoduchou statistiku zahrnujici minimální, maximální a průměrný počet
kostek v modelu, počet témat a počet modelů v tématu.
'''


def print_stats(set_num_start, sets, themes):
    pass


def main():
    sets=load_sets('sets.csv')
    print(get_set('700',sets))
    load_themes('themes.csv')

if __name__ == "__main__":
    main()
