def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    num_words = count_words(book_text)
    print (f"There are {num_words} words in the book")

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        text_split = file_contents.split()
        return text_split

def count_words(text):
    words = 0
    for word in text:
        words += 1
    return words

main()
