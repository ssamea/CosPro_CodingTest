#You may use import as below.
#import math

def solution(num): #9949999
    # Write code here.
    answer = num+1
    str_ans=str(answer)
   #  a=1  #1의 자리수부터 더하기위한 변수

   # while answer // a % 10 == 0:
    #    answer+=a
     #   a*=10 # 1,10,100 .... 자리수 초기화 

    C=str_ans.replace('0','1')

    answer=int(str_ans)
    print(C)

    return answer


#The following is code to output testcase.
num = 9949999;
ret = solution(num)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")