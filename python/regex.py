'''
Given a simple regular expressions supporting:
- lowercase letters a-z
- a dot operator
- a star operator

Write a method that checks if the word matches a regex
'''

'''
A class representing a single regular expression token (letter, dot, or star)
'''
class Token():

    def __init__(self, char, is_star = False):
        if len(char) != 1:
            raise Exception()

        if char != '.' and (ord(char) < 97 or ord(char) > 122):
            raise Exception()

        self.char = char
        self.is_star = is_star

    def __str__(self):
        if self.is_star:
            return '*({0})'.format(self.char)
        return self.char

    def __repr__(self):
        return self.__str__()

    @property
    def is_char(self):
        return not self.is_star and self.char != '.'

    @property
    def is_dot(self):
        return self.char == '.' and not self.is_star

    def matches(self, char):
        return self.char == '.' or self.char == char

'''
Converts regex string into a list of tokens
'''
def tokenize(regex):
    result = []
    token = None

    for char in regex:
        if (char == '*'):
            if len(result) == 0:
                raise Exception()

            prev_token = result.pop()

            if prev_token.is_star:
                raise Exception()

            token = Token(prev_token.char, True)
        else:
            token = Token(char)

        result.append(token)

    return result

'''
Given a star token and a list of remaining tokens, check for match
'''
def match_star(star_token, tokens, word):
    i = 0

    while True:
        if match_here(tokens, word[i:]):
            return True

        char = word[i]
        i += 1
        if i > len(word) or not star_token.matches(char):
            return False

    return False

'''
Given a list of tokens and a string word check for match
'''
def match_here(tokens, word):
    if len(tokens) == 0:
        return len(word) == 0

    token = tokens[0]
    if token.is_star:
        return match_star(token, tokens[1:], word)

    if len(word) == 0:
        return False

    char = word[0]
    if token.matches(char):
        return match_here(tokens[1:], word[1:])

    return False

'''
Entry point, given a string regex and a string word, check for match
'''
def is_match(regex, word):
    tokens = tokenize(regex)
    return match_here(tokens, word)

print(is_match('a*ab', 'aaab'))
