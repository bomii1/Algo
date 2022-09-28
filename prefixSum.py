import time, random

def prefixSum1(A, n):
	# code for prefixSum1
	start = time.process_time()
	s = []
	for i in range(0,n):
		s.append(0)
		for j in range(0,i):
			s[i] += A[j]
	end = time.process_time()
	return end - start
	
	
def prefixSum2(A, n):
	# code for prefixSum2
	start = time.process_time()
	s = [0]
	s[0] = A[0]
	for i in range(1,n):
		s.append(0)
		s[i] = s[i-1] + A[i]
	end = time.process_time()
	return end - start
	
random.seed()		# random 함수 초기화

# n 입력받음
n = int(input())

# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = []

for i in range(n):
	A.append(random.randint(-999,999))
	
# prefixSum1 호출
# prefixSum2 호출
ps1 = prefixSum1(A,n)
ps2 = prefixSum2(A,n)

# 두 함수의 수행시간 출력
print(ps1,ps2)