#PROJECT DESCRIPTION
#takes an input sentence, strips any trailing whitespace, and then splits the sentence into words using the space character as a delimiter.
#It returns the length of the last word in the input sentence.
#It retrieves the last word from the list of words obtained and computes its length using the len() function. 
#If the input sentence is empty or has no words after stripping, it returns 0.

def lengthh(s):
    words = s.rstrip().split()
    if not words:
        return 0
    
    return len(words[-1])
sent = input("enter a sentence: ")
result = lengthh(sent)
print("Length of the last word:", result)
