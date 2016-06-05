import random

# You have 90% of chance to be able to laugh.
def canLaugh():
	return random.random() > 0.1

def laugh():
	print ':D'

def weep():
	print 'T_T'

# Write your program using while loop so that:
# * While you can laugh, continue laughing.
# * While you can't laugh, stop laughing and weep.
# * Your tears ends the program.
# * You can't laugh more than 5 times.
i=0
while canLaugh() and i<5:
	laugh()
	i=i+1
weep()
