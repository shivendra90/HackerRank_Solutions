
def rotateLeft(d, array):
    """
    Rotates each element d times to the left.
    """
    to_shift = array[d:]
    
    return to_shift + array[:d] 


if __name__ == '__main__':
    n, d = map(int, input().split())
    array = list(map(int, input().split()))
    
    rotateLeft(d, array)
