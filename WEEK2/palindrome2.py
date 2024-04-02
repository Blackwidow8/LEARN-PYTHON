def find_palindromes_in_text(text):
    normalized_text = ''.join(c for c in text.lower() if c.isalnum() or c.isspace()).split()
    palindromes = []

    def is_palindrome_seq(words_seq):
        seq = ''.join(words_seq)
        return seq == seq[::-1]

    for start_idx in range(len(normalized_text)):
        for end_idx in range(start_idx + 1, len(normalized_text) + 1):
            word_sequence = normalized_text[start_idx:end_idx]
            if is_palindrome_seq(word_sequence) and len(word_sequence) > 1:
                palindrome_phrase = ' '.join(word_sequence)
                if palindrome_phrase not in palindromes:
                    palindromes.append(palindrome_phrase)

    return palindromes

# Extract palindromes from the story
with open("story.txt", "r") as story:
    story_text = story.read()
    extracted_palindromes = find_palindromes_in_text(story_text)

print(extracted_palindromes)
