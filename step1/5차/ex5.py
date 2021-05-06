# 다음과 같이 import를 사용할 수 있습니다.
# import math


# 캐릭터는 자신과 공격력이 같거나 자신보다 공격력이 작은 몬스터에게 이깁니다. 내가 가진 캐릭터가 최대 몬스터 몇 마리를 이길 수 있는지 구하려 합니다. 단, 한 캐릭터는 한 번만 싸울 수 있습니다.
def solution(enemies, armies):
    # 여기에 코드를 작성해주세요.
    answer = 0
    cnt=[0 for i in range(len(armies))] # 이긴 카운팅 횟수를 체크하려는 변수


    for i in range(len(armies)):
        for j in range(len(enemies)):
            if armies[i] >= enemies[j]:
                if enemies[j] == 0:
                    pass

                else:
                    answer+=1
                    enemies[j]=0

    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
enemies1 = [1, 4, 3]
armies1 = [1, 3]
ret1 = solution(enemies1, armies1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

enemies2 = [1, 1, 1]
armies2 = [1, 2, 3, 4]
ret2 = solution(enemies2, armies2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")