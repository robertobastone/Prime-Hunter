######################### Prime Hunter

# author: Roberto Bastone
# email: robertobastone93@gmail.com


# code

print "Welcome to the prime Hunter"

num = input("Type an integer, the Hunter will tell whether it is a prime number.\n")
div = 2
while ( int(num) % div != 0):
	div = div + 1
if ( int(num) == div):
	print "The Hunter says that", num, "is prime"
else:
	print "The Hunter says that", div, "is the divisor of", num
