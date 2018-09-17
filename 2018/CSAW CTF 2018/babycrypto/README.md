# babycrypto
***Category: Crypto***
>yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeet
>
>single yeet yeeted with single yeet == 0
>
>yeeet
>
>what is yeet?
>
>yeet is yeet
>
>Yeetdate: yeeted yeet at yeet: 9:42 pm
---

For this challenge, we are given [ciphertext.txt](ciphertext.txt) which contains a base64 encoded string.
With the challenge being worth 50 points, I figured it would be encrypted with a relatively simple method.
Using [CyberChef](https://gchq.github.io/CyberChef/), I decoded the base64 string and started messing around with the resulting ciphertext.
Using the `XOR Brute Force` function, I saw a plaintext output using key `FF`. I then swapped out the brute force for an `XOR` with key `FF` which gave me this:


>`Leon is a programmer who aspires to create programs that help people do less. He wants to put automation first, and scalability alongside. He dreams of a world where the endless and the infinite become realities to mankind, and where the true value of life is preserved.flag{diffie-hellman-g0ph3rzraOY1Jal4cHaFY9SWRyAQ6aH}`

The flag is:
`flag{diffie-hellman-g0ph3rzraOY1Jal4cHaFY9SWRyAQ6aH}`



Alternatively, you can use the [Magic function with Intensive mode](https://gchq.github.io/CyberChef/#recipe=Magic(3,true,false)&input=czVxUWtkK1dqTitlMzQrTmtKaU5ucEtTbW8zZmlKZVEzNTZNajVhTm1vemZpNURmbkkyYW5vdWEzNCtOa0ppTm5wS00zNHVYbm92Zmw1cVRqOStQbXBDUGs1cmZtNURmazVxTWpOSGZ0NXJmaUo2Umk0emZpNURmajRxTDM1NktpNUNTbm91V2tKSGZtWmFOakl2VDM1NlJtOStNbko2VG5wMldrNWFMaHQrZWs1Q1JtSXlXbTVyUjM3ZWEzNXVObXA2U2pOK1FtZCtlMzRpUWpaT2IzNGlYbW8yYTM0dVhtdCtha1p1VG1veU0zNTZSbTkrTGw1cmZscEdabHBHV2k1cmZuWnFja0pLYTM0MmFucE9XaTVhYWpOK0xrTitTbnBHVWxwR2IwOStla1p2ZmlKZWFqWnJmaTVlYTM0dU5pcHJmaVo2VGlwcmZrSm5mazVhWm10K1dqTitQalpxTW1vMkptcHZSbVpPZW1JU2JscG1abHByU2w1cVRrNUtla2RLWXo0K1h6STJGalo2d3BzNjFucFBMbkxlZXVhYkdyS2l0aHI2dXlaNjNnZz09) in `CyberChef` which will attempt to make sense of the data for you based on the resulting entropy. The first result returns `From_Base64('A-Za-z0-9+\\-=',false)
XOR({'option':'Hex','string':'ff'},'Standard',false)` as a possible decryption key.
