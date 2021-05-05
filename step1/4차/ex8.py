# 다음과 같이 import를 사용할 수 있습니다.
# import math

# 1 이상 9 이하 숫자가 적힌 카드를 이어 붙여 숫자를 만들었습니다. 이때, 숫자 카드를 조합해 만든 수 중에서 n이 몇 번째로 작은 수인지 구하려 합니다.

def solution(card, n):
    # 여기에 코드를 작성해주세요.
    answer = []# 조합을 저장할 리스트
    card.sort() # 1 1 2 3

    # card 리스트를 방문하여 만들 수 있는 카드를 조합해야함
    for i in range(len(card)):
        for j in range(i+1,len(card)):
            for k in range(j+1,len(card)):
                for l in range(k+1,len(card)):
                    answer.append(str(card[i])+str(card[j])+str(card[k])+str(card[l]))

    print(answer)


    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card1 = [1, 2, 1, 3] # 숫자 카드를 담은 리스트
n1 = 1312 # 찾고자 하는 수
ret1 = solution(card1, n1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card2 = [1, 1, 1, 2]
n2 = 1122
ret2 = solution(card2, n2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")