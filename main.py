# Main information that all application is derived from
#split python file into three functions 1. main function to establish the data path along with putting together returned values to create desired outcome 2. get_num_words function is to give word count 
# 3. get_book_text to open data and return the words in general to be utilized in main
# 4. Added f string with more text to look more professional in output

def main():
    book_path= "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    num_words = get_num_words(file_contents)
    chars_dict = get_chars_dict(file_contents)
    print(f"{num_words} words found in the document")
    
    for char_info in chars_dict:
        print(f"There are {char_info['num']} of '{char_info['name']}' inside this passage!")
    

def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)

def sort_on(dict):
    return dict["num"]


def get_chars_dict(file_contents):
    char_counts = {}
    for c in file_contents.lower():
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] =1

    # Convert the dictionary to a list of dictionaries
    chars = [{"name": char, "num": count} for char, count in char_counts.items()]
    # Sort the list of dictionaries using the sort_on function
    chars.sort(reverse=True, key = sort_on)
    return chars
        
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
if __name__ == '__main__':
    main()
