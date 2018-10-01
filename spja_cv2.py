def fu(x):
	return 3*x+5

def fu_map(list_data, function):
	tmp=[]
	for i in list_data:
		tmp.append(function(i))
	return tmp

if __name__=='__main__':
	print(str(fu_map(['neco',0,2.3],fu)))
