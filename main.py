
import sys

from stats import get_num_words, char_counter, char_sort

def get_book_text (file_path):
    with open(file_path) as f:
        return f.read()
    
def main(): 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")   
    book_text=get_book_text(sys.argv[1])

    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")

    print("--------- Character Count -------")
    char_counts=char_counter(book_text)
    char_dict=char_sort(char_counts)

    for item in char_dict:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")
        
    print("============= END ===============")
    return 


main() 