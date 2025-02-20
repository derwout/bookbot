def main():
    text = get_book_text()
    lowercase_text = text.lower()
    # word_count = get_word_count(text)
    # print(word_count)
    character_count = count_characters(lowercase_text)
    alphabet_characters = filter_alphabet(character_count)
    list_characters(alphabet_characters)

def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    dict = {}
    for character in text:
        if character in dict:
            dict[character] += 1
        else:
            dict[character] = 1
    return dict

def list_characters(character_count):
    for character in character_count:
        print(f"The '{character}' character was found {character_count[character]} times")

def filter_alphabet(dict):
    filtered_dict = {}
    alphabet = list(map(chr, range(97, 123)))
    for i in alphabet:
        if i in dict:
            filtered_dict[i] = dict[i]
    return filtered_dict


main()