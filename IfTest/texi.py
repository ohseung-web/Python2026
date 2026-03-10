# 입력
start = input("출발지를 입력하세요: ")
end = input("목적지를 입력하세요: ")
distance = float(input("이동 거리를 입력하세요(km): "))
ride_time = int(input("탑승 시간을 입력하세요(0~23): "))
child = input("어린이(13세 미만) 동반 여부를 입력하세요(예/아니오): ")

# 요금 계산
# 어린이 동반 여부 판별
if child == "예":
    base_fare = 0
else:
    base_fare = 4800

# 거리 요금 계산 (2km 초과분만 계산)
#  1km = 1000m / 100m => 10개
if distance > 2:
    extra_distance = distance - 2          # 초과 거리 3.5 - 2 => 1.5
    # distance_fare = int(extra_distance * 10) * 100  # 100m당 100원
    # 요금 = 거리 / 단위거리 * 단위요금
    distance_fare = int(extra_distance / 0.1) * 100  # 100m당 100원
else:
    distance_fare = 0

# 심야 할증 계산 (22시 이상 or 4시 이하)
subtotal = base_fare + distance_fare

if ride_time >= 22 or ride_time <= 4:
    night_fare = int(subtotal * 0.2)
    is_night = True
else:
    night_fare = 0
    is_night = False

# 최종 요금
total_fare = subtotal + night_fare

# 출력
print("=" * 42)
print(f" 택시 요금 안내")
print("=" * 42)
print(f"  출발지    : {start}")
print(f"  목적지    : {end}")
print(f"  이동거리  : {distance} km")
print(f"  탑승시간  : {ride_time}시")

if child == "예":
    print(f"  어린이 동반 : 기본요금 면제")

print("=" * 42)
print(f"  기본요금  : {base_fare:>8,} 원")
print(f"  거리요금  : {distance_fare:>8,} 원")

if is_night:
    print(f"  심야할증  : {night_fare:>8,} 원  (20% 적용)")
else:
    print(f"  심야할증  :        0 원  (해당없음)")

print("-" * 42)
print(f"  최종요금  : {total_fare:>8,} 원")
print("=" * 42)
