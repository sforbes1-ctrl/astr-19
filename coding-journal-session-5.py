#coding journal1
#session5

import numpy as np

def main():

	num_points = 1000	
	for i in range(num_points + 1):
		x = 2 * i / num_points
		y = (f"sin({x})")
		print( "x =",x, "sin(x) =", y)
		
if __name__ == "__main__":
	main()