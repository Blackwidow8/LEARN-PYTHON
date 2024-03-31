import string

palindromes = set()


def isPalindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

with open("story.txt", mode="r") as story:
    splitted_words = story.read().split()

    for word in splitted_words:
        converted_word = word.strip(string.punctuation).lower()

        if isPalindrome(converted_word):
            palindromes.add(converted_word)

print(palindromes)
import string
sentence =  "he continued to roam the Enchanted Fores"

sentence_list = sentence.split()

final_list = list()

for word in sentence_list:
    remove_punctuations = word.strip(string.punctuation).lower()

    final_list.append(remove_punctuations)


new_palindrome_string = ''.join(final_list)
print(sentence)
print(new_palindrome_string)
if new_palindrome_string == new_palindrome_string[::-1]:
    print("The String is a Palindrome")
else:
    print("The string is not a Palindrome")