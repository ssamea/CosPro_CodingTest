def solution(arrA, arrB):
    arrA_idx = 0
    arrB_idx = 0
    arrA_len = len(arrA) #4
    arrB_len = len(arrB) #3
    answer = []
    while arrA_idx < arrA_len and arrB_idx < arrB_len: # 배열 A,B의 인덱스가 두 배열의 길이보다 작을때까지 반복
        if arrA[arrA_idx] < arrB[arrB_idx]:
            answer.append(arrA[arrA_idx])
            arrA_idx += 1
        else:
            answer.append(arrB[arrB_idx])
            arrB_idx += 1
    while arrA_idx < arrA_len:
        answer.append(arrA[arrA_idx])
        arrA_idx += 1
    while arrB_idx < arrB_len:
        answer.append(arrB[arrB_idx])
        arrB_idx += 1
    return answer


#The following is code to output testcase.
arrA = [-2, 3, 5, 9]
arrB = [0, 1, 5]
ret = solution(arrA, arrB);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")