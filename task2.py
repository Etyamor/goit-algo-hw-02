from collections import deque


def is_palindrome(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    char_deque = deque(cleaned_string)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


input_string = "А роза упала на лапу Азора"
if is_palindrome(input_string):
    print(f"'{input_string}' є паліндромом.")
else:
    print(f"'{input_string}' не є паліндромом.")
