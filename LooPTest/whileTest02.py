
# 문제) 1부터 50까지의 합을 구하기
# 단, while문 이용
count = 1
sum = 0
while count <= 50:
    sum += count
    count += 1

print(f"합계 : {sum}")

# 다중 while문을 이용해서 구구단 2단 ~ 9단까지출력
# i = 1 ~ 9
# dan = 2 
# i=1
dan = 2
while dan<=9:
    i = 1
    while i <=9:
        print(f"{dan}*{i}={dan*i}")
        i += 1

    print()
    dan += 1
       

