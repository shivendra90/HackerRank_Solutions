if __name__ == '__main__':
    a = int(input())
    b = int(input())

    while a < 10**10:
        while b < 10**10:
            if a == int(a):
                if b == int(b):
                    add = a + b
                    sub = a - b
                    prod = a * b
                    break
                else:
                    print(ValueError("b is not an integer."))
                    break
            else:
                print(ValueError("a is not an integer."))
                break
        break

    print(add)
    print(sub)
    print(prod)            

