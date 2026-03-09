# 1. Basic slices
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Basic slices:")
print(arr[2:5])      # output  [2, 3, 4]
print(arr[:4])       # output  [0, 1, 2, 3]
print(arr[6:])       # output  [6, 7, 8, 9]

# 2. Slicing with step
print("\nSlicing with step:")
print(arr[1:8:2])    # output  [1, 3, 5, 7]
print(arr[::3])      # output  [0, 3, 6, 9]

# 3. Negative indexing
print("\nNegative indexing:")
print(arr[-3:])      # output  [7, 8, 9]
print(arr[:-2])      # output  [0, 1, 2, 3, 4, 5, 6, 7]
print(arr[-5:-2])    # output  [5, 6, 7]

# 4. Reverse array using slicing
print("\nReverse array:")
print(arr[::-1])     # output  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 5. Modifying slices
print("\nModifying slices:")
arr[2:5] = [20, 30, 40]
print(arr)           # output  [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

arr[::2] = [100, 101, 102, 103, 104, 105]
print(arr)           # output  [100, 1, 101, 30, 102, 5, 103, 7, 104, 9]