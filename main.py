from stats import get_num_words

def get_book_text(file_path):
    contents = None
    with open(file_path) as f:
        contents = f.read()
    return contents

def main():
    frankenstein_content = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(frankenstein_content)
    print(f"Found {num_words} total words")

main()