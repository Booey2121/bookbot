frankenstein_path = "books/frankenstein.txt"


def main():
    # print(get_book(frankenstein_path))
    print(f"{get_word_count(frankenstein_path)} words found in the document")
    # print(get_character_count(frankenstein_path))
    print_summary(get_character_count(frankenstein_path))


def get_book(path):
    with open(path) as f:
        frankenstein = f.read()
        return frankenstein


def get_word_count(path):
    words = get_book(path).split()
    return len(words)


def get_character_count(path):
    characters = get_book(path).lower()
    output = {}
    for character in characters:
        if character.isalpha():
            if character not in output:
                output[character] = 1

            else:
                output[character] = output[character] + 1

    # output looks like {"a": 5, "b": 10, "c": 9}
    # make it like this:
    # [{"name": "a", "num": 5}, {"name": "b", "num": 10}, {"name": "c", "num": 9}]

    new_list_dict = []

    for letter in output:
        letter_dict = {"name": letter, "num": output[letter]}
        new_list_dict.append(letter_dict)

    return new_list_dict


def print_summary(character_list):
    character_list.sort(reverse=True, key=sort_on)
    # "The 'name' character was found 'num' times"

    for result in character_list:
        name = result["name"]
        num = result["num"]

        print(f"The '{name}' character was found {num} times")


def sort_on(dict):
    return dict["num"]




main()
