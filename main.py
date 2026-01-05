
def get_book_text (file_path):
    with open(file_path) as f:
        return f.read() 

def get_num_words(text_content):
    num_words=len(text_content.split(sep=None))
    return num_words
    
def main(): 
    book_text=get_book_text ("books/frankenstein.txt")
    print(f"Found {get_num_words(book_text)} total words")
    return 


main() 