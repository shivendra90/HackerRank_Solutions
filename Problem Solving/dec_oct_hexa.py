def print_formatted(number):
    width = len(str(bin(number)))  # Since the last column is always filled

    for i in range(1, number+1):
        print(str(i).rjust(width-2, '.') + 
                oct(i).lstrip("0o").rjust(width-1, '.') +
                hex(i).lstrip("0x").upper().rjust(width-1, '.') +
                bin(i).lstrip("0b").rjust(width-1, '.')
                )


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)

