def main(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def word_count(book):
    words = book.split()
    word_count = len(words)
    print(f"{word_count}  words found in the document")

def character_count(book):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    characters = {}
    lower = book.lower()
    for i in lower:
        if i in alphabet:
            if i not in characters:
                characters[i] = 1
            else:
                characters[i] += 1
    for i in characters:
        print(f"the '{i}' was found {characters[i]} times")


books = "books/frankenstein.txt"
print(f"--- Begin report of {books} ---")
story = main(books)
word_count(story)
character_count(story)
print("--- End report ---")
