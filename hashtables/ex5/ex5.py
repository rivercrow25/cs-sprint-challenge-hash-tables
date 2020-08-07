# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    dct = {}
    results = []
    for i in range(len(files)):
        dct[i] = files[i]
        if i < len(queries):
            if queries[i] in dct[i]:
                results.append(dct[i])

    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
