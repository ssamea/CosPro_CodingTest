# You may use import as below.
# import math

def solution(n): # n==3, 3x3 array
    # Write code here.
    data=[[0 for _ in range(n)] for _ in range(n)]
    answer = 0
    #방향을  위한 변수
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    ci, cj = 0, 0 # 시작 좌표 설정
    num=1

    while 0 <= ci and ci < n and 0 <= cj and cj < n and data[ci][cj]==0: # x,y좌표는 모드 0보다 크거나 같아야하며 nxn행렬 이니까 여기를 초과하면 안되면서 현재 초기화된 배열값이0
        for k in range(4):
            if not 0<= ci and not ci < n and not 0 <= cj and not cj < n and data[ci][cj]!=0:
                break
            while True:
                data[ci][cj]=num
                num+=1
                nx=ci+dx[k]
                ny=cj+dy[k]
                if not 0<= ci and not ci < n and not 0 <= cj and not cj < n and data[ci][cj]!=0:
                    ci += dy[(k + 1) % 4]
                    cj += dx[(k + 1) % 4]
                    break
                ci=nx
                cj=ny


    for i in range(n):
        answer += data[i][i]

    return answer


# The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

n2 = 2
ret2 = solution(n2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")