from stats import get_num_words, get_num_chars, get_sorted_dict
import sys

def get_book_text(file_path):
    contents = None
    with open(file_path) as f:
        contents = f.read()
    return contents

def main():
    frankenstein_content = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(frankenstein_content)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    num_chars = get_num_chars(frankenstein_content)
    sorted_num_chars = get_sorted_dict(num_chars)

    for dict in sorted_num_chars:
        if not dict["char"].isalpha():
            continue
        print(f"{dict["char"]}: {dict["num"]}")
    
    print("============= END ===============")

main()