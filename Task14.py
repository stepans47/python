def isLetterVowel(letter):
    vowels = ['a','e','i','o','u']
    return letter in vowels

def isLetterConsonant(letter):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y', 'z']
    return letter in consonants


print('Enter one letter:')
letter = input()

if(isLetterVowel(letter.lower())):
    print(letter + ' - letter is vowel')
elif(isLetterConsonant(letter.lower())):
    print(letter + ' - letter is consonant')
else:
    print(letter + ' - is not a letter')
