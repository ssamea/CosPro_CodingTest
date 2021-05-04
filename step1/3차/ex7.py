#카프리카 수는 다음을 만족하는 수를 뜻합니다.

#자신의 제곱수를 둘로 나누어 더한 값이 자기 자신과 같습니다.
#단, 둘로 나뉜 수는 모두 양수여야 합니다.
#자연수 k가 매개변수로 주어질 때, k 이하인 모든 카프리카 수를 리스트에 담아 오름차순으로 정렬하여 return 하도록 solution 함수를 작성

def solution(k):
    answer = [] #카프리수를 담을 변수
    for i in range(1, k + 1): # 인덱스가 1부터 시작하니까 끝은 k+1 (501)
        square_num = i * i # 제곱수, 250000
        divisor = 1
        while square_num // divisor != 0: # 여기가 문제인데 모든 수가 다 걸려짐.
            front = square_num // divisor
            back = square_num % divisor
            divisor *= 10
            if back != 0 and front != 0:
                if front + back == i:
                    answer.append(i)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution 함수만 수정하세요.
k = 500
ret = solution(k)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")