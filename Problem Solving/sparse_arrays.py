def matchingStrings(stringList, queries):
    """
    Returns number of times a query matches an input.
    """
    # Write your code here
    res = []
    for inp in queries:
        recurring = 0
        for out in stringList:
            if inp == out:
                recurring += 1
        res.append(recurring)

    return res


if __name__ == '__main__':

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)
    print(res)
