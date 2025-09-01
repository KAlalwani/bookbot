from stats import count_words
from stats import count_char
from stats import dict_to_list
import sys
def get_book_text(file_path):
    try:
        with open(file_path) as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
    book= get_book_text(file_path)
    print(book)
    print("--------------------")
    print(f"Found {count_words(book)} total words")
    print("--------------------")
    def sort_on(item):
        return item["num"] 
    char_list=dict_to_list(count_char(book))
    char_list.sort(reverse=True, key=sort_on)
    for char in char_list:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
if __name__ == "__main__":
    main()