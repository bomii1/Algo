def compute_e_ver2(n):
	# code for O(n)-time version
	s = 1
	k = 1
	if n == 1:
		return s
	for i in range(1, n):
		k = k * i
		s = s + (1/k)
	return s

n = int(input())
print(compute_e_ver2(n))