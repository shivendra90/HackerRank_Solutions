if __name__ == '__main__':
    n = int(input())
    marksheet = {}
    total_score = 0.00
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        marksheet[name] = scores
    query_name = input()
    for student, scores in marksheet.items():
        if query_name == student:
            for items in scores:
                total_score += items
    
    print("{0:.2f}".format(total_score/3))
