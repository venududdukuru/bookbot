def get_book_text(book):
    with open(book) as f:
        text = f.read()
        return text


def word_count(content):
    words = content.split()
    return len(words)


def alpha_count(content):
    freq = {}
    for char in content.lower():
        if char.isalpha():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq


def book_report(path_to_file):
    content = get_book_text(path_to_file)
    wordcount = word_count(content)
    alphacount = alpha_count(content)

    print(f"--- Begin Report of {path_to_file} ---")
    print(f"{wordcount} words found in the document")
    print()
    sorted_alpha_count = sorted(alphacount.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_alpha_count:
        print(f"The '{char}' character was found {count} times")
    print(f"--- End Report ---")


def main():
    path_to_file = "books/frankenstein.txt"
    book_report(path_to_file)

main()
