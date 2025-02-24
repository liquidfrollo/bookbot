from stats import get_num_words
from stats import sortedwords

def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    count=get_num_words(file_contents)
    sorted=sortedwords(file_contents)
    #print(words(file_contents))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document \n \n")

    #print(sorted)
    for letters in sorted:
        print(f"The '{letters['char']}' character was found {letters['num']} times")
    print("--- End report ---")


main()
