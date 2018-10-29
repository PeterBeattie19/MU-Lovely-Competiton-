def collatx(n, x, k, current, a):
    if n==1 and current == 0:
        return 1
    
    if [n, current] in a:
        print("-1")
        exit() 
        
    a.append([n, current]) 
    
    
    if n%2 == 0:
        return 1 + collatx(int(n/2), x, k, (current+1)%(k), a)
    
    
    return 1 + collatx(3*n + 1, x, k, (current + 1)%(k), a)

n, x, k = map(int, input().split()) 
print(collatx(n, x, k, x, []) - 1)