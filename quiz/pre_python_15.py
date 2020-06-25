"""
15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오.
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""


id_card = input("주민등록번호 : ")    # 주민등록번호 입력란

id_card = id_card.split("-")[1]     # split 분할 메소드 구분자로 하이픈 사용

if id_card[0] == "1" or id_card[0] == "3":      # 하이픈 다음 0번째 수가 1 이나 3 이라면
    print("남자")     # 남자 출력
elif id_card[0] == "2" or id_card[0] == "4":    # 하이픈 다음 0번째 수가 2 나 4 라면
    print("여자")     # 여자 출력
