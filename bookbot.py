# Main function for executing the program
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    # Write out text to console
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document.")
    print()
    
    for index in chars_sorted_list:
        print(f"The '{index['char']}' character was found {index['num']} times.")
        
    print("--- End of report ---")


# Function for opening a book
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
 

# Function for number of words
def get_num_words(text):
    words = text.split()
    return len(words)

# Creating the dictionary of characters + number of occurrences
def get_chars_dict(text):
    chars_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars_dict:
                chars_dict[lowered] += 1
            else:
                chars_dict[lowered] = 1
    return chars_dict


# Sort function
def sort_on(d):
    return d["num"]


# Get sorted list from characters dictionary
def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for ch in chars_dict:
        sorted_list.append({"char": ch, "num": chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()