def IF(cond,funcA,funcB,parA=None,parB=None):
	if(cond):
		if(parA):
			funcA(parA);
		else:
			funcA()
	else:
		if(parB):
			funcB(parB)
		else:
			funcB()

def LOOP(count, func, par=None):
	i = 0
	while(i<counter):
		if(par):
			func(i,par)
		else:
			func(i)
		i +=1

def ADD(a,b):
	return a+b

def SUB(a,b):
	return a-b

def MUL(a,b):
	return a*b

def DIV(a,b):
	return a/b

def PRINT(var=""):
	print(var)
	return(str(var))
