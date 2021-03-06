"""
6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★

예시
<입력>
숫자를 입력하세요 : 5

<출력>
    ★
   ★★
  ★★★
 ★★★★
★★★★★  
 ★★★★
  ★★★
   ★★
    ★
"""

num = int(input("숫자를 입력하세요 : "))  # 기준이 될 가운데 수 입력단

for i in range(1, num + 1):  # 1부터 입력된 num + 1 미만의 수
    # num 을 바로 써주게 되면 num - 1의 수가 나오게 된다.
    print(" " * (num - i), "★" * i)

for j in range(1, num + 1):  # 1부터 입력된 num + 1 미만의 수
    print(" " * j, "★" * (num - j))
