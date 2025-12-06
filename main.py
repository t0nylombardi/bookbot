import sys
from stats import *


def get_book_text(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def print_sorted_unique_chars(text):
    unique_chars = count_unique_chars(text)
    for char, count in unique_chars:
        print(f"{char}: {count}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print_sorted_unique_chars(text)


main()
