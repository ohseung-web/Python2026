# 입력
name = input("학생 이름을 입력하세요: ")
korean = int(input("국어 점수를 입력하세요: "))
english = int(input("영어 점수를 입력하세요: "))
math = int(input("수학 점수를 입력하세요: "))

# 계산
total = korean + english + math
average = total / 3

# 학점 판별
if korean < 40 or english < 40 or math < 40:
    grade = "F (과락)"
    is_fail = True
else:
    is_fail = False
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

# 출력
print("─" * 37)
print(f"  이름  :  {name}")
print(f"  국어  :  {korean:>4}점")
print(f"  영어  :  {english:>4}점")
print(f"  수학  :  {math:>4}점")
print("─" * 37)
print(f"  총점  :  {total:>4}점")
print(f"  평균  :  {average:>7.2f}점")

if is_fail:
    print(f"  학점  :  {grade}")
    print("\n  한 과목이 40점 미만으로 과락 처리됩니다.")
else:
    print(f"  학점  :  {grade}")

print("─" * 37)

