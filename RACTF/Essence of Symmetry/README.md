Looking through main.go we can see
```go
var (
	m, n = 21, 22
)

L, R := string(content[:len(content)/2]), string(content[len(content)/2:])
	x := ""
	for i := 0; i < len(L); i++ {
		x += string(int(op(string(R), m)[i]) ^ int(L[i]))
	}
	y := op(string(R), 0)
  
  L, R = y, x
	x = ""
	for i := 0; i < len(L); i++ {
		x += string(int(op(string(R), n)[i]) ^ int(L[i]))
	}
	y = op(string(R), 0)

	ciphertext := x + y
  ```
  content contains the flag. The flag is divided into two parts of equal length L and R. We can figure through the code that the text in cipher.txt is the left half
  of the flag XORred with 21 and 22 and the right half XORred with the left half and 21
  
  
  In solve.py
  ```python
  with open('cipher.txt', 'rb') as file:
    line = file.readline()

  print(line)

  nums = []
  for i in line:
      nums.append(i)
  ```
  nums contains the ascii of the bytes in cipher.txt
  
  
  ```python
  lh = nums[:16]
  rh = nums[16:]
  for i in lh:
      print(chr(i ^ 21 ^ 22), end="")

  for i in range(len(rh)):
      print(chr(rh[i] ^ 22 ^ lh[i]), end="")
  ```
  XORres the left half of nums with 21 and 22 and the right half with 22 and the left half
  
  **Flag:DOCTF{1TS_4_F3I$TIV4L_0F_S0RT$}**
