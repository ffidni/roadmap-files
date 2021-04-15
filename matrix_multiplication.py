from os import system
from time import sleep


def matrix_multiplication(matrices, dimensions):
	defined_matrices = []
	for index, dimension in enumerate(dimensions):
		if (index+1 < len(dimensions) and index-1 >= 0):
			prev = dimensions[index-1]
			current = dimension
			next = dimensions[index+1]

			if current[-1] == next[-1]:
				defined_matrices[index].append()

def print_matrix(matrix, index):
	CLEAR_SCREEN()
	print(f"Matrix {index} has been created:")
	for rows in matrix:
		for cols in rows:
			print(f"\t{cols}\n")


def generate_matrix(n, dimensions):
	matrices = [[] for rows in range(n)]
	for index, dimension in enumerate(dimensions):
		for rows in range(int(dimension[0])):
			matrices[index].append([[int(input("Input a number: ")) for cols in range(int(dimension[-1]))]])
			if len(matrices[index]) == int(dimension[0]):
				print_matrix(matrices[index], index+1)

	return matrices


if __name__ == '__main__':
	CLEAR_SCREEN = lambda: system('cls')
	n_matrices = int(input("Input the number of matrices: "))
	print("Dimensions format, i.g -> 2x3")
	dimensions = [input(f"Input the dimension for matrix {num}: ") for num in range(1, n+1)]
	matrices = generate_matrix(n_matrices, dimensions)
	print(matrix_multiplication(matrices, dimensions))
	
