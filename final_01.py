# 1번문제
def solution(str1, str2):
    # 결과를 저장할 변수 초기화
    answer = 0
    # str1이 str2에 포함되어 있는지 여부 확인
    if str1 in str2:
        # 포함되어 있으면 answer에 1 할당
        answer = 1
    else:
        # 포함되어 있지 않으면 answer에 0 할당
        answer = 0
    return answer

print(solution("gju", "hwangjune"))