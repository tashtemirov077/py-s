sonlar = [9, 32, 13, 46, 80]
sonlar2 = [20,17,28,48,73,88]
juft = []
toq = []
 
main = sonlar+sonlar2

for item in main:
    if item % 2 == 0:
        juft.append(item)
    else:
        toq.append(item)

print("juft sonlar:", juft)
print("toq sonlar:", toq)


juftYigindi = 0
for i in juft:
    juftYigindi += i


toqYigindi = 0
for i in toq:
    toqYigindi += i

print("juft sonlar yig'indisi:", juftYigindi)
print("toq sonlar yig'indisi:", toqYigindi)
    