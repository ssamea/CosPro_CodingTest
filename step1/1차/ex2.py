def func_a(string, length): # string=110, length=5라면
    padZero = ""
    padSize = length - len(string)


    for i in range(padSize):
        padZero += "0"
    return padZero + string


def solution(binaryA, binaryB):
    max_length = max(len(binaryA), len(binaryB)) # ex 10010 ,110이면 max_length=5
    binaryA = func_a(binaryA, max_length)
    binaryB = func_a(binaryB, max_length)

    hamming_distance = 0
    for i in range(max_length):
        if binaryA[i] !=binaryB[i]:
            hamming_distance += 1
    return hamming_distance


# The following is code to output testcase.
binaryA = "10010"
binaryB = "110"
ret = solution(binaryA, binaryB)

# Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")