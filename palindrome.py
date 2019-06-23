def mismatched_letters(l):
    mismatches = []
    for i in range(len(l)//2):
        if l[i] != l[len(l)-1-i]:
            mismatches.append(i)
    if len(mismatches) == 1:
        mismatches.append(len(l)//2)
    return mismatches

def get_one_of_original_palindrome(mismatches, l):
    response = ""
    letter1, letter2 = mismatches
    for i in range(len(l)):
        if i == letter1:
            response += l[letter2]
        elif i == letter2:
            response += l[letter1]
        else:
            response += l[i]
    return response

def get_original_palindrome(l):
    if l == l[::-1]:
        return(l)
    else:
        mismatches = mismatched_letters(l)
        return get_one_of_original_palindrome(mismatches, l)


print(get_original_palindrome("rtyrty"))
