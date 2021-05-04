#1. arrA와 arrB의 길이가 다르면 false를 return 합니다.
#2. 두 리스트의 구성 성분이 달라 회전했을 때 같아질 가능성이 없다면 false를 return 합니다.
#3. arrA 리스트를 두 번 이어 붙여 길이가 2배인 리스트로 만듭니다.
#4. arrA의 부분 리스트 중 arrB와 같은 리스트가 있으면 true를, 그렇지 않으면 false를 return 합니다.

def func_a(arr):
    ret = arr + arr
    return ret

def func_b(first, second):
    MAX_NUMBER = 1001
    counter = [0 for _ in range(MAX_NUMBER)]
    for f, s in zip(first, second):
        counter[f] += 1
        counter[s] -= 1
    for c in counter:
        if c != 0:
            return False
    return True

def func_c(first, second):
    length = len(second)
    for i in range(length):
        if first[i : i + length] == second:
            return True
    return False

def solution(arrA, arrB):
    if len(arrA) != len(arrB):
        return False
    if func_b(arrA,arrB):
        arrA_temp = func_a(arrA)
        if func_c(arrA_temp,arrB):
            return True
    return False

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arrA1 = [1, 2, 3, 4]
arrB1 = [3, 4, 1, 2]
ret1 = solution(arrA1, arrB1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

arrA2 = [1, 2, 3, 4]
arrB2 = [1, 4, 2, 3]
ret2 = solution(arrA2, arrB2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")