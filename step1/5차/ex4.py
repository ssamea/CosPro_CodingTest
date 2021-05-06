# 주어진 숫자를 각 숫자와 숫자의 개수로 읽으려 합니다. 이때, 값이 큰 숫자를 먼저 읽어야합니다.
# 예를 들어, 2433은 2 한개 4 한개 3 두개로 이루어져 있기 때문에 "413221"로 읽습니다.
def solution(number): # ex) 2433
    answer = ''
    number_count = [0 for _ in range(10)] # 각 숫자가 얼만큼 나오기 위해 세기 위한 리스트


    while number > 0:
        number_count[number % 10] += 1
        number //= 10

    #값이 큰 숫자를 먼저 읽어야합니다.
    for i in range(9,-1,-1):
        if number_count[i] != 0:
            answer += (str(i) + str(number_count[i]))
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
number1 = 2433
ret1 = solution(number1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 662244
ret2 = solution(number2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")