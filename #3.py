def compute_e_ver2(n):
	s = []
	sum = 0
	k = 1
	for i in range(n):
		k = k * (i+1)
		s.append(1/k)
	for j in range(n):
		sum += s[j]
	return sum

n = int(input())
print(compute_e_ver2(n))