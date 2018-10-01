#promenlivy pocet argumentu funkce
def f(a,b,*arg):
	print('a: ', a)
	print('b: ', b)
	print('arg: ', arg) # arg je tuple

def second_f(**kw): #kw je dict, pokud funkci chci volat s ruznymy parametry, iteruju pres dict
	print(kw)

#anonymni funkce
#map() aplikuje lambdu na vsechny prvky pole

lst=[]
lst.extend([1,2])	#pripoji na konec listu list [1,2]
list(filter(lambda x:x>4,lst))
list(map(lambda x: x**2, filter(lambda x: x>4, lst)))
[x**2 for x in lst if x>4] # udelej neco pouze pokud je to vetsi nez 4
#soubor otevirat vzdy s with
try:
	with open('file') as f:
	for line in f:
		print(line.strip())	#strip() nacte bez \n
except Exception as e:
	print(e,type(e))	##exception handling
else:
	pass
finally:
	pass

with open('file', 'wt') as f:
	for row in matrix:
		f.write(','.join([ str(x) for x in row]) + '\n')
