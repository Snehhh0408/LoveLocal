#PROJECT DESCRIPTION
#function isPalindrome that checks if a string is a palindrome by comparing it to its reverse using slicing ([::-1])
#After finding the longest palindrome prefix, it separates the remaining characters (suffix) that are not part of the palindrome.
#Finally, it concatenates the prefix, the result of the recursive call (middle), and the suffix to form the shortest palindrome by adding characters in front of the given string.



def shortt_pal(s):
    def isPalindrome(string):
        return string == string[::-1]

    if not s:
        return ""

    i = 0
    for j in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
            i += 1

    if i == len(s):
        return s

    suffix = s[i:]
    prefix = suffix[::-1]
    middle = shortt_pal(s[:i])

    return prefix + middle + suffix

user_input = input("Enter a string: ")
result = shortt_pal(user_input)
print("Shortest palindrome:", result)
