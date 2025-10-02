# Linear Search Algorithm
# arr = [5, 3, 8, 4, 2]
# x = 8
# y = -1

# for i in range(len(arr)):
#     print(f"Checking index {i}: value {arr[i]}")
#     if arr[i] == x:
#         y = i
#         break

# print(f"Element is present at index: {y}")


# Binary Search Algorithm
# arr = [2, 3, 4, 5, 8]
# x = 4
# y = -1

# low = 0
# high = len(arr) - 1

# while low <= high:
#     mid = low + (high - low) // 2
#     print(f"Checking index {mid}, {arr[mid]}")
    
#     if arr[mid] == x:
#         y = mid
#         break
#     elif arr[mid] < x:
#         low = mid + 1
#     else:
#         high = mid - 1

# if y != -1:
#     print(f"Element {x} found at index: {y}")
# else:
#     print(f"Element {x} not found")