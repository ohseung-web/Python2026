# 주문 데이터 (리스트 안에 딕셔너리)
orders = [
    {'id': 1, 'product': '노트북', 'amount': 1200000, 'status': 'PAID'},
    {'id': 2, 'product': '마우스', 'amount': 35000, 'status': 'PENDING'},
    {'id': 3, 'product': '모니터', 'amount': 450000, 'status': 'PAID'},
    {'id': 4, 'product': '키보드', 'amount': 89000, 'status': 'CANCELLED'},
    {'id': 5, 'product': '웹캠', 'amount': 75000, 'status': 'PAID'}
]

# 주문한 상품을 저장할 새로운 리스트 
paid_orders =[]
# status ='paid' 인 자료를 -> paid_orders담는다
# for 작명 in 리스트 이름
# order에는 orders의 인덱스 첫 번째 값 부터 순서대 담긴다.
# 고로 현재는 {'id': 1, 'product': '노트북', 'amount': 1200000, 'status': 'PAID'}
for order in orders:
    # 딕셔너리는 반드시 key값을 읽어야 value를 출력할 수 있다.
    if order['status'] == 'PAID':
        # paid_orders리스트에 append()로 상품을 하나 추가한다.
        paid_orders.append(order)

# 조건에 만족하는 상품 저장 결과 
# paid_orders =[
#     {'id': 1, 'product': '노트북', 'amount': 1200000, 'status': 'PAID'},
#     {'id': 3, 'product': '모니터', 'amount': 450000, 'status': 'PAID'},
#     {'id': 5, 'product': '웹캠', 'amount': 75000, 'status': 'PAID'}
# ]        
# 출력문
print(" ---- 결제 주문 완료 -----")
total = 0
for order in paid_orders:
    print(f"{order['id']}번 주문 / 상품:{order['product']} / 금액:{order['amount']:,}")
    # 총금액 계산
    total += order['amount']

print(f"\n총 결제 금액:{total:,}원")