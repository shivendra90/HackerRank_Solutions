if __name__ == '__main__':

    arr = []
    score_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        arr += [[name, score]]
        score_list += [score]

    mid_score = sorted(list(set(score_list)))[1]

    for student, score in sorted(arr):
        if score==mid_score:
            print(student)
