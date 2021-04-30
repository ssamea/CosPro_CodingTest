#369 게임은 여러 명이 같이하는 게임입니다. 게임의 규칙은 아래와 같습니다.

#1부터 시작합니다.
#한 사람씩 차례대로 숫자를 1씩 더해가며 말합니다.
#말해야 하는 숫자에 3, 6, 9중 하나라도 포함되어있다면 숫자를 말하는 대신 숫자에 포함된 3, 6, 9의 개수만큼 손뼉을 칩니다.

def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i # 현재 진행 수
        temp = count
        while current != 0:
            if current%3==0:
                count += 1
                print("pair", end = '')
            current = current // 10
        if temp == count:
            print(i, end = '')
        print(" ", end = '')
    print("")
    return count

#The following is code to output testcase.
number = 40
ret = solution(number)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")