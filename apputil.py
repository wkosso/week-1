

# add code below ...

##Question 1
def palindrome(word):
    '''
    A function that return's true if the word meets the palindrome requirements else return false.
    '''
    clean_word = word.lower().replace(" ", "").replace(",", "").replace(".", "")
    reversed_word = clean_word[::-1]
    
    if clean_word == reversed_word:
        result = True
    else:
        result = False
    
    return result


##Question 2

def parentheses(sequence):
    '''
    This function goes through sequence character by character in a for loop and returns the result either true or false.
    '''
    balance = 0
    
    for char in sequence:
        if char == "(":
            balance = balance + 1
        else:
            balance = balance - 1
            if balance < 0:
                return False
    
    if balance == 0:
        return True
    else:
        return False
