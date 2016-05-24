lst = ['a', 'b', 'c', 'd', 'e']
print 'Originally, the list is: %s' % lst

# Your solution here. 
print 'The third element in the list is: %s' % lst[2]

# Now change the third element to 'i'
lst[2]='i'

print "Changed the third element to 'i', now the list is: %s" % lst

# Remove the first element from list
lst.pop(0)

print "Removed the first element, now the list is: %s" % lst

# Add a 't' at the end of list
lst.append('t')

print "Added a 't' at the end, now the list is: %s" % lst

# Fill your solution at the end of line.

print 'At last the word is: %s' % lst+', which has %d ' % len(lst) + 'letters.'