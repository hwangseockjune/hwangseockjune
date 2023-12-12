# 4번
def solution(r1, r2):
    # r1, r2 안에 있는 격자점 개수를 세기 위한 변수 초기화
    count1 = 0
    count2 = 0

    # 첫 번째 원에 대한 격자점 개수 세기
    for x in range(1, r1 + 1):
        for y in range(1, r1 + 1):
            # 격자점까지의 거리의 제곱 계산
            distance_squared = x**2 + y**2
            # 원 안에 있는지 확인하여 count1 증가
            if distance_squared <= r1**2:
                count1 += 1

    # 두 번째 원에 대한 격자점 개수 세기
    for x in range(1, r2 + 1):
        for y in range(1, r2 + 1):
            # 격자점까지의 거리의 제곱 계산
            distance_squared = x**2 + y**2
            # 원 안에 있는지 확인하여 count2 증가
            if distance_squared <= r2**2:
                count2 += 1

    # 겹치는 부분에 해당하는 격자점 개수 계산
    spare = ((r2 - r1) + 1) * 4

    # 두 원의 반지름이 같으면 겹치는 부분이 없으므로 spare를 0으로 설정
    if r1 == r2:
        spare = 0

    # 최종 결과 계산
    answer = (count2 - count1) * 4 + spare
    return answer

print(solution(2, 3))