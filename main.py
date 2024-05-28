def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    num_words = count_words(book_text)
    num_per_char = count_per_letter(book_text)
    list_of_dicts = convert_dict_to_list(num_per_char)
    print_report(book_path, num_words, list_of_dicts)

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def split_text(text):
    text_split = text.split()
    return text_split

def count_words(text):
    split_text = text.split()
    words = 0
    for word in split_text:
        words += 1
    return words

def count_per_letter(text):
    lowered_text = text.lower()
    chars_count = {}
    for char in lowered_text:
        if char in chars_count:
            chars_count[char] += 1
        elif char.isalpha():
            chars_count[char] = 1
    return chars_count

def convert_dict_to_list(dict):
    list_of_dicts = []
    for a in dict:
        letter_dict = {"letter": "", "count": 0}
        letter_dict["letter"] = a
        letter_dict["count"] = dict[a]
        list_of_dicts.append(letter_dict)
    return list_of_dicts
        
def print_report(book_path, word_count, letter_count):
    letter_count.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print (f"{word_count} words found in the document")
    print("")
    for dict in letter_count:
        letter = dict["letter"]
        count = dict["count"]
        print(f"The '{letter}' character was found {count} times")
    return

def sort_on(dict):
    return dict["count"]


main()
