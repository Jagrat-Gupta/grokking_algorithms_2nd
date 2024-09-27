def binary_search(arr: List[int], item : int) -> int :
    low : int = 0
    high : int = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif item > guess:
            low =  mid + 1
        else:
            high = mid - 1
    return None

my_list = [1,3,5,7,9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))