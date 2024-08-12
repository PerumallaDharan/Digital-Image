# Q14) Write a Python program to identify unique triplets whose three elements sum 
# to zero from an array of n integers.

def find_zero_sum_triplets(arr):
    arr.sort()
    n = len(arr)
    triplets = set()

    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                triplets.add((arr[i], arr[left], arr[right]))
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return list(triplets)

# Example usage
array = [-1, 0, 1, 2, -1, -4]
unique_triplets = find_zero_sum_triplets(array)
print("Unique triplets that sum to zero:")
for triplet in unique_triplets:
    print(triplet)
