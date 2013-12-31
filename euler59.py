import glob
dictionary = []
cipher = []
keys = []
alphanum = range(65,91)
alphanum.extend(range(97,123))
def loadDictionary():
    filenames = glob.glob('scowl-7.1/final/english-words.*')
    for filename in filenames:
        f = open(filename)
        dictionary.extend([x.strip() for x in f.readlines()])
def loadCipher():
    cipher = [int(x) for x in open('cipher1.txt').readline().split(',')]
    return cipher
def makeKeys():
    a = [x for x in range(97, 123)]
    keys = [[x,y,z] for z in a for y in a for x in a]
    return keys
def go():
    loadDictionary()
    cipher = loadCipher()
    keys = makeKeys()
    last_first_two = []
    words_found = 0
    for key in keys:
        this_first_two = [chr(x) for x in key[1:3]]
        if not last_first_two == this_first_two:
            print [chr(x) for x in key] 
        last_first_two = this_first_two
        text = ''
        last_word = ''
        for i in range(0, len(cipher)):
            this_letter = (cipher[i]^key[i%3])
            if this_letter in alphanum:
                last_word=last_word+chr(this_letter)
                text= text+chr(this_letter)
            else:
                if last_word.lower() in dictionary or last_word=='':
                    text = text+chr(this_letter)
                    if not last_word=='' and len(text)>15:
                        print text 
                        a = raw_input('1 if correct')
                        if not a=='':
                            break;
                    last_word = ''
                else:
                    text = ''
                    break
        if not text=='':
            print text
            print key
            break
loadDictionary()
cipher = loadCipher()
keys = makeKeys()
last_first_two = []
key =[103,111,100]
unciphered =0 
text=''
for i in range(0, len(cipher)):
    this_letter = cipher[i]^key[i%3]
    unciphered+=this_letter
    text+=chr(this_letter)
print text
print unciphered
