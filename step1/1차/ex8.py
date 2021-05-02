def solution(N, votes):
    vote_counter = [0 for i in range(N + 1)] # 각 후부의 투표수를 카운터하기위한 배열, 후보번호는 1번부터 있으므로 n+1
    for i in votes: # 투표 결과 리스트 방문
        vote_counter[i] += 1 # 체크


    max_val = max(vote_counter)


    answer = []
    for idx in range(1, N + 1):
        if vote_counter[idx] == max_val:
            answer.append(votes[idx])
    return answer


# The following is code to output testcase. The code below is correct and you shall correct solution function.
N1 = 5
votes1 = [1, 5, 4, 3, 2, 5, 2, 5, 5, 4]
ret1 = solution(N1, votes1)

# Press Run button to receive output.
print("Solution: return value of the function is ", ret1, " .")

N2 = 4
votes2 = [1, 3, 2, 3, 2]
ret2 = solution(N2, votes2)

# Press Run button to receive output.
print("Solution: return value of the function is ", ret2, " .")