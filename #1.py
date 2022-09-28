import random

def compute_e_ver2(n):
	# code for O(n)-time version
	s = 0
	for i in range(n):
		k = 1
		for j in range(i):
			k = k * (j+1)
		s = s + (1/k)
	return s

n = random.randint(100,500000)
x = compute_e_ver2(n)
print(x)


