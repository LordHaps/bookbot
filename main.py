def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    chars_count = count_chars(book_text)
    generate_report(chars_count, word_count, book_path)

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_chars(book_text):
    chars = {}
    for char in book_text.lower():
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def generate_report(chars_count, words_count, book_path):
    report_list = []
    
    for char in chars_count:
            report_list.append({"char": char, "num": chars_count[char]})
    report_list.sort(reverse=True, key=sort_on)
    
    print(f"""
--- Begin report of {book_path} ---
{words_count} words found in the document
""")
    
    for line in report_list:
        if not line["char"].isalpha():
            continue
        print(f"The \'{line["char"]}\' character was found {line["num"]} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

main()