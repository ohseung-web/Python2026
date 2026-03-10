# 입력
month = int(input("방문 월을 입력하세요(1~12): "))
adult = int(input("성인 인원수를 입력하세요: "))
teen = int(input("청소년 인원수를 입력하세요: "))
child = int(input("어린이 인원수를 입력하세요: "))
senior = int(input("경로 인원수를 입력하세요: "))

# 기본 입장료
adult_price = 55000
teen_price = 40000
child_price = 28000
senior_price = 15000

# 총 인원
total_people = adult + teen + child + senior

# 어린이 3명 이상이면 어린이 무료
if child >= 3:
    child_price = 0
    is_child_free = True
else:
    is_child_free = False

# 각 구분별 소계
adult_total = adult_price * adult
teen_total = teen_price * teen
child_total = child_price * child
senior_total = senior_price * senior

# 전체 소계
subtotal = adult_total + teen_total + child_total + senior_total

# 성수기 여부 판별 + 단체 할인 적용
if month == 7 or month == 8:
    is_peak = True
    discount = 0
else:
    is_peak = False
    if total_people >= 5:
        discount = int(subtotal * 0.1)
    else:
        discount = 0

# 최종 금액
total_price = subtotal - discount

# 출력
print("=" * 42)
print(f" 놀이공원 입장권 계산서")
print("=" * 42)

if is_peak:
    print(f"  방문 월    : {month}월 (성수기)")
else:
    print(f"  방문 월    : {month}월 (비수기)")

print("=" * 42)

if is_child_free:
    print(f"  성인   {adult}명 : {adult_total:>10,} 원")
    print(f"  청소년 {teen}명 : {teen_total:>10,} 원")
    print(f"  어린이 {child}명 : {child_total:>10,} 원 (무료!)")
    print(f"  경로   {senior}명 : {senior_total:>10,} 원")
else:
    print(f"  성인   {adult}명 : {adult_total:>10,} 원")
    print(f"  청소년 {teen}명 : {teen_total:>10,} 원")
    print(f"  어린이 {child}명 : {child_total:>10,} 원")
    print(f"  경로   {senior}명 : {senior_total:>10,} 원")

print("=" * 42)
print(f"  소계       : {subtotal:>10,} 원")

if is_peak:
    print(f"  단체 할인  :          0 원 (성수기 할인 미적용)")
else:
    if total_people >= 5:
        print(f"  단체 할인  : {-discount:>10,} 원 (10%)")
    else:
        print(f"  단체 할인  :          0 원 (5명 미만)")

print("-" * 42)
print(f"  최종 금액  : {total_price:>10,} 원")
print("=" * 42)
print(f"  총 인원 : {total_people}명")
print("=" * 42)