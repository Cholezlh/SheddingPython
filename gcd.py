import random

#a = random.randint(10 ** 9, 10 ** 10)
#b = random.randint(10 ** 9, 10 ** 10)
a=10
b=21
def min(a,b):

	if a>b:
		return b
	else:
		return a

n = min(int(a/2)+1,int(b/2+1))

if a % b == 0 or b % a == 0:
	print 'gcd(%d,%d) is %d' % (a,b,min(a,b))
else:
	while n>1:
		if a % n == 0 and b % n == 0:
			print 'gcd(%d,%d) is %d' % (a,b,n)
			break
		n = n-1
	else:
		print 'gcd(%d,%d) is 1' % (a,b) 