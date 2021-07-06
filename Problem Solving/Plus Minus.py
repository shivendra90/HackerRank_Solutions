def plusMinus(arr):
    """
    Takes in an array and finds out
    propertion of positive,
    negative integers as well as zeros.
    """
    negs = [i for i in arr if i < 0]
    pos = [i for i in arr if i > 0]
    zeros = [i for i in arr if i == 0]
    
    print("%.6f" % (len(pos)/len(arr)))
    print("%.6f" % (len(negs)/len(arr)))
    print("%.6f" % (len(zeros)/len(arr)))
    
