word = input("Enter a word: ")
word = word.lower()
reversed_word = word[::-1]

if word == reversed_word:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")