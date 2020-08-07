def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dct = {}
    for i in range(length):
        dct[weights[i]] = i

    for (cur, n) in enumerate(dct):
        compliment = limit - n

        if dct.get(compliment):
            index = dct[compliment]
            return (index, cur)

    return None


array = [1, 12, 456, 4, 0, 6, 32, 467, 9]
length = len(array)
limit = 7
print(get_indices_of_item_weights(array, length, limit))
