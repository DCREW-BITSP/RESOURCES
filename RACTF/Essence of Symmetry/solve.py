with open('cipher.txt', 'rb') as file:
    line = file.readline()

print(line)

nums = []
for i in line:
    nums.append(i)

n = len(nums)

print(n)


lh = nums[:16]
rh = nums[16:]

print(lh)
print(rh)

for i in lh:
    print(chr(i ^ 21 ^ 22), end="")

for i in range(len(rh)):
    print(chr(rh[i] ^ 22 ^ lh[i]), end="")