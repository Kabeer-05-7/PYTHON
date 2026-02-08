# Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.
arr= [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = int(input("Enter the index:"))
arr.sort()
print(arr)
arr1 = arr[k-1]
print(arr1)



