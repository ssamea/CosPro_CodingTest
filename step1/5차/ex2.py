# 모든 벽의 위치와 높이를 담은 2차원 리스트 walls가 매개변수로 주어질 때, 물을 최대 몇 리터나 담을 수 있는지 return
def solution(walls):
    answer = 0

    # 물은 두 벽 사이의 거리 x 두 벽 중 낮은 벽의 높이리터 만큼 담을 수 있으며, 두 벽의 거리는 두 벽의 위치 차이입니다
    # walls의 각 원소는 [벽의 위치, 벽의 높이]

    for i in range(len(walls)):
        for j in range(i+1, len(walls)):
            area = 0
            if walls[i][1] < walls[j][1]: # 앞의 벽의 높이가 더 높다면 -> 원래 코드에서는 부등호가 >여서 값이 이상하게 나온거였음
                area = walls[i][1] * (walls[j][0] - walls[i][0]) # 더 낮은 뒷 벽 높이의 물을 담을 수 있다. 물은 두 벽 사이의 거리 x 두 벽 중 낮은 벽의 높이

            else: #앞의 벽 높이가 작다면
                area = walls[j][1] * (walls[j][0] - walls[i][0])

            if answer < area:
                answer = area
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
walls = [[1, 4], [2, 6], [3, 5], [5, 3], [6, 2]]
ret = solution(walls)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")