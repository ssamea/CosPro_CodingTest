#지난 연속된 n일 동안의 주식 가격이 순서대로 들어있는 리스트가 있습니다. 이때, 다음 규칙에 따라 주식을 사고 팔았을 때의 최대 수익을 구하려 합니다.

# n일 동안 주식을 단 한 번 살 수 있습니다.
# n일 동안 주식을 단 한 번 팔 수 있습니다.
# 주식을 산 날에 바로 팔 수는 없으며, 최소 하루가 지나야 팔 수 있습니다.
# 적어도 한 번은 주식을 사야하며, 한 번은 팔아야 합니다.
# 주식을 팔 때는 반드시 이전에 주식을 샀어야 하며, 최대 수익은 양수가 아닐 수도 있습니다.

def solution(prices):
    INF = 1000000001;
    tmp = INF
    answer = -INF
    for price in prices:
        if tmp != INF:  # 첫 반복시 실행되지 않습니다.(매수가 일어나야 하기 때문)
            answer = max(answer, price-tmp) # 매도시 차익을 구하는 부분으로 price 하강시 answer 변화가 없dma
        tmp = min(tmp, price)
    return answer


# The following is code to output testcase. The code below is correct and you shall correct solution function.
prices1 = [1, 2, 3];
ret1 = solution(prices1);

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

prices2 = [3, 1];
ret2 = solution(prices2);

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")