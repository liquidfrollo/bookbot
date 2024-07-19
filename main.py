def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    #print(len(split(file_contents)))
    print(words(file_contents))

def split(args):
    words = args.split()
    return words

def words(args):
    charlist = {}
    for char in args:
        if char not in charlist:
            charlist[char] = 1
        else:
            charlist[char] += 1
    return charlist

main()
