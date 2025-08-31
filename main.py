def get_book_text(file_path):
    try:
        with open(file_path) as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
def count_words(text):
    words= text.split()
    return len(words)
def main():
    print ("Enter the book file path: ")
    file_path = "books/frankenstein.txt"
    book= get_book_text(file_path)
    print(book)
    print("--------------------")
    print(f"{count_words(book)} words found in the document")
if __name__ == "__main__":
    main()