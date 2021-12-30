#with userinput 
n=int(input('enter no '))
fact=1
while n>=2:
	fact=fact*n
	n-=1
print('factorial no :', fact)