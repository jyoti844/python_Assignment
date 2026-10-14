
# Create a matrix
matrix = [
    [10, -5, 20],
    [15, -2, 30],
    [5, 25, -10]
]

print("Original Matrix:")
for row in matrix:
    print(row)

# 1. Remove negative numbers using filter()
print("\nMatrix without negative numbers:")
result = list(map(lambda row: list(filter(lambda x: x >= 0, row)), matrix))
for row in result:
    print(row)

# 2. Find squares using map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("\nSquares:", squares)

# 3. Filter even numbers using filter()
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# 4. Sort numbers using sorted()
sorted_numbers = sorted(numbers, reverse=True)
print("Sorted numbers:", sorted_numbers)

# 5. Sort tuples by second element
data = [(1, 30), (2, 10), (3, 20)]
sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted tuples:", sorted_data)

