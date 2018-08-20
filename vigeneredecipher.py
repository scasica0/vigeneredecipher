

def decipher(text,key): #decrypts an alphabetic character: Original = (Encrypted - Key) % 26
    if text.isalpha() == True:
        if text.islower() == True:
            new_letter = ((ord(text) - ord('a')) - (ord(key) - ord('a'))) % 26
            new_letter += ord('a')
            return chr(new_letter)
        else:
            new_letter = ((ord(text) - ord('A')) - (ord(key) - ord('a'))) % 26
            new_letter += ord('A')
            return chr(new_letter)
    else:
        return text

import sys

#imports key
key = sys.argv [2] 

#imports text inside file
with open(sys.argv[1], 'r') as fin: 
    file_text = fin.read()

#makes the length of key at least as long as the text to be encrypted
while len(key) < len(file_text):
    key+=key

#aligns key with text by inserting spaces and skipping non-alphabetic characters
new_key = ''
i = 0
for c in range(len(file_text)): 
    text = file_text[c]
    if text.isalpha() == True:
        new_key += key[i]
        i +=1
    else:
        new_key += ' '

#traverses and decrypts each character of the encrypted text 
decrypted_text = ''
for c in range(len(file_text)):
    decrypted_text += decipher(file_text[c], new_key[c])

#outputs decrypted text to new 'FILENAME-clear.txt' where 'FILENAME' is the name of the original file
newfile = sys.argv[1]
newfile = newfile[:4] + '-clear.txt'
with open(newfile, 'w') as fout:
    fout.write(decrypted_text) 

