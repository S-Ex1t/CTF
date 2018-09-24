# DefCamp CTF 2018: RobotsVSHumans
***Category: web***
>*Find your flag on this website.
>Target: https://robots-vs-humans.dctfq18.def.camp/*
## Solution
For this challenge, we are given a website with a flag hidden somewhere in it.

Based on the name of the challenge, I immediately think of checking [robots.txt](robots.txt). Unfortunately, we only get this:
```
Did you know that robots.txt is not the only .txt file in a website? BTW: I am against humans!
```
However, it does give us a hint. This, combined with the title of the challenge, `RobotsVSHumans`, makes me think to check [humans.txt](humans.txt). From there, we get:
```
                            
/* TEAM */

                            
Your title: RobotsVSHumans

                            
Location: Bcharest, Romania

							
/* THANKS */

							
Name: DCTF{1091d2144edbffaf5dd265cb7c93e799c4659eb16ee79735b3bd6e09dd6e791f}
```

***Flag: `DCTF{1091d2144edbffaf5dd265cb7c93e799c4659eb16ee79735b3bd6e09dd6e791f}`***
