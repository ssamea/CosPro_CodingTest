# 시작 날짜와 끝 날짜가 주어질 때, 두 날짜가 며칠만큼 떨어져 있는지(D-day)를 구하려 합니다.
#1단계. 시작 날짜가 1월 1일로부터 며칠만큼 떨어져 있는지 구합니다.
#2단계. 끝 날짜가 1월 1일로부터 며칠만큼 떨어져 있는지 구합니다.
#3단계. (2단계에서 구한 날짜) - (1단계에서 구한 날짜)를 구합니다.

def func_a(month, day): # (1/2)
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0;
    for i in range(month-1):
        total +=month_list[i]
    total +=day

    return total - 1


def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day) #1단계
    end_total = func_a(end_month, end_day) #2단계
    return end_total - start_total #3단계


# The following is code to output testcase. 1/2일 2/2일 차이를 구하시오
start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

# Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")