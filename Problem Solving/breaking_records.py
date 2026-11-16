import os

def breakingRecords(scores):
    """
    Returns a pair of high and low scores
    """
    # Convert to unique scores to avoid duplicates
    scores = list(dict.fromkeys(scores))

    wins, losses = 0, 0
    
    try:
        high_score, low_score = scores[0], scores[0]
        for score in scores[1:]:
            if score > high_score:
                wins += 1
                high_score = score
            
            elif score < high_score and score < low_score:
                losses += 1
                low_score = score
            
            else:
                continue

    except IndexError as e:
        print("Empty list instantiated")
    
    return wins, losses


# Examples
l1 = [10,5,20,20,4,5,2,25,1]
l2 = [3,4,21,36,10,28,35,5,24,42]
print(breakingRecords(l1))
print(breakingRecords(l2))

if __name__ == '__main__':
    fptr = open(os.environ["OUTPUT_PATH"], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


