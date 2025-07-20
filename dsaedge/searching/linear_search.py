def Linear_Search(arr, target):
    """
    Performs a linear search to find the index of a target in an array.
    Works on both sorted and unsorted lists.
    Returns the index of the target if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1