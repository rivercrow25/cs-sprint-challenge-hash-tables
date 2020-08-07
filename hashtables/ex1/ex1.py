def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dct = {}
    reversed = {}
    for i in range(length):
        dct[i] = weights[i]
        reversed[length - i-1] = weights[i]
    return dct


array = [1, 12, 456, 4, 0, 6, 32, 467, 9]
length = len(array)
limit = 7
print(get_indices_of_item_weights(array, length, limit))
