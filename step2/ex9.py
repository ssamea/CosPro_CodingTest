#알파벳 문자열이 주어질 때, 연속하는 중복 문자를 삭제하려고 합니다. 예를 들어, "senteeeencccccceeee"라는 문자열이 주어진다면, "sentence"라는 결과물이 나옵니다.

#영어 소문자 알파벳으로 이루어진 임의의 문자열 characters가 매개변수로 주어질 때, 연속하는 중복 문자들을 삭제한 결과를 return

def solution(characters):
    result = ""
    result += characters[0]
    for i in range(1,len(characters)):
        if characters[i - 1] != characters[i]:
            result += characters[i]
    return result

#The following is code to output testcase. The code below is correct and you shall correct solution function.
characters = "senteeeencccccceeee"
ret = solution(characters)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")