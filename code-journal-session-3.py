#code journal 1
#session prompt 3

def f(x):
		return x**3 + 8

def main():
	x = 9
	result = f(x)
	print(result)
	if result > 27:
		print("YAY!")

if __name__=="__main__":
	main()