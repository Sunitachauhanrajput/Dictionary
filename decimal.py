num=int(input('enter no '))
sum=0
i=0
while num!=0:
	rem=num%10
	sum=sum+rem*pow(2,i)
	num=int(num/10)
	i=i+1
print("decimal no:",sum)