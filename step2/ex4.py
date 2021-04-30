#자연수가 들어있는 리스트가 있습니다. 이 리스트에서 가장 많이 등장하는 숫자의 개수는 가장 적게 등장하는 숫자 개수의 몇 배인지 구하세요

# 1단계. 리스트에 들어있는 각 자연수의 개수를 셉니다.
# 2단계. 가장 많이 등장하는 수의 개수를 구합니다.
# 3단계. 가장 적게 등장하는 수의 개수를 구합니다.
# 4단계. 가장 많이 등장하는 수가 가장 적게 등장하는 수보다 몇 배 더 많은지 구합니다.

def func_a(arr): # 1단계.
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1
    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr):
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt  #4단계

#The following is code to output testcase.
arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")