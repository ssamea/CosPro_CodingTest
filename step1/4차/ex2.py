#알파벳 소문자와 대문자로 구성된 문자열을 압축하려 합니다. 압축이란 대표 문자와 대표 문자가 연속되는 개수를 함께 표현하는 것입니다. 이때, 대문자와 소문자는 구분하지 않으며, 대표 문자는 소문자로 표현합니다.

#예를 들어, 문자열 "YYYYYbbbBbbBBBMmmM"을 압축하면 "y5b9m4"입니다.

def solution(s): # s = "YYYYYbbbBbbBBBMmmM"
    s = s.lower() # 소문자로 변환, s="yyyyybbbbbbbbbmmmm"
    answer = ""
    previous = s[0]
    counter = 1
    for alphabet in s[1:]: # alpha[1]=y, [2]=y,[3]=y...
        if alphabet == previous: # 비교변수인 previeous와 같다면 그 알파벳의 카운터 +1
            counter += 1
        else:
            answer += previous + str(counter)
            counter = 1
            previous = alphabet
    answer += previous + str(counter)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
s = "YYYYYbbbBbbBBBMmmM"
ret = solution(s)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")