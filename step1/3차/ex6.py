#어떤 수를 서로 다른 소수 3개의 합으로 표현하는 방법의 수를 구하려 합니다.
#자연수 n이 매개변수로 주어질 때, n을 서로 다른 소수 3개의 합으로 표현하는 방법의 수를 return 하도록 solution 함수를 작성

def solution(n):
    answer = 0
    primes = [2] #소수 배열
    for i in range (3, n + 1, 2) : # 3~n+1까지 2만큼 건너 뛰자. ex) 3, 5, 7, 왜? 2이후부터 시작하는 소수를 구해야하므로
        is_prime = True
        for j in range(2, i) : # 소수인지 판별 하고 아니면 탈출
            if i % j == 0 :
                is_prime = False
                break
        if is_prime == True :
            primes.append(i)


    # 구해진 소수 배열을 가지고 N값을 구할 수 있는 조합을 찾아내야함
    prime_len = len(primes)
    for i in range(0, prime_len - 2) :
        for j in range(i + 1, prime_len - 1) :
            for k in range(j + 1, prime_len) :
                if primes[i]+primes[j]+primes[k] == n :
                    answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 33
ret1 = solution(n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 9
ret2 = solution(n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")