# 2번
def solution(letter):
    # Morse 코드에 대응하는 알파벳을 담은 딕셔너리
    morse = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z'
    }
   
    # 결과를 저장할 문자열 초기화
    answer = ""

    # 입력된 Morse 코드 문자열을 공백을 기준으로 분리
    codes = letter.split()

    # 분리된 Morse 코드에 대응하는 알파벳을 찾아 결과에 추가
    for i in codes:
        answer += morse[i]

    return answer
print(solution('.... .-- .- -. --.'))