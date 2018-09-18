with open('BlindDate.jpeg','rb') as f:
    data = f.read()
corrected = b''
for i in range(0, len(data), 4):
    corrected += data[i:i+4][::-1]

with open('corrected.jpeg','wb') as f:
    f.write(corrected)
