if __name__ == '__main__':
    string = str(input())


    methods = [".isalnum()", ".isalpha()", ".isdigit()",
                ".islower()", ".isupper()"]

    for i, method in enumerate(methods):
        print(eval("any(alpha{0} for alpha in string)".format(method)))
