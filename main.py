def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    count=len(split(file_contents))
    sorted =sortedwords(file_contents)
    #print(words(file_contents))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document \n \n")

    for letters in sorted:
        print(f"The '{letters['char']}' character was found {letters['num']} times")
    print("--- End report ---")

def split(args):
    words = args.split()
    return words

def words(args):
    wordlist = args.lower()
    charlist = {}
    for char in wordlist:
        if char.isalpha():    
            if char not in charlist:
                charlist[char] = 1
            else:
                charlist[char] += 1

    return charlist

def sortedwords(args):
   
    startlist = words(args)
    sortedlist = [{'char':k, 'num':v} for k, v in startlist.items()]

    sortedlist.sort(reverse=True, key=sort_on)

    return sortedlist

def sort_on(dict):
    return dict["num"]


main()
