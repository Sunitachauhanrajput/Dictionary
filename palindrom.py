n=int(input('enter no '))
rev=0
i=n
while n>0:
	rev=rev*10+n%10
	n=n//10
if i==rev:
	print('palindrome no')
else:
	print('not ')