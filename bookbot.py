#!/usr/bin/env python3
import os

def main():

    quit_command = ["q", "quit", "exit", "stop", "cancel"]
    books_folder = "books/"
    books = os.listdir(books_folder)
    books.sort()
    book_list = print_books(books)

    print("\n[ Q --> EXIT ]")

    while True:
        choose_book = input("Pick your poison: ")

        if choose_book.lower() in quit_command:
            return

        for book in book_list:
            if choose_book == str(book["num"]) or choose_book == book["file"]:
                book_path = books_folder + book["file"]
                book_text = get_book_text(book_path)
                if book_text == None:
                    return
                word_count = count_words(book_text)
                chars_count = count_chars(book_text)
                generate_report(chars_count, word_count, book_path)
                return

def get_book_text(book_path):
    try:
        with open(book_path) as file:
            return file.read()
    except:
        print("""
Can't read this file.
Try to change format or encoding.
""")
        return None

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
--- Begin report of {book_path[6:]} ---
{words_count} words found in the document
""")
    
    for line in report_list:
        if not line["char"].isalpha():
            continue
        print(f"The \'{line["char"]}\' character was found {line["num"]} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def print_books(books):
    book_list = []
    
    for file in books:
        book_list.append({"num": books.index(file), "file": file})
    book_list.sort(key=sort_on)

    print()

    for p in book_list:
        print(p["num"], p["file"])

    return book_list

main()