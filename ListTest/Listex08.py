courses = [
    {'subject': 'Python 프로그래밍\t', 'score': 92, 'credit': 3},
    {'subject': 'SpringBoot 개발\t\t', 'score': 88, 'credit': 3},
    {'subject': 'React 프론트엔드\t', 'score': 76, 'credit': 2},
    {'subject': '데이터베이스\t\t', 'score': 95, 'credit': 3},
    {'subject': '알고리즘\t\t', 'score': 68, 'credit': 2}
]
# 점수에 따라 학점 계산하기
for cour in courses:
    score = cour['score'] #현재 과목점수 가져오기
    if score>=95:
        grade="A+"
        point=4.5
    elif score>=90:
        grade="A"
        point=4.0
    elif score>=85:
        grade="B+"
        point=3.5
    elif score>=80:
        grade="B"
        point=3.0
    elif score>=75:
        grade="C+"
        point=2.5
    elif score>=70:
        grade="C"
        point=2.0
    elif score>=60:
        grade="D"
        point=1.0
    else:
        grade="F"
        point=0
    # 계산된 grade와 point 딕셔너리 추가
    cour['grade']=grade
    cour['point']=point    

# 성적표 출력
print("---- 성적표 -----")
print(f"과목\t\t\t점수\t학점\t학점포인트\t이수학점")
print("-"*60)
# 각 과목 정보 출력
for cour in courses:
    print(f"{cour['subject']}\t{cour['score']}점\t{cour['grade']}\t{cour['point']}\t{cour['credit']}학점")

print()

# GPA 계산
creditTotal = 0
pointTotal =0
for cour in courses:
    # 총 학점 합계
    creditTotal += cour['credit']
    # (학점포인트 * 학점)
    pointTotal += (cour['point']*cour['credit'])
gpa = pointTotal / creditTotal    
print()
print(f"GPA : {gpa} / 4.50 (총 {creditTotal}학점)")

# 학점별 과목 수 계산
# 학점 분포
gradeCount = {}
for cour in courses:
     grade = cour['grade']
    # 이미 학점이 존재하면 +1, 아니면 1
     if grade in gradeCount:
       gradeCount[grade] += 1
     else:
       gradeCount[grade] = 1    

print("학점 분포 :",gradeCount)