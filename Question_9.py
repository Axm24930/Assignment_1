import math
N = int(input("Enter Number of students:"))
print("Enter the weights of ",N,"Students:")
L1 = []
for i in range(0, N):
    wt = int(input())
    L1.append(wt)

print("weights in lbs", L1)
# convert lbs to kgs
Kg1= []
for i in range(0, N):
    Kg1.append(math.floor((L1[i] / 2.2046) * 100) / 100)
print("Weights in kgs", Kg1)
