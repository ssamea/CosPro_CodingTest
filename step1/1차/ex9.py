#1. 계단 제일 아래에서 게임을 시작합니다. (0번째 칸)
#2. 가위바위보를 합니다.
#3. 이기면 계단 세 칸을 올라가고, 지면 한 칸을 내려가고, 비기면 제자리에 있습니다.
#4. 계단 제일 아래에서 지면 제자리에 있습니다.
#5. 2~4 과정을 열 번 반복합니다.

def func(record):
    if record == 0:
        return 1 #1은 바위
    elif record == 1:
        return 2 #2는 보
    return 0

def solution(recordA, recordB):
    cnt = 0
    for i in range(len(recordA)): #길이 10
        if recordA[i] == recordB[i]: #비길 경우
            continue
        elif recordA[i] == func(recordB[i]): #이길 경우
            cnt = cnt + 3
        else: #질 경우
            cnt = max(0,cnt - 1) #계단 제일 아래값은 0이므로 음수값은 없음. 그래서 음수값이 나오면 0으로 퉁치는거임
    return cnt

#The following is code to output testcase. The code below is correct and you shall correct solution function.
# 0, 1, 2중 하나이고 순서대로 가위, 바위, 보를 의미
recordA = [2,0,0,0,0,0,1,1,0,0]
recordB = [0,0,0,0,2,2,0,2,2,2]
ret = solution(recordA, recordB)


#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")