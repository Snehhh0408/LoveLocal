# LoveLocal
def lengthh(s):
    words = s.rstrip().split()
    if not words:
        return 0
    
    return len(words[-1])
sent = input("enter a sentence: ")
result = lengthh(sent)
print("Length of the last word:", result)
