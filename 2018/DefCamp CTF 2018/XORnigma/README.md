# CTF: XORnigma
***Category: category***
>*Obtain the flag from the given file.*
## Solution
For this challenge, we are given the [source code](xornigma.py) to the cipher along with the resulting ciphertext.
```python
import itertools
def xor_two_str(s, key):
	key = key * (len(s) / len(key) + 1)
	return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in itertools.izip(s, key)) 

flag = "" 
flag_key = ""
x = xor_two_str(flag, flag_key)
print x.encode("hex")
# 000000003f2537257777312725266c24207062777027307574706672217a67747374642577263077777a3725762067747173377326716371272165722122677522746327743e
```
Here we see the cipher is doing a simple XOR cipher encrypted with a key. If we look at the ciphertext of the encoded string, we see it begins with `00000000`, which means both the flag and the key are the same for the first 4 bytes. Assuming the flag is in the standard flag format, we know the first four bytes will be `DCTF`. Unfortunately, we do not know if the key is longer than 4 bytes. However, we do know the next character should be `{`. Using this, we can do a quick check to see what the next character of the key is by XORing `{` with the next byte in the encoded string:
```python
chr(int('3f',16)^ord('{'))
```
We find out the next character in the key is `D`, so we can now safely assume the key is `DCTF`. I write a quick script to decrypt the rest of the string:
```python
enc = '000000003f2537257777312725266c24207062777027307574706672217a67747374642577263077777a3725762067747173377326716371272165722122677522746327743e'
key = 'DCTF'
flag = ''

for i in range(len(enc.decode('hex'))):
    flag += chr(ord(enc.decode('hex')[i])^ord(key[i%len(key)]))

print flag
```
And out comes the flag.

***Flag: `DCTF{fcc34eaae8bd3614dd30324e932770c3ed139cc2c3250c5b277cb14ea33f77a0}`***
