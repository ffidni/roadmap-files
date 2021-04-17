from os import system
from time import sleep
import numpy as np

"""TODO: 1. CREATE MAIN FUNCTION
		 2. FIX THE MULTIPLIED MATRICES RESULT
		 3. CREATE A FEATURE TO CONTINUES MULTIPLIED THE MULTIPLIED MATRIX.
		 4. FIX INPUT ANIMATIONS."""

def multiply(matrix1, matrix2):
	index,m1_index,m2_index,counter = 0,0,0,1
	rows, cols = len(matrix1),len(matrix2[0])
	result = []
	r1 = 0
	r2 = 0
	dot_product = ''
	while (m1_index < rows):
		if not dot_product or dot_product[-1] == '+':
			try:
				#print(F"M1 = {matrix1[m1_index][index]} x {matrix2[index][m2_index]} = M2")
				dot_product += str(matrix1[m1_index][index] * matrix2[index][m2_index])
				index += 1
			except:

				index = 0
				m2_index += 1
				counter += 1
		else:
			dot_product += '+'

		if dot_product and dot_product[-1] != '+':
			if len(dot_product.split('+')) == len(matrix1[0]):
				result.append(eval(dot_product))
				dot_product = ''
		
		if counter == cols+1:
			m1_index += 1
			m2_index = 0
			counter = 0
	
		#print(f"m2_index: {m2_index}, length m2= {len(matrix2[0])}Counter= {counter}, Rows: {rows}, Cols: {cols}\n")
	return np.array(result).reshape(rows, cols)

def generate_dimensions():
	CLEAR_SCREEN()
	print("Dimensions format, i.e -> 2x3")
	dimensions = [input(f"Input the dimension for matrix {num}: ") for num in range(1, 3)]
	if dimensions[0][-1] != dimensions[1][0] and len(dimensions[0]) < 3 or len(dimensions[1]) < 3:
		print("The column for the matrix A should be the same as row in the matrix B\ni.e Matrix A: 3x2, Matrix B: 2x5")
		sleep(3)
		dimensions = generate_dimensions()
	return dimensions

def print_matrix(matrix, index=0):
	CLEAR_SCREEN()
	if index:
		print(f"Matrix {index} has been created:")

	for rows in matrix: 
		print(f"\t{rows}")

def fill_columns(index, dimension):
	CLEAR_SCREEN()
	example = ' '.join(str(cols) for cols in range(1, int(dimension)+1))
	numbers = input(f"Input {dimension} numbers for row {'A' if index+1 == 1 else 'B'}\n example -> {example}: ").split()
	cols = list(map(int, numbers))
	if len(cols) != int(dimension):
		print(f"Please put {dimension} numbers to the matrix!")
		sleep(1)
		cols = fill_columns(index, dimension)
		
	return cols

def fill_rows(dimensions):
	matrices = [[], []]
	for index, dimension in enumerate(dimensions): #
		for rows in range(int(dimension[0])):
			cols = fill_columns(index, dimension[-1])
			matrices[index].append(cols)
			print(f"{cols} has been added to matrix {'A' if index+1 == 1 else 'B'}")
			sleep(1)
			if len(matrices[index]) == int(dimension[0]):
				print_matrix(matrices[index], index+1)
				sleep(1)

	return matrices

def main():
	dimensions = generate_dimensions()
	m1, m2 = fill_rows(dimensions)
	result = multiply(m1,m2).tolist()
	print_matrix(result)


if __name__ == '__main__':
	CLEAR_SCREEN = lambda: system('cls')
	main()