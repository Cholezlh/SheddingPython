wealth = 100.0
salary = 10.0   # your daily salary
r = 0.2 # your daily rate of return for investment

# You have 100.0 at beginning. Each day, you earn your fix amount of 
# salary, as well as 20% of income by investing your existing wealth.

day = 0

# Use while loop to finish calculation. As well as showing how much 
# money you have every day.
# You become rich when your wealth reached 10000. That's when you'll 
# conclude your calculation and declare that you're rich.

# Your code here.

while wealth<10000:
	wealth=wealth*(1+r)+salary
	day=day+1



print 'You got rich in %d days' % day