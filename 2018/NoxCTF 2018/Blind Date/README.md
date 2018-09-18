

# NoxCTF 2018: Blind Date
***Category: Forensics***

> *My mom got me a date with someone! she sent me an image but i cannot open it. I don't want it to be a blind date. Can you help me?*

## Solution
For this challenge, we are given a file [BlindDate.jpeg](BlindDate.jpeg). We begin by trying to open the file, but it seems to be corrupt, So we try using some basic forensics commands to see what we are dealing with.

Running `file BlindDate.jpeg` gives us:

```
BlindDate.jpeg: data
```

So we try `strings BlindDate.jpeg`, which gives us:

```
fixEMM
kcuD
:pttsn//oda.c.ebx/mo1/pa
/0.px?<ekcaeb t=nig
"di "5W"=pM0MiheCerzHTNzSckzc?"d9<
>mx:xtempmx a:snla"=xebod:sn:atemx "/pmx:"=ktbodAMX eoC P5 erc-3. 1101.6666542 ,
1/2100/2041-6:65:  72    >"  <	
:fdr FDRnlmxdr:sh"=f:pttww//3w.wgro.991/20/9-22/-fdrtnysn-xa>"#s		
fdr<seD:pircnoitfdr oba:"=tumx ":snlMpmxh"=M:pttsn//oda.c.ebx/mo1/pam/0. "/mnlmx
ts:s=feRtth"//:pa.snebodmoc.pax/0.1/yTs/R/epuoseRecr"#felmx x:sn"=pmptthn//:da.s
.ebo/moc/pax/0.1mx ":MMpgirOlaniucoDtnem"=DI.pmx:didA9EC24F4BDD611ED4C68EA8F0646
85ABmx ":MMpucoDtnem"=DI.pmx:did44570CE6DEFC1E11DDFB97CDF34B982Dmx ":MMptsnIecna
"=DI.pmx:dii4457FBE6DEFC1E11DDFB97CDF34B982Dmx "rC:potaeooTrA"=lebodohP hsotC po
...
...
...
AiLg4CIg4CIK0AIgACIu4CIgACIgACIgACIu4CIgACIgACIgAiLu4CIgACIgACIgAiLKPgL
galftxt.
G3CX
galftxt.

```
Here, we can see some strange text appearing. We get long strings of printable ascii characters but none of the words are readable.
However, if we look a little closer, we see `galftxt.` at the end. It looks like `flag.txt` with the characters scrambled.
If we keep looking, the first line says `fixE` which looks like `Exif`. After seeing this, I run `xxd BlindDate.jpeg`. The first few lines give us this:
```
00000000: e0ff d8ff 464a 1000 0100 4649 6000 0101  ....FJ....FI`...
00000010: 0000 6000 2200 e1ff 6669 7845 4d4d 0000  ..`."...fixEMM..
00000020: 0000 2a00 0100 0800 0300 1201 0100 0000  ..*.............
00000030: 0000 0100 0000 0000 1100 ecff 6b63 7544  ............kcuD
00000040: 0001 0079 0000 0004 ff00 004b 687e 03e1  ...y.......Kh~..
00000050: 3a70 7474 736e 2f2f 6f64 612e 632e 6562  :pttsn//oda.c.eb
00000060: 782f 6d6f 312f 7061 002f 302e 7078 3f3c  x/mo1/pa./0.px?<
00000070: 656b 6361 6562 2074 3d6e 6967 bfbb ef22  ekcaeb t=nig..."
00000080: 6469 2022 3557 223d 704d 304d 6968 6543  di "5W"=pM0MiheC
00000090: 6572 7a48 544e 7a53 636b 7a63 3f22 6439  erzHTNzSckzc?"d9
```
In the first line, we see `FJ....FI`. This looks like `JFIF`, which is what we should be seeing for a `.jpeg` file.

The file header for a `.jpeg` should be:

`ffd8 ffe0 0010 4a46 4946 0001`

Instead, we see:

`e0ff d8ff 464a 1000 0100 4649`

We can see that the order of bytes is reversed for every four bytes, so I write a quick script to fix the file:
```python
with open('BlindDate.jpeg','rb') as f:
    data = f.read()
corrected = b''
for i in range(0, len(data), 4):
    corrected += data[i:i+4][::-1]

with open('corrected.jpeg','wb') as f:
    f.write(corrected)
```
After running the script, we get [corrected.jpeg](corrected.jpeg).  The file actually opens now, so we know were getting somewhere. Analyzing the file in `StegSolve`, we see there are 485 bytes of additional data in the file. After running `binwalk corrected.jpeg`, we can see there is a zip file containing `flag.txt` hidden within the image. Using `binwalk -e corrected.jpeg`, we extract an encrypted zip file, which accounts for the last 319 bytes of the file. However, we still have an extra 166 bytes of unexplained data. We can assume the extra bytes somehow give us the password to unzip the file.

The extra bytes in ascii gives us:
```
Li4gICAuICAuLiAgLi4gICAuICAuLiAgLi4gICAuICAuLiAgLiAgLi4NCi4gICAgLiAgIC4gICAgICAgLiAgICAgIC4gICAgLiAgIC4gIC4gIA0KICAgIC4uICAgICAgICAgIC4uICAgICAgLiAgIC4uICAgICAgLiAgLg
```
If we base64 decode this, we get:
```
..   .  ..  ..   .  ..  ..   .  ..  .  ..
.    .   .       .      .    .   .  .  
    ..          ..      .   ..      .  .
```
This looks like braille, which goes right along with the theme of the challenge, ***Blind*** Date. From this, we get the password to the zip file, `F4C3P4LM`. We open the `flag.txt` file which gives us:
```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++++++++++.+.+++++++++.<---.+++++++++++++++++.--------------.>+++.<+++++++++++++++++.<++++++++++++++++++.>>------.---------.--------.-----.++++++++++++++++++++++++++.<<.>>----.<++++++++.+++.>---------.<<+.>>++.<++.-----.+++++.<+++.>>++++++.<<-.>-----.<+.>.+++.>--------.<<---.>>++.<++.-----.+++++.<+++.>>++++++.<<-.++++++++++++.>>+++++++++.<<<++++++++++++++++++++++.
```
This is written in `Brainfuck`. After running this through an interpreter, we get: `noxCTF{W0uld_y0u_bl1nd_d4t3_4_bl1nd_d4t3?}` 

***Flag: `noxCTF{W0uld_y0u_bl1nd_d4t3_4_bl1nd_d4t3?}`***
