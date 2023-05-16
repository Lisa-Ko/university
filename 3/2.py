N = int(input())
S=0
k=-0.5
a=2
for i in range (N):
    print(a)
    S+=a
    a=a*k
print(S)