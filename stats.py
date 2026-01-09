def get_num_words(text_content):
    num_words=len(text_content.split(sep=None))
    return num_words

def char_counter(text_content):
    char_counts = {}
    for text in text_content:
        if text.lower() in char_counts:
            char_counts[text.lower()] += 1 
        else:
            char_counts[text.lower()] = 1
        
    return char_counts

def char_sort(char_dict):
    char_lst = []
    for char, count in char_dict.items():
        char_lst.append({"char": char, "num": count})
    char_lst.sort(reverse=True, key=sort_on)
    return char_lst

def sort_on(item):
    return item["num"]