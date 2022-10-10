## Pixlate It ##
_DFIR2.zip_ contains _gotreut.jpeg_. Run ```binwalk -e gotreut.jpeg``` to extract _E004.zip_ from _gotreut.jpeg_. _E004.zip_ is password protected so run ```exiftool gotreut.jpeg``` to read metadata and get Base64 encoded password which gives _flag1.txt_. Use the hint in _flag1.txt_ as passphrase for ```steghide extract -sf gotreut.jpeg``` which gives _flag.txt_. _flag.txt_ has the flag brainfuck encoded.

Flag: KPMG{CTfs_4r3_Fun}
