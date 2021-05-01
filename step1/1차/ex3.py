#문자열 형태의 식을 계산하려 합니다. 식은 2개의 자연수와 1개의 연산자('+', '-', '*' 중 하나)로 이루어져 있습니다.
#ex) 주어진 식이 "123+12"라면 이를 계산한 결과는 135입니다.
#1단계. 주어진 식에서 연산자의 위치를 찾습니다.
#2단계. 연산자의 앞과 뒤에 있는 문자열을 각각 숫자로 변환합니다.
#3단계. 주어진 연산자에 맞게 연산을 수행합니다.

def func_a(numA, numB, exp):
    if exp == '+':
        return numA + numB
    elif exp == '-':
        return numA - numB
    elif exp == '*':
        return numA * numB


def func_b(exp):
    for index, value in enumerate(exp):
        if value == '+' or value == '-' or value == '*':
            return index


def func_c(exp, idx):
    numA = int(exp[:idx])
    numB = int(exp[idx + 1:])
    return numA, numB


def solution(expression):
    exp_index = func_b(expression)
    first_num, second_num = func_c(expression,exp_index)
    result = func_a (first_num, second_num,expression[exp_index])
    return result


# The following is code to output testcase.
expression = "123+12"
ret = solution(expression)

# Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")