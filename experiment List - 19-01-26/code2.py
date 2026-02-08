# You are given an integer array arr[]. You need to find the maximum sum of a sub array (containing at least one element) in the array arr[].
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = arr[0]
for i in range(len(arr)):
    current_sum = 0
    for j in range(i, len(arr)):
        current_sum += arr[j]
        if current_sum > max_sum:
            max_sum = current_sum
print(max_sum)
