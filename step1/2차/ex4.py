#다음과 같이 import를 사용할 수 있습니다.
#자연수가 중복 없이 들어있는 리스트가 있습니다,  이 리스트에서 합이 K의 배수가 되도록 서로 다른 숫자 세개를 고르는 방법은 몇 가지인지 세려고 합니다.


#import math

def solution(arr, K):
    #여기에 코드를 작성해주세요.
    answer = 0 #카운트 변수

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for c in range(j+1,len(arr)):
                if (arr[i]+arr[j]+arr[c]) % K ==0:
                    answer+=1


    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")