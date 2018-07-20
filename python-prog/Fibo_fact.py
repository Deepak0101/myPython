''''

Using yieled to generate Fibo numbers
'''

#range object is iterable

def fibo_generator(limit):
	a, b= -1, 1
	count = 0

	while count < limit:
		c = a+b
		yield c

		a = b
		b = c

		count += 1
		#return c
	

def fact(limit):
	def factorial(n):
		if n == 1: return 1
		return n* factorial(n-1)

	for i in range(1,limit+1):
		yield factorial(i)


def main():
	fg = fibo_generator(10)
	for i in fg :
		print(i)

	fac = fact(10)
	for i in fac :
		print(i)


	

if __name__ == '__main__':
	main()