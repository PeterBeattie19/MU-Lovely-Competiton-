a = input()
b = input()

a = [a[i:i+4] for i in range(0, len(a)-3, 4)]
b = [b[i:i+4] for i in range(0, len(b)-3, 4)]

a = set(a)
b = set(b) 

print("".join(list(a - b)))