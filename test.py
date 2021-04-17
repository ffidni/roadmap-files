from time import sleep

def process(arr):
    for index,element in enumerate(arr):
        print(arr[index])
        for i in range(index):
            print(f"Previous: {arr[i]}")

if __name__ == '__main__':
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    process(arr)