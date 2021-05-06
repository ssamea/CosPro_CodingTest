def solution(numbers):
    answer = []
    numbers.sort()
    mid = (len(numbers) - 1) // 2 # 리스트의 중앙 인덱스 -1을 해주는 이유는 인데스의 시작위치는 0부터라서
    numbers[mid], numbers[len(numbers)-1] = numbers[len(numbers)-1], numbers[mid] #스왑
    left = mid + 1
    right = len(numbers) - 2

    while left <= right:
    	numbers[left], numbers[right] = numbers[right], numbers[left]
    	left = left + 1
    	right = right - 1
    answer = numbers
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
numbers = [7, 3, 4, 1, 2, 5, 6]
ret = solution(numbers)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")