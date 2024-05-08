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
    print(chars_dict)
    

def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)

def get_chars_dict(file_contents):
    chars = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] =1
    return chars
        
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
if __name__ == '__main__':
    main()
