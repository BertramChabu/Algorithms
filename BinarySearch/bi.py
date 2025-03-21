# The binary search function takes a sorted array and an item.
# If the item is in the aarray, the function returns its position.
# You keep track of what part of the array you have to search through.


# low = 0
# high = len(list) -1
# each time, you check the middle element

# mid = (low+high) /2
# guess = list[mid]

# guess < item:
    # low = mid +1

def binary_search(list, item):
    low = 0
    high = len(list) -1


    while low <= high:
        mid = (low + high)
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid +1
    return None


my_list = [1,3,5,7,9]

print(binary_search(my_list, 5))
print(binary_search(my_list, 2))
