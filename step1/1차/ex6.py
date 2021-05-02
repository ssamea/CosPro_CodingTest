#You may use import as below.
#import math

def solution(pos):
    # Write code here.
    answer = 0
    # 방향을  위한 변수 나이트는 기본적으로 앞으로 1칸 전진 후, 대각선 한칸 전진하므로
    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, -2, 2, 1, -1, -1, 1]

    cx= ord(pos[0])-ord("A") # 행이 알파벳으로 되어있어서 그 좌표값을 얻기 위해 ord함수를 이용 ex) A7이면 cx=A의 ASCII값 65 -> 65-65=0
    cy= ord(pos[1])-ord("0")-1 #배열의 인덱스는 0이기 때문에 -1을 해준거임. 배

    for i in range(8):
        nx=cx+dx[i]
        ny=cy+dy[i]

        if nx>=0 and nx<8 and ny>=0 and ny<8:
            answer+=1
    return answer

#The following is code to output testcase.
pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")