#You may use import as below.
import math

def solution(shirt_size):
    #Write code here.
    answer = [0 for i in range(len(shirt_size))] # 셔츠 사이즈만큼의 갯수 체크하는 배열 초기화

    if shirt_size=="XS":
        answer[0]+=1

    elif shirt_size=="S":
        answer[1]+=1

    elif shirt_size=="M":
        answer[2]+=1

    elif shirt_size=="L":
        answer[3]+=1

    elif shirt_size=="XL":
        answer[4]+=1

    else:
        answer[5]+=1



    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "M", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")