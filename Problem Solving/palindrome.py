num = "ABCBA"


def isPalindrome(some_input):
    """Check if an input is palindrome"""
    if some_input[::-1] == some_input:
        return ("Input is palindrome")
    else:
        return ("Input is not palindrome.")

print(isPalindrome(num))
