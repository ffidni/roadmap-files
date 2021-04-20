from os import system
from time import sleep
from main import *
import numpy as np

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
	
	return np.array(result).reshape(rows, cols)

def print_matrix(matrix1,matrix2=None,matrix3=None, index=0):
	CLEAR_SCREEN()

	if index:
		print(f"Matrix {index if isinstance(index, int) else 'B'} has been created:")

	if matrix1 and matrix2 and matrix3:
		largest_matrix = max(len(matrix1), len(matrix2), len(matrix3))
		spaces_a = " "*len(str(matrix1[0]))
		spaces_b = " "*len(str(matrix2[1]))
		spaces_c = " "*len(str(matrix3)[0])
		print_spaces = "{a} {b}   {c}"
		for index in range(largest_matrix):
			if index == largest_matrix//2:
				print_spaces = "{a} {b} = {c}"

			if index > len(matrix1)-1 and index > len(matrix2)-1:
				print(print_spaces.format(a=spaces_a, b=spaces_b, c=matrix3[index]).replace(',', ' '))
			elif index > len(matrix1)-1 and index > len(matrix3)-1:
				print(print_spaces.format(a=spaces_a, b=matrix2[index], c=spaces_c).replace(',', ' '))
			elif index > len(matrix2)-1 and index > len(matrix3)-1:
				print(print_spaces.format(a=matrix1[index], b=spaces_b, c=spaces_c).replace(',', ' '))
			elif index > len(matrix1)-1:
				print(print_spaces.format(a=spaces_a, b=matrix2[index], c=matrix3[index]).replace(',', ' '))
			elif index > len(matrix2)-1:
				print(print_spaces.format(a=matrix1[index], b=spaces_b, c=matrix3[index]).replace(',', ' '))
			elif index > len(matrix3)-1:
				print(print_spaces.format(a=matrix1[index], b=matrix2[index], c=spaces_c).replace(',', ' '))
			else:
				print(print_spaces.format(a=matrix1[index], b=matrix2[index], c=matrix3[index]).replace(',', ' '))

			print_spaces = "{a} {b}   {c}"

	else:
		for rows in matrix1:
			print(f"{str(rows).replace(',', ' ')}")
		
def generate_dimensions(dimension_a=None):
	CLEAR_SCREEN()

	print("Dimensions format, i.e -> 2x3")
	if dimension_a:
		dimensions = [dimension_a, input(f"Matrix A dimensions: {dimension_a}\nInput the dimension for matrix B: ")]
	else:
		dimensions = [input(f"Input the dimension for matrix {'A' if num == 1 else 'B'}: ") for num in range(1, 3)]
	if dimensions[0][-1] != dimensions[1][0] or len(dimensions[0]) < 3 or len(dimensions[1]) < 3:
		print("The column for the matrix A should be the same as row in the matrix B\ni.e Matrix A: 3x2, Matrix B: 2x5")
		sleep(3)
		if dimension_a:
			dimensions = generate_dimensions(dimension_a)
		else:
			dimensions = generate_dimensions()

	return [dimensions[1]] if dimension_a else dimensions
	
def generate_matrix(dimensions, matrix_a=False):
	def fill_columns(index, dimension):
		CLEAR_SCREEN()

		example = ' '.join(str(cols) for cols in range(1, int(dimension)+1))
		numbers = input(f"Input {dimension} numbers for row {'B' if matrix_a else ('A' if index+1 == 1 else 'B')}\n example -> {example}: ").split()
		cols = list(map(int, numbers))
		if len(cols) != int(dimension):
			print(f"Please put {dimension} numbers to the matrix!")
			sleep(1)
			cols = fill_columns(index, dimension)

		return cols

	def fill_rows(dimensions):
		if matrix_a:
			matrices = []
		else:
			matrices = [[], []]

		for index, dimension in enumerate(dimensions): #
			for rows in range(int(dimension[0])):
				cols = fill_columns(index, dimension[-1])
				if matrix_a:
					matrices.append(cols)
				else:
					matrices[index].append(cols)
				cols = str(cols).replace(',', '')
				print(f"{cols} has been added to matrix {'B' if matrix_a else ('A' if index+1 == 1 else 'B')}")
				sleep(1)
				if len(matrices[index]) == int(dimension[0]) and not matrix_a:
					print_matrix(matrices[index], index+1)
					sleep(1)
				else:
					print_matrix(matrices, 'B')

		return matrices
	return fill_rows(dimensions)

def main(matrix_a= None):
	if matrix_a:
		dimensions = generate_dimensions(f"{len(matrix_a)}x{len(matrix_a[0])}")
		matrix_b = generate_matrix(dimensions, matrix_a)
	else:
		dimensions = generate_dimensions()
		matrix_a,matrix_b = generate_matrix(dimensions)

	result = multiply(matrix_a, matrix_b).tolist()
	if result:
		print_matrix(matrix_a, matrix_b, result)
		is_continue = input("Reset / Continue  / Quit: ").lower()

		if 'continue' in is_continue:
			main(result)
		elif 'reset' in is_continue:
			main()