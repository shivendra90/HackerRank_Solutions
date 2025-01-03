import string


def print_rangoli(size):
    # your code goes here
    if size == 1:
        print('a')
    else:
        alp = string.ascii_lowercase
        hyphens = int(((size * 4) - 4) / 2)

        # Print the first line
        print("-" * hyphens + f"{alp[size - 1]}" + "-" * hyphens)
        hyphens -= 2

        for line in range(size - 2):
            print("-" * hyphens +
                  "-".join(alp[(size - 1):((size - 1) - line) - 2:-1]) +
                  "-" +
                  "-".join(alp[size - (line + 1):size]) +
                  "-" * hyphens)

            hyphens -= 2

        # Print central line
        print("-".join(alp[(size - 1)::-1]) + "-" + "-".join(alp[1:size]))

        # Reset hyphens
        hyphens = 2

        for line in range(size - 2):
            print("-" * hyphens +
                  "-".join(alp[(size - 1):line:-1]) +
                  "-" +
                  "-".join(alp[(line + 2):size]) +
                  "-" * hyphens)

            hyphens += 2

        # Print last line
        print("-" * hyphens + f"{alp[(size - 1)]}" + "-" * hyphens)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
