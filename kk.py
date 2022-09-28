import heapq

def k_smallest(n):
    heap, last = [], [] 
    res = 0
    for i in range(0, len(n)):
        if i != 0 and i % 3 == 0:
            heapq.heappush(last, -heapq.heappop(heap))
        heapq.heappush(last, -n[i])
        heapq.heappush(heap, -heapq.heappop(last))
        res += heap[0]
    return res

L = list(map(int,input().split()))
x = k_smallest(L)
print(x)