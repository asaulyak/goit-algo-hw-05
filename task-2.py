def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    counter = 0

    while low <= high:
        counter += 1

        mid = (high + low) // 2

        # Search for the case when we have only one element to pick from
        if low == high:
            result = mid if arr[mid] >= x else -1
            return counter, result

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid

        # We've found the element that equals x
        else:
            return counter, mid
