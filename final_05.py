# 5번
def solution(numbers):
    # 각 숫자를 문자열로 변환하여 리스트에 저장
    numbers = list(map(str, numbers))
   
    # 각 숫자를 3번 반복하여 새로운 리스트에 추가
    new_numbers = []
    for num in numbers:
        repeated_num = num * 3
        new_numbers.append(repeated_num)
        # 각 숫자를 3번 반복하여 리스트에 추가

    # 새로운 리스트를 내림차순으로 정렬
    result_numbers = sorted(new_numbers, reverse=True)
   
    # 숫자의 길이에 따라 3, 6, 9의 배수에 해당하는 부분을 잘라내어 수정된 리스트 생성
    for i in range(0, len(result_numbers)):
        if len(result_numbers[i]) == 3:
            result_numbers[i] = result_numbers[i][0]
            # 숫자의 길이가 3이면 가장 첫 번째 숫자로 변경
        elif len(result_numbers[i]) == 6:
            result_numbers[i] = result_numbers[i][0] + result_numbers[i][1]
            # 숫자의 길이가 6이면 첫 번째와 두 번째 숫자로 변경
        elif len(result_numbers[i]) == 9:
            result_numbers[i] = result_numbers[i][0] + result_numbers[i][1] + result_numbers[i][2]
            # 숫자의 길이가 9이면 첫 번째, 두 번째, 세 번째 숫자로 변경

    # 수정된 리스트의 숫자들을 합쳐서 문자열로 반환
    result_string = "".join(result_numbers)
    return result_string

print (solution( [8, 30, 17, 2, 23]))
