## Based Pande

Running
`strings cutie.jpg`
gives us the following line of text:

`RE9DVEZ7UDRuRDNzTDBvazRGVDNSRTBGfQ==`

which is a base64 encoded line of text.

Run `echo "RE9DVEZ7UDRuRDNzTDBvazRGVDNSRTBGfQ==" | base64 -d` to get the flag

**Flag: DOCTF{P4nD3sL0ok4FT3RE0F}**
