#앞에서부터 읽을 때와 뒤에서부터 읽을 때 똑같은 단어 또는 문장을 팰린드롬(palindrome)이라고 합니다.
#소문자 알파벳, 공백(" "), 그리고 마침표(".")로 이루어진 문장이 팰린드롬 문장인지 점검하려 합니다
def solution(sentence):
    str = ''
    for c in sentence:
        if c != '.' and c != ' ':
            str += c
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size - 1 - i]:
            return False
    return True


# The following is code to output testcase. The code below is correct and you shall correct solution function.
sentence1 = "never odd or even."
ret1 = solution(sentence1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

sentence2 = "palindrome"
ret2 = solution(sentence2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")