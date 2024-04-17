import numpy as np

# Generate a random 2-dimensional numpy array with dimensions 5x5.
array = np.random.randint(1, 10, size=(5, 5), dtype=int)

if __name__ == '__main__':
    print(f"Entire array:\n{array}")
    print(f"\nNumber from the 2nd row, 3rd column: {array[1, 2]}")
    print(f"\nSum of all array elements: {np.sum(array)}")
    print(f"\nMean of each row in the array: {np.mean(array, axis=1)}")
    print(f"\nMaximum value in each column: {np.max(array, axis=0)}")
