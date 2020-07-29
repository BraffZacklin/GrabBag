a = 0
b = 5

def main():
	global a, b
	i = 10
	b = g(i)
	print(a + b + i)

def f(i):
	n = 0
	while n * n <= i:
		n = n + 1
	return n - 1

def g(a):
	b = 0
	for n in range(a):
		i = f(n)
		b = b + i
	return b

main()

#TYPE ERROR originally
#CHANGED g(a) to return b, and call main()
#RESULT is 26