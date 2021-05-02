#현재 작성되어있는 가장 마지막 게시글 이후에 작성된 게시글이어야 합니다.
#게시글 번호의 자릿수가 짝수여야 합니다.
#게시글 번호가 2n 자릿수 일때, 앞 n 자리의 각 자릿수의 합과 뒤 n 자리의 각 자릿수의 합이 같아야 합니다.

def func_a(n): #n==235388
    ret = 1
    while n > 0:
        ret *= 10 #ret=10
        n -= 1 #n=235387
    return ret


def func_b(n): #n == 235388
    ret = 0
    while n > 0:
        ret += 1  # ret=1
        n //= 10  # n=23538
    return ret


def func_c(n): #n=235388
    ret = 0
    while n > 0:
        ret += n % 10 #ret=8
        n //= 10    # n=23538
    return ret


def solution(num):
    next_num = num
    while True:
        next_num += 1
        length = func_b(next_num)
        if length % 2:
            continue

        divisor = func_a(length // 2)

        front = next_num // divisor
        back = next_num % divisor

        front_sum = func_c(front)
        back_sum = func_c(back)
        if front_sum == back_sum:
            break

    return next_num - num

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
num1 = 1
ret1 = solution(num1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num2 = 235386
ret2 = solution(num2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")