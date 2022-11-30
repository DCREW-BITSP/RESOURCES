## Lightning Seeds

Looking through encrypt.py we see 
```python
encrypted = ''.join(f'{(ord(c) ^ random.randint(0,255)):02x}' for c in flag)
```
So each letter of the flag is XORred with a random integer in the range of 0 to 255 and then added to out.txt in the form of a 2 digit hexadecimal number.

Since the random package of python generates pseudo-random numbers and the seed is generated only once, we can crack the seed since we know the flag starts with "DOCTF{"


In solve.py
```python
for i in range(0, len(flag)-1, 2):
    a = (str(flag[i]) + str(flag[i + 1]))
    nums.append(int(a, 16))
print(nums)
```
nums contains the 2 digit hexadecimal converted back to decimal for easier operations


We can find the first 6 randomly generated numbers using
```python
init = 'DOCTF{'
for i in range(len(init)):
    for j in range(255):
        if j ^ ord(init[i]) == nums[i]:
            start.append(j)
```


The seed can then be bruteforced using
```python
for i in range(999):
    test = []
    random.seed(i)
    for j in range(6):
        test.append(random.randint(0, 255))
    if test == start:
        print(f'Seed is {i}')
        seed = i
```
which gives the seed as 876

The flag can then be found by XORring each number in nums with the random number generated using seed 876
```python
random.seed(seed)  #seed = 876

for i in range(len(nums)):
    print(chr(nums[i] ^ random.randint(0, 255)), end="")
```



**Flag: DOCTF{n0t_4s_r4nd0m_4s_y0u_th1nk!}**
