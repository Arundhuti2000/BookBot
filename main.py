
from numpy import character


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words= text.split()
    return len(words)

def count_characters(text):
    character_freq = {}
    text = text.lower()
    for i in text:
        if i in character_freq:
            character_freq[i]+=1
        else:
            character_freq[i]=1
    return character_freq
    
def main():
    path_to_file = './books/frankenstein.txt'
    content = get_book_text(path_to_file)
    total_length = count_words(content)
    count_character = count_characters(content)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{total_length} words found in the document")
    for i in count_character:
        if not i.isalpha():
            continue
        else:
            print(f"The '{i}' character was found {count_character[i]}")
    print("--- End report ---")
    

if __name__ == "__main__":
    main()