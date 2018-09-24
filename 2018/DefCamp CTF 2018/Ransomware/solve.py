with open('youfool!.exe','rb') as f:
    enc = f.read()

key = b':P-@u\x1aL"Y1K$[X)fg[|".45Yq9i>eV)<0C:(\'q4n\x02[hGd\x2fEeX+\xbc7,2O"+:[w'
dec = ''
for i in range(len(enc)):
    dec += chr(ord(enc[i]) ^ ord(key[i%len(key)]))
