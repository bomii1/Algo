import time, random

def compute_e_ver1(n):
	# code for O(n^2)-time version
	s = 0
	for i in range(n):
		k = 1
		for j in range(i):
			k = k * (j+1)
		s = s + (1/k)
	return s
	
	
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

	
# n 입력받음
n = int(input())
#print(n)
# compute_e_ver1 호출
before1 = time.process_time()
compute_e_ver1(n)
after1 = time.process_time()

# compute_e_ver2 호출
before2 = time.process_time()
compute_e_ver2(n)
after2 = time.process_time()

# 두 함수의 수행시간 출력
print(after1 - before1)
print(after2 - before2)
print(compute_e_ver1(n),compute_e_ver2(n))

