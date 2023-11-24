n , m = map(int , input().split())
ar = list(map(int , input().split()))

fre_arr = {}

for i in range(1, m+1):
    fre_arr[i] = 0
    
for i in ar: 
    if i in fre_arr:
        fre_arr[i] += 1
        
for i in range(1, m+1):
    print(fre_arr[i])
