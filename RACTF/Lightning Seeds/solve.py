import random

flag = '4fcbac835550403f13c4cc337d8d8da48351921dfb7cd47d33857432c2ee665d821227'
nums = []
init = 'DOCTF{'
start = []

for i in range(0, len(flag)-1, 2):
    a = (str(flag[i]) + str(flag[i + 1]))
    nums.append(int(a, 16))
print(f'nums = {nums}') #nums is ASCII of each letter of flag xorred with random int converted from hexadecimal to decimal

for i in range(len(init)):
    for j in range(255):
        if j ^ ord(init[i]) == nums[i]:
            start.append(j)

print(f'start = {start}') #start is first 6 random numbers and xorring with first 6 of start to compare with "DOCTF{" 
seed=0


for i in range(999):
    test = []
    random.seed(i)
    for j in range(6):
        test.append(random.randint(0, 255))
    if test == start:
        print(f'seed = {i}')
        seed = i     #Seed is bruteforced by generating 6 random numbers and comparing with known random numbers in start

random.seed(seed)  #seed = 876

for i in range(len(nums)):
    print(chr(nums[i] ^ random.randint(0, 255)), end="")