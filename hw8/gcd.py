import random

a = random.randint(10 ** 9, 10 ** 10)
b = random.randint(10 ** 9, 10 ** 10)
#a=69
#b=21
def min(a,b):

	if a>b:
		return b
	else:
		return a


def gcd(x,y):
	if x % y == 0 or y %x == 0:
		return min(x,y)
	else:
		return gcd(y,x%y)
gcd=gcd(a,b)

print 'gcd(%d,%d) = %d' % (a,b,gcd) 