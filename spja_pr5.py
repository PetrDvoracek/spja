#moduly slouzi k tomu aby nenastavaly konflikty jmena
# if __name__='__main__': se pouziva pro testovani
#explicit is better than implicit - napr self, nikdo nic nerika za me
#flat is better than nested - lepsi jedno pole se vsim nez 100 ruznych poli
#sparse is better than nested - komprimace
#dutch - autor python je holandan

#parsovani xml a json. xml puvodne dokumentace us army software - samopopisujici
#sax parser - musim nakodit, malo pameti zere
#don element - spracuje vse sam, ale zere pamet
#__init__ se spousti prikazem import
import xml.etree.cElementTree as ET

root = ET.parse('menza.xml') # ElementTree instance

dates = root.findall('date') # list of elements

for date in dates:
    print(date.attrib['day'])
    meals = iter(date)#vyhoda vyuziva mene pameti

    for meal in meals:
        print('\t' + meal.attrib['name'])
        for ingredient in meal.iterfind('ingredient'):
            print('\t\t' + ingredient.attrib['name'])

def xml2py(node):
    name = node.tag

    pytype = type(name, (object, ), {})#tvori datovy typ podle name, nadrazeny objekt(dedi?), atributy. , za object protoze je to tuple
    #tridy v pythonu je slovnik kde klic je jmeno a hodnota samotna funkce
    #c# reflexe, pomale, nebezpecne, nepekne
    #co je introspekce?
    #vyhoda je prehlednost
    #linq v c# musel nekdo udelat spoustu interface atd
    #list comp v pythonu stacilo upravit compiler
    #lisp - prefixovy jazyk . n length == n.length
        #nejvice vyrazovy jazyk, dsp jazyky (domenove specificke) muzu si vytvorit vlastni syntax
    1
    pyobj = pytype()

    for attr in node.attrib.keys():
        setattr(pyobj, attr, node.get(attr))

    if node.text and node.text != '' and node.text != ' ' and node.text != '\n':
        setattr(pyobj, 'text', node.text)

    for cn in node:
        if not hasattr(pyobj, cn.tag):
            setattr(pyobj, cn.tag, [])
        getattr(pyobj, cn.tag).append(xml2py(cn))

    return pyobj