def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    num_chars = {}
    for char in text:
        lowcase_char = char.lower()
        if lowcase_char in num_chars:
            num_chars[lowcase_char] += 1
        else:
            num_chars[lowcase_char] = 1
    return num_chars