# Rewind
***Category: Forensics***
>Sometimes you have to look back and replay what has been done right and wrong
---
For this challenge, we are given a file `rewind.tar.gz`.

We begin by extracting the contents using `tar -xzf rewind.tar.gz`. We are given two files: `rewind-rr-snp` and `rewind-rr-nodent.log`. We then run our basic recon commands such as `file`, `strings`, and `binwalk` on the files to see what we are dealing with.

Both of the files were pretty big so `strings` returned a lot of results for each of them. However, while running `strings` on `rewind-rr-snp`, I thought I saw the words `flag` fly across the screen, so I searched for the standard flag format with `strings rewind-rr-snp | grep flag{` which returned:
```
while [ true ]; do printf "flag{FAKE_FLAG_IS_ALWAYS_GOOD}" | ./a.out; done
while [ true ]; do printf "flag{FAKE_FLAG_IS_ALWAYS_GOOD}" | ./a.out; done
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
^[[Aflag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
^[[Aflag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
while [ true ]; do printf "flag{FAKE_FLAG_IS_ALWAYS_GOOD}" | ./a.out; done
while [ true ]; do printf "flag{FAKE_FLAG_IS_ALWAYS_GOOD}" | ./a.out; done
while [ true ]; do printf "flag{FAKE_FLAG_IS_ALWAYS_GOOD}" | ./a.out; done
while [ true ]; do printf "flag{FAKE_FLAG_IS_ALWAYS_GOOD}" | ./a.out; done
while [ true ]; do printf "flag{FAKE_FLAG_IS_ALWAYS_GOOD}" | ./a.out; done
while [ true ]; do printf "flag{FAKE_FLAG_IS_ALWAYS_GOOD}" | ./a.out; done
while [ true ]; do printf "flag{FAKE_FLAG_IS_ALWAYS_GOOD}" | ./a.out; done
while [ true ]; do printf "flag{FAKE_FLAG_IS_ALWAYS_GOOD}" | ./a.out; done
while [ true ]; do printf "flag{FAKE_FLAG_IS_ALWAYS_GOOD}" | ./a.out; done
while [ true ]; do printf "flag{FAKE_FLAG_IS_ALWAYS_GOOD}" | ./a.out; done
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}
```
Using my impeccable detective skills, I figured `flag{FAKE_FLAG_IS_ALWAYS_GOOD}` was probably not the correct flag, which leaves us with one other option: `flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}`. I am not sure whether this was how the author intended the challenge to be solved, but if it works, it works.

The flag is:
`flag{RUN_R3C0RD_ANA1YZ3_R3P3AT}`
