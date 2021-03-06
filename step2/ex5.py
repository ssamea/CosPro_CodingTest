#주어진 리스트의 순서를 뒤집으려고 합니다.
#예를 들어 주어진 리스트가 [1, 4, 2, 3]이면, 순서를 뒤집은 리스트는 [3, 2, 4, 1]입니다.

def solution(arr):
    left, right = 0, len(arr)-1
    while left<right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

#The following is code to output testcase.
arr = [1, 4, 2, 3]
ret = solution(arr)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")