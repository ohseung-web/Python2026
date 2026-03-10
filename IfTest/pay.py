# 입력
name = input("이름을 입력하세요: ")
hourly_wage = int(input("시급을 입력하세요(원): "))
work_hours = float(input("하루 근무 시간을 입력하세요(h): "))
work_days = int(input("근무 일수를 입력하세요(일): "))
start_time = int(input("근무 시작 시간을 입력하세요(0~23): "))

# 야간 여부 판별
if start_time >= 22 or start_time <= 6:
    real_wage = int(hourly_wage * 1.5)  # 야간 시급
    is_night = True
else:
    real_wage = hourly_wage
    is_night = False

# 주간 총 근무시간 계산
total_hours = work_hours * work_days

# 기본급 계산
basic_pay = int(real_wage * total_hours)

# 주휴수당 계산 (주 15시간 이상 근무 시)
if total_hours >= 15:
    weekly_allowance = int(real_wage * work_hours)
    is_weekly = True
else:
    weekly_allowance = 0
    is_weekly = False

# 세금 및 실수령액 계산
gross_pay = basic_pay + weekly_allowance         # 세전 총급여
tax = int(gross_pay * 0.033)                     # 세금 3.3%
net_pay = gross_pay - tax                        # 실수령액

# 출력
print("=" * 42)
print(f"  급여 명세서")
print("=" * 42)
print(f"  이름        : {name}")
print(f"  시급        : {hourly_wage:>8,} 원")
print(f"  근무시간    : {total_hours:>5} 시간 ({work_hours}h × {work_days}일)")

if is_night:
    print(f"  야간 근무   :  해당 있음 (시급 {real_wage:,}원 적용)")
else:
    print(f"  야간 근무   :  해당 없음")

if is_weekly:
    print(f"  주휴수당    :  해당 있음")
else:
    print(f"  주휴수당    :  해당 없음 (주 15시간 미만)")

print("=" * 42)
print(f"  기본급      : {basic_pay:>8,} 원")
print(f"  주휴수당    : {weekly_allowance:>8,} 원")
print(f"  세금(3.3%) : {tax:>8,} 원")
print("-" * 42)
print(f"  실수령액    : {net_pay:>8,} 원")
print("=" * 42)