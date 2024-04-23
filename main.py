import os

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path}---")
    print(f"{num_words} words found in the document\n")
    chars_dict = get_num_letters(text)
    list_of_chars_dict = convert_dict_to_sorted_list(chars_dict)
    
    for item in list_of_chars_dict:
        print(f"The '{item["letter"]}' character was found {item["num"]} times")
    print(f"--- End report ---")

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_num_letters(text):
    lower_text = text.lower()
    lower_letters_dict = list_to_dict(get_lower_case_letters_list())
    for char in lower_text:
        # lower_letters_dict[char] = lower_letters_dict.get(char, 0) + 1
        if lower_letters_dict.get(char, None) is not None:
            lower_letters_dict[char] += 1
    return lower_letters_dict

def get_lower_case_letters_list():
    return [chr(i) for i in range(97,123)]

def list_to_dict(list):
    return dict.fromkeys(list, 0)

def sort_on(dict):
    return dict["num"]

def convert_dict_to_sorted_list(input_dict):
    result_lst = []
    for key, value in input_dict.items():
        result_lst.append(dict({"letter": key, "num": value}))
    result_lst.sort(reverse=True, key=sort_on)
    return result_lst

# def get_chars_dict(text):
#     chars = {}
#     for char in text:
#         lowered= char.lower()
#         if lowered in chars:
#             chars[lowered] += 1
#         else:
#             chars[lowered] = 1
#     return chars

main()
