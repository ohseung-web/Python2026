# a=[1,2,3,4,5] => 리스트, 일종의 배열과 같은 의미

#  i=1, i=2, i=3, i=4, i=5
for i in [1,2,3,4,5]:
    print("반복문")

# for 변수 in range(종료값) => 변수가 0 부터 종료값-1까지 반복됨
for i in range(5):
    print(f"{i}-1까지 반복")

# for 변수 in range(초기값, 종료값, 증감값)
# 1부터 5까지 반복하여 숫자 출력
# range(1,6,1) => 6을 지정한 이유는 6-1까지 반복되기때문
for i in range(1, 6, 1):
    print(f"{i}")