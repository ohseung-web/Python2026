# 함수안에서 전역변수 사용하기
def cal_area(radius):
    global area 
    area = 3.14 * radius ** 2
    return

area = 0 #전역변수 임
r = float(input("반지름 입력 :"))
cal_area(r)
print(area)
