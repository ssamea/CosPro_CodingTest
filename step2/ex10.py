# 평균은 자료의 합을 자료의 개수로 나눈 값을 의미합니다. 자연수가 들어있는 리스트의 평균을 구하고, 평균 이하인 숫자는 몇 개 있는지 구하려합니다.

def solution(data):
    total = sum(data)
    average = total/len(data)
    cnt = 0
    for d in data:
        if d <= average:
            cnt += 1
    return cnt


# The following is code to output testcase. The code below is correct and you shall correct solution function.
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret1 = solution(data1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
ret2 = solution(data2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")