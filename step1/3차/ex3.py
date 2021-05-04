#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(bishops):
    #여기에 코드를 작성해주세요.
    answer = 0
    # 방향을  위한 변수 비숍은 기본적으로 좌우상하 대각선
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]

    cx = ord(bishops[0]) - ord("A")  # 행이 알파벳으로 되어있어서 그 좌표값을 얻기 위해 ord함수를 이용 ex) A7이면 cx=A의 ASCII값 65 -> 65-65=0
    cy = ord(bishops[1]) - ord("0") - 1  # 배열의 인덱스는 0이기 때문에 -1을 해준거
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")