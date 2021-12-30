a=int(input('enter no '))
b=int(input('enter no '))
c=a
sum=0
while c>0:
	d=c%10
	sum=sum+d**b
	c=c//10
if sum==a:
	print(a,'armstrong')
else :
	print(a,'composit')