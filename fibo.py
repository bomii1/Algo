def fibo(n):
	a, b = 1, 1
	if n == 0 or n == 1:
		return 1
	while n != 1:
		c = b
		b = a + b
		a = c
		#print(a, b, a+b)
		n -= 1
	return b
	

# n을 입력받은 후
n = int(input())
# fibo(n) 호출!
f = fibo(n)
# 리턴값을 출력함
print(f)