'''
Given a list of characters output all possible strings of length l made of those characters
'''
def get_combinations(chars, max_l, current = ''):
    result = []

    for char in chars:
        #create a new string for every character
        added = current + char
        
        if len(added) < max_l:
            #if the length has not been reached yet, 
            #keep appending all possible character combinations to the new string
            result += get_combinations(chars, max_l, added)
        else:
            #if the length has been reached, just add the new string to the result
            result += [added]

    return result

'''
Given a list of characters output all subsets of the list
'''
def get_subsets(chars, result = []):
    if len(chars) == 1:
        #if there's only one character left, just append it to the result, and return it
        result += chars[0]
        return result

    #recursively call the function to get subsets of the remaining characters
    temp = get_subsets(chars[1:], result)
    l = len(temp)

    char = chars[0]

    #for all subsets returned by the recursive call,
    #prepend the current character to them, and append the new string to the result
    for i in range(l):
        temp += [char + temp[i]]

    #handle the subset being just one character
    temp += [char]

    return temp


print(get_combinations(['a','b','c'], 3))
print(get_subsets(['1','2','3']))
