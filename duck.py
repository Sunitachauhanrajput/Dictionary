#duck no
n=int(input("enter no "))
c=0
while n>0:
	a=n%10
	n=n//10
	if a==0:
		c=c+1
if c>=1:
	print("duck ")
else:
	print("not")