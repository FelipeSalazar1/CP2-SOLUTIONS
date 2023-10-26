n = 123456
sum = str(n)
sumAlg = 0
i = 0
b = n

while True:
    sum = str(b)
    if b < 10:
        break
    while i < len(sum):
        sumAlg += int(sum[i])
        i += 1
    i = 0
    b = sumAlg
    sumAlg = 0
print(sumAlg)
