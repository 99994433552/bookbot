print("hello world")

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = len(file_contents.split())
    letters = {}
    for letter in file_contents.lower():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")

    letters_list = [letter for letter in list(letters.keys()) if letter.isalpha()]
    letters_list.sort()
    for letter in letters_list:
        print(f"The '{letter}' character was found {letters[letter]} times")
    print("\n--- End report of books/frankenstein.txt ---")
