import heapq

def k_smallest(n):
    sum = 0
    kth,N = [],[]

    for i in range(len(n)):
        if i%3 == 0 and i != 0:
            heapq.heappush(kth,-heapq.heappop(N))
        heapq.heappush(kth,-n[i])
        heapq.heappush(N,-heapq.heappop(kth))
        sum += N[0] 
    return sum  
 
L = list(map(int,input().split()))
x = k_smallest(L)
print(x)
