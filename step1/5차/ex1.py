#계단 n칸을 올라가는 방법의 수를 구하려고 합니다. 계단은 한 번에 1계단, 2계단, 3계단씩 오를 수 있습니다. 예를 들어, 계단 3칸을 오르는 방법은 다음과 같이 4가지가 있습니다.
#1. 1계단 + 1계단 + 1계단
#2. 1계단 + 2계단
#3. 2계단 + 1계단
#4. 3계단

def solution(n):
	answer = 0
	steps = [0 for _ in range(n+1)] ## dp로 문제 푸는 방법이네요
	steps[1] = 1
	steps[2] = 2
	steps[3] = 4
	for i in range(4, n+1):
		steps[i] = steps[i-1]+steps[i-2]+steps[i-3]
	answer = steps[n]
	return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
ret1 = solution(n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 4
ret2 = solution(n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")