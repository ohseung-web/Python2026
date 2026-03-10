name = input("이름을 입려하세요:")
height = float(input("키를 입력하세요(cm):"))
weight = float(input("현재 체중을 입력하세요(kg):"))

# 표준체중
st_weight = (height-100) * 0.9

# 비만도
obesity = (weight / st_weight) * 100
print("-" * 40)
# f-string : 소수 두째자리 까지 출력 .2f
print(f"{name}님의 비반도는 {obesity:.2f}%입니다.")
print("-" * 40)