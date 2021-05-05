# XX 사전에는 대문자 알파벳 'A', 'E', 'I', 'O', 'U'를 사용해 만들 수 있는 길이가 5 이하인 모든 단어가 수록되어 있습니다.
# 어떤 단어가 XX 사전의 몇 번째 단어인지 알고 싶습니다

words = []

def create_words(lev, s):
    global words
    VOWELS = ['A', 'E', 'I', 'O', 'U']
    words.append(s)
    for i in range(0, 5):
        if lev < 5:
            create_words(lev+1, s + VOWELS[i])

def solution(word):
    global words
    words = []
    answer = 0
    create_words(0, '')
    for idx, i in enumerate(words):
        if word == i:
            answer = idx
            break
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
word1 = "AAAAE"
ret1 = solution(word1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

word2 = "AAAE"
ret2 = solution(word2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")