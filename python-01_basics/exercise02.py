import string

vowel_string = 'aeiouAEIOU'

def is_vowel(s):
    return s in vowel_string


def is_consonant(s):
    return s.isalpha() and not is_vowel(s)


def print_string_ascii_uppercase() :
    for ch in string.ascii_uppercase:
        print(ch)


def print_words(string_example):
    for word in string_example.split():
        print(word)


string_example = "This is a great thing"
print_words(string_example)
print(is_vowel('aeiou'))
print(is_vowel('123'))
print(is_consonant('1'))

print_string_ascii_uppercase()

print('1'*20)
print(1*20)

print('test' > 'test1')
print('test' == 'test')