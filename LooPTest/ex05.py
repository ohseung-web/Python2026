# 요구사항
#   - 측정 횟수 n을 입력받고, n개의 응답시간(ms)을 입력받으세요.
#   - 각 응답에 대해 등급을 판별하여 출력하세요.
#     · 100ms 이하  : FAST
#     · 101~300ms  : NORMAL
#     · 301~1000ms : SLOW
#     · 1001ms 이상 : CRITICAL
#   - 전체 측정 후 평균 응답시간, 최대 응답시간, 최소 응답시간 출력
#   - CRITICAL 비율이 10% 초과 시 'SLA 위반! 서버 점검이 필요합니다.' 출력
#   - (힌트: 최대/최소값은 첫 번째 값으로 초기화 후 비교하여 갱신)

# 응답시간
n = int(input("측정 횟수:"))

# 전체응답 시간
total_time = 0
# critical 상태 개수
critical_cnt = 0

# for i in range(초기값, 종료값, 증감)
# for i in range(종료값) => 종료값-1까지
for i in range(1,n+1):
    # i뻔째 응답시간 입력 => ms = 5
    ms = int(input(f"응답시간 {i} (ms):"))
    # 전체 합계 + 응답시간
    total_time += ms
    # 최대값 / 최소값
    # 첫 번째  입력값을 기준으로 설정
    if i == 1:
       max = ms
       min = ms 
    else:
        # 최대값 갱신
        if ms > max:
            max = ms
        # 최소값 갱신
        if ms < min:   
            min = ms 
    # 응답 속도 상태 판별
    if ms <= 100:
        print("FAST")
    elif ms <= 300:
        print("NORMAL")
    elif ms <= 1000:
        print("SLOW")
    else:
        print("CRITICAL")
        critical_cnt += 1

# 평균 응답시간
avg = total_time  / n
print("--- 측정 결과 ---")
print(f"평균 응답시간: {avg:.1f}")
print(f"최대 응답시간: {max}")
print(f"최소 응답시간: {min}")

# SLA 검사
if critical_cnt / n > 0.1:
    print("SLA 위반! 서버 점검이 필요합니다.")