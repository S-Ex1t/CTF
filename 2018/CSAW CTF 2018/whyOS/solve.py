import re
with open('console.log','r') as f:
    data = [i.strip() for i in f]

matches = []
for i in data:
    tmp = i.split(' ')
    if re.match('^[a-f0-9]{32,}$',tmp[-1],re.I):
            matches.append(i)

#for i in matches:
#    print i

print "Flag:", matches[-1].split(' ')[-1]
