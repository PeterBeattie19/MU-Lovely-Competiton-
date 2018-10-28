def convert_to_sec(s):
    #s = "hh:mm:ss"
    s = list(map(int, s.split(':')))
    t = s[0]*60*60
    t += s[1]*60
    t += s[2]
    return t

init_line = input().split() 
n = int(init_line[0]) 

max_time = convert_to_sec(init_line[1]) 

arr = [input() for _ in range(n)] 
arr = list(map(convert_to_sec, arr)) 
arr.sort() 

c = 0
total = 0
while True:
    if c >= len(arr): break
    total += arr[c]
    if total > max_time: break
    c += 1
print(c)
