
# 다중 for문을 이용해서 구구단 2단 ~ 9단 출력
for i in range(2,10):
    print(f"-----{i}단 시작-----")
    for j in range(1,10):
        print(f"{i} X {j} = {i*j}")
    # 한단이 끝날때 마다 빈 줄 출력
    print()
