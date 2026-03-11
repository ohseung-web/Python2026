# 상품 이름 리스트
products = ['노트북', '마우스', '키보드', '모니터', '웹캠']

# 상품 재고 리스트
stocks = [15, 3, 8, 22, 5]
print("----- 재고 현황 -----")

# 배열의 길이  i<products.length
# len(products) => products의 길이를 숫자로 출력하는 함수
for i in range(len(products)):
    # 상품 이름 가져오기
    product = products[i]
    # 재고 수량 가져오기
    stock = stocks[i]
    # f-string 사용하면 해결
    # 출력하는 값을 담는 변수 msg이용해서 str()
    # 파이썬은 문자와 숫자를 하나로 나열할 수 없다.
    # 그러므로 str()함수를 이용해 숫자를 문자열로 변환하여 나열한다.
    msg = product +":" + str(stock) + "개"
    # 재고가 10개 미만이면 재고 부족 표시
    if stock < 10:
        msg = msg + " 재고 부족"
    print(msg)

# 총계 구하기
total = 0
# 재고 리스트를 하나씩 더하기
for stock in stocks:
    total += stock

print()
print(f"전체 재고 합계:{total:,}개")