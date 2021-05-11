def print_upper_words(words, must_start_with):
    """Prints each word from a list in uppercase if it starts with a specified letter"""

    for word in words:
        upper_word = word.upper()
        for letter in must_start_with:
            upper_letter = letter.upper()
            if upper_word.startswith(upper_letter):
                print(upper_word)

print_upper_words(['hi', 'how', 'are', 'you'], {"h", "y"})