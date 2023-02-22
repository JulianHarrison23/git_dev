#!/usr/bin/env python3
"""
program_name.py
*insert description*
"""

__author__ = "Julian Harrison"
__version__ = "insert date"

from atds import Deque

class PalindromeChecker(object):
        def __init__(self):
            self.strict = False
        
        def setStrictMode(self, y):
            if(y):
                self.strict = True
            else:
                self.strict = False

        def isPalindrome(self,phrase):
            nphrase = phrase
            if not self.strict:
                nphrase = self.sanitize(phrase)
            d = Deque()
            for i in range(len(nphrase)):
                d.addRear(nphrase[i])
            while d.size()>1:
                if d.removeFront() != d.removeRear():
                    return False
                return True
                
        
        def sanitize(self, phrase):
            phrase = phrase.lower()
            new = ""
            for i in range(len(phrase)-1):
                if phrase[i] in 'abcdefghijklmnopqrstuvwxyz':
                    new += phrase[i]
            return new


def main():
    p = PalindromeChecker()
    print("Palindrome Checker!")
    strict = input("Do you want strict mode 1) on, or 2) off? --> ")
    if (strict == "1"):
        p.setStrictMode("True")
    phrase = input("Phrase: ")
    print("Palindrome?: " + str(p.isPalindrome(phrase)))


if __name__ == "__main__":
    main()