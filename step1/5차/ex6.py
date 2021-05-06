# 다음과 같이 import를 사용할 수 있습니다.
import math

# p 진법으로 표현한 수란, 각 자리를 0부터 p-1의 숫자로만 나타낸 수를 의미합니다. p 진법으로 표현한 자연수 두개를 더한 결과를 q 진법으로 표현하려 합니다.
# 접근법:  10진수로 변환 후  더하고 q진법으로 변환

numbers_int = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def char_to_int(ch):
    for i in range(10):
        if ch == numbers_char[i]:
            return numbers_int[i]

def int_to_char(val):
    for i in range(10):
        if val == numbers_int[i]:
            return numbers_char[i]

def convert_scale(num, q):
    if num == 0:
        return ""
    return convert_scale(num // q, q) + int_to_char(num % q)

def parse_decimal(s, p):
    num = 0
    mul = 1
    for s_i in reversed(s):
        num += char_to_int(s_i) * mul
        mul *= p
    return num

def solution(s1, s2, p, q):
    num1 = parse_decimal(s1, p)
    num2 = parse_decimal(s2, p)
    answer = convert_scale(num1 + num2, q)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")