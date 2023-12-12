# 3번
def solution(age):
    answer = ''
#최종 결과를 저장할 문자열 정의
    alpha = 'abcdefghij'
#0~9까지의 숫자에 대응되는 알파벳 문자열 정의
    for i in str(age):
#매개변수 age를 문자열로 변환하고 i 에 대입하며 age의 길이 끝까지 순회
        answer += alpha[int(i)]
#순회하는 동시에 숫자로 변환된 i에 대응되는 알파벳을 찾아 answer에 추가하며 answer을 완성한다.
   
    return answer
#answer값을 리턴한다

print(solution(98))