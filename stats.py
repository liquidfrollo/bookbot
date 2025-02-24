def get_num_words(args):
    count=len(split(args))
    return count

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
    #print(charlist)
    return charlist

def sortedwords(args):
    startlist = words(args)
    sortedlist = [{'char':k, 'num':v} for k, v in startlist.items()]

    sortedlist.sort(reverse=True, key=sort_on)

    return sortedlist

def sort_on(dict):
    return dict["num"]   