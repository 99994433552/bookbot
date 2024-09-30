import re


def count_characters(content: str) -> dict:
    result: dict[str, int] = dict()

    lower_content = content.lower()

    for letter in lower_content:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1

    filtered_data = {
        key: value
        for key, value in result.items()
        if re.match(r"^[a-zA-Z]$", key)
    }

    sorted_data = dict(
        sorted(filtered_data.items(), key=lambda item: item[1], reverse=True)
    )

    return sorted_data


def count_words(content: str) -> int:
    return len(content.split())


def print_report(book_content: str):
    words = count_words(book_content)
    characters = count_characters(book_content)

    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"{words} words found in the document")
    for character in characters:
        print(
            f"The '{character}' character was found {characters[character]} times"
        )
    print("--- End report ---")


if __name__ == "__main__":
    with open("books/frankenstein.txt") as book:
        book_content = book.read()
        print_report(book_content)
