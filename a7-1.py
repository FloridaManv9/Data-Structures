"""
File: a7.py

"""

from stack import Stack

def replaceIt(string_input):
    return string_input.replace(" ", "")

def isPalindrome(sentence):
    """Returns True if sentence is a palindrome
    or False otherwise."""
    stk = Stack()  # Creates a stack called stk.

    for char in sentence:
        if char.isalpha():
            stk.push(char)

    sentence = replaceIt(sentence)


    list1 = ""
    while not stk.isEmpty():
        x = stk.peek()

        if x.isalpha():
            list1 += stk.pop()
        else:
            stk.pop()

    if (list1 == sentence):
        return True
    else:
        return False

# *** Do not modify main() ***
def main():
    while True:
        sentence = input("Enter some text or just hit Enter to quit: ")
        if sentence == "":
            break
        elif isPalindrome(sentence):
            print("It's a palindrome.")
        else:
            print("It's not a palindrome.")


main()
