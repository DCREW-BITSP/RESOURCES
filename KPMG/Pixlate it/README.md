DFIR2.zip contains gotreut.jpeg. Run binwalk to extract E004.zip from gotreut.jpeg. E004.zip is password protected so run exiftool on gotreut.jpeg to read metadata and get Base64 encoded password which gives flag1.txt. Use the hint in flag1.txt as passphrase for steghide on gotreut.jpeg which gives flag.txt. flag.txt has the flag brainfuck encoded.