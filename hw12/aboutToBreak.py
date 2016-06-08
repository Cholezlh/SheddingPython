# Pressure rising every day by a fixed portion. Finish the program 
# using break statement, see if you can survive the year.

import random

pressure = 1.0
pressureRate = 1 + random.randint(7, 17) / 1000.0
pressureLimit = 100.0   # how much pressure you can endure
print 'pressureRate = %f' % pressureRate
day = 0

broken = False

while day < 365:
    pressure *= pressureRate
    print 'Pressure rising: %.3f' % pressure

    # Your code here. 
    if pressure<pressureLimit:
        day += 1 
    else:
    	broken=True
    	break
    	
    
if broken:

    print 'Too much pressure, you break on day %d' % day
else:
    print 'Luckily, you survived the year.'