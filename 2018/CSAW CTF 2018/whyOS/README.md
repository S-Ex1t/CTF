# whyOS
***Category: Forensics***
> Have fun digging through that one. No device needed.
> Note: the flag is not in flag{} format
> 
> HINT: the flag is literally a hex string. Put the hex string in the flag submission box
> 
> Update (09/15 11:45 AM EST) - Point of the challenge has been raised to 300 Update
>
> Sun 9:09 AM: its a hex string guys
***

***Update:*** *Since I was completely new to iOS applications, I decided to do a little more research after the CTF was over. I knew my solution was not the intended method to solve the challenge and also relied heavily on the hint, so I did some research on how log entries are generated to figure out how to solve this the correct way. As it turns out, my assumptions about the flag format were completely wrong and my solution was 100% luck and coincidence. Nevertheless, I still got the flag and ended up learning something new, so that's a win in my book.*

For this challenge, we are given two files: [com.yourcompany.whyos_4.2.0-28debug_iphoneos-arm.deb](com.yourcompany.whyos_4.2.0-28debug_iphoneos-arm.deb) and [console.log](console.log). 

We begin by taking a quick glance through the `console.log` to see what we were dealing with. The `console.log` turned out to be an extremely large file containing 185,088 log entries, which meant `com.yourcompany.whyos_4.2.0-28debug_iphoneos-arm.deb` had to contain some clues to help us narrow down the search criteria. I begin looking through the file for any clues that might point us towards where the flag might be. After a quick search through the contents of the files, we find a file named `Root.plist` located in `data.tar.lzma/Library/PreferenceBundles/whyOSsettings.bundle/` which contained the following snippet of code:

	<dict>
		<key>cell</key>
		<string>PSGroupCell</string>
		<key>footerText</key>
        <string>Put the flag{} content here</string>
	</dict>
I assumed this was the format for the log entry where the flag was hiding. Based on the snippet of code above, I was able to tell the flag was in the last part of the log entry. After getting the hint: `the flag is literally a hex string`, I was able to narrow down my search results by a ton. In order to narrow down the initial search results even more, I assumed the flag was at least 32 characters long. 

I felt this was enough to at least get me started, so I began a search with the following assumptions:
- The flag is in the last field of the log entry
- The flag is a hex string of 32 characters or more

Using this criteria, I wrote a quick python script to filter through the entries:
```
import re
with open('console.log','r') as f:
    data = [i.strip() for i in f]
    
matches = []
for i in data:
    if re.match('^[a-f0-9]{32,}$',i.split()[-1],re.I):
            matches.append(i)

for i in matches:
    print i
```
Since I had almost no experience with iOS applications prior to this challenge, I was not exactly sure what to look for or what data would be in each individual field. Because of this, I decided to leave out the filter for fields and just manually look through the results for anomalies. Surprisingly, the script returned only three results:
```
default 19:09:48.701395 -0400   securityd   session[0x102c43610] failed to decrypt, session: <Done c i FPDk 6:7 PT 0 Mrse>, mk: <SecOTRFullDHKeyRef@0x102b4ba00: x: E4FF45A23909E20AB8FEA0A8C9563737A326EDA49CC91C55538316A30569D27F y: 53627A4C1446D7BE3956C5E0CB55E31AD23CF7490D9B4380CF4057423A73DF38 [5EC13ED1FFE1BDCF875BA2CD31C0A017524672C7]>, mpk: <SecOTRFullDHKeyRef@0x102b55560: x: F7009D0863F90B650E0D8725CC04E7D375572EF97EACBB5AC4E14806713C8AAE y: 744B2996A4CFC79D95D5E5B87D2A8ADC205C4A0383DCA04344B87B4FCABB7A87 [6CE646617B058CDFB1DCBBF5C3DE3C991219C0FE]>, tpk: <SecOTRPublicDHKeyRef@0x102b2c640: x: E705E1726FE049DBD6AF9713BF98FB0EEA97F2DA63B63B15AE83C8789D4E0B2D y: 7A53E0F1EB2DEADEA2012AFBFFCA8B7524EEA84E65C0C771A24536EE5DD456D9 [621BF69F134448C3FAE3BCB114CF58C446DD2D67]>, tk: <SecOTRPublicDHKeyRef@0x102b4b670: x: A183EF7B34E0924D1A49317AB2DDC77365BFCAF158A058A8BD3D9896D1FF3E8A y: 4774FF271BA4CFCE6B5A787AC9B74AEC70574A7B62B8D5189D76169835F0195A [82EE8C5862AF5E2017A1F9D92DD86F3AEF796B30]>, chose tktu: <SecOTRPublicDHKeyRef@0x102b2c640: x: E705E1726FE049DBD6AF9713BF98FB0EEA97F2DA63B63B15AE8
default 19:09:48.704576 -0400   securityd   session[0x102c402d0] failed to decrypt, session: <Done c i FPdk 319:319 PT 0 Mrse>, mk: <SecOTRFullDHKeyRef@0x102b1e210: x: 06B7C203FA950F848F46E3C9AD4946141EACE5E8015F58BE1E11C2D343EBF1E0 y: 19E64A4A8C1A420E1702C38972A5754C3564F24C5F823175CFA6A4B9A074210E [27AB14752A96A358E385E7161968EE4DF90A34E5]>, mpk: <SecOTRFullDHKeyRef@0x102b4b430: x: 15D5FF367C910C32A903391C61DD3BCCD59DD86F1C4F9ABB39E4C789BC2802F2 y: 7D1D9CC90611ABEB8BADB606816D55DF1BC09358EEFAAD65537CD7569DDC4CE9 [43FDF4F8ED5094C1CB3F63A6E81FBC869F1B07FE]>, tpk: <SecOTRPublicDHKeyRef@0x10294f220: x: 9EB6562D61A0BB1C1FFCEF1C1C184AB2BC39E6889126370AEE47BD6EE4BC0D01 y: 460C25FEDAD5A42470AD029B757F3849D2A6271CDB0176D7A1DB74929628FF05 [C5C06D0001663B7552BBA8ED442A7E13DEA90D42]>, tk: <SecOTRPublicDHKeyRef@0x102c80750: x: 07282DF3961CDDEB26007E061740FF4F2727B73F36A40006C747B9805635C866 y: 067FCCEB2ACB818E748B4525CBF3816D33B3949806028D97D9C77EC4D48EFD80 [7649E1A68A560B72F76F8C27176A2B6B7970C335]>, chose tktu: <SecOTRPublicDHKeyRef@0x10294f220: x: 9EB6562D61A0BB1C1FFCEF1C1C184AB2BC39E6889126370
default 19:12:18.884704 -0400   Preferences ca3412b55940568c5b10a616fa7b855e
```

The first two results contained a bunch of extraneous information. However, the last result looked pretty close to what we were looking for:

`default 19:12:18.884704 -0400   Preferences ca3412b55940568c5b10a616fa7b855e`

So I tried checking if `ca3412b55940568c5b10a616fa7b855e` was the flag and it was!

Flag: `ca3412b55940568c5b10a616fa7b855e`
