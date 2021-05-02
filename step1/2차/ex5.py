#자연수가 들어있는 리스트가 있습니다. 이 리스트에서, 숫자가 연속해서 증가하는 가장 긴 구간의 길이를 구하려 합니다. 단, 바로 전 숫자와 현재 숫자가 같은 경우는 증가한 것으로 보지 않습니다.
#접근법
# 1. 첫번째수가 두번째수보다 무조건 작음녀 ans+1
# 2. 방문하면서 값이 계속 커지는지 검사하면서 참이면 ans+1

#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(arr):
    #여기에 코드를 작성해주세요.

    answer = 0
    dp = [1 for _ in range(len(arr))]

    for i in range(1,len(arr)):
        if arr[i]> arr[i-1]:
            dp[i] = dp[i-1] + 1

    answer = max(dp)

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)


#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")