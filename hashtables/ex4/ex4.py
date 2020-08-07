def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    positive = {}
    negative = {}
    for i in range(len(a)):
        if a[i] > 0:
            positive[a[i]] = a[i]
        elif a[i] < 0:
            negative[a[i]] = a[i]
    for key in positive:
        if negative.get(key * -1):
            result.append(positive[key])
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
