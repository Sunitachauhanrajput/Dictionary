a=int(input('enter no'))
count=0
i=1
while i<=a:
	if a%i==0:
		count=count+1
	i+=1
if count==2:
	print(a,'prime')
else:
	print(a,'composit')