from stats import get_num_words, get_num_chars, get_sorted_dict
import sys

def get_book_text(file_path):
    contents = None
    with open(file_path) as f:
        contents = f.read()
    return contents

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    frankenstein_content = get_book_text(path_to_book)
    num_words = get_num_words(frankenstein_content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
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