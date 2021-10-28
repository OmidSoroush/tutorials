import sys

#Read the inputs.
N = 3

P = [0] * N

print([0] * 4)
for i in range(N):
    P[i] = int(input())

#Sort horse strengths.
P.sort()

#Find D.
D = sys.maxsize

for i in range(1, N):
    D = min(D, P[i] - P[i - 1])

#Print D.
print(D)