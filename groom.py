import heapq

m = []
def k_smallest(n):
	m.append(n[0])
	sum = n[0]
	for i in range(1,len(n)):
		H = heapq.nsmallest(((i//3)+1),n[:i+1])
		small = max(H)
		m.append(small)
		sum += m[i]
	return sum


L = list(map(int,input().split()))
x = k_smallest(L)
print(x)