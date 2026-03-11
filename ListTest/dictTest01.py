# 딕셔너리 = 오브젝트 이다.
# 딕셔너리 => key : value 가 쌍으로 존재한다.
# 딕셔너리 출력하는 방법
# 딕셔너리 dict['key']로 절대 dict.key로 출력할 수 없다.
# phone_book = {'name':'홍길동','age':7,'class':'고급'}
phone_book = {}
phone_book['홍길동'] = '010-1234-5678'
phone_book['강감찬'] = '010-1234-5679'
phone_book['이순신'] = '010-1234-5670'

print(phone_book)
# 모든 key만 출력
print(phone_book.keys())
# 모든 value만 출력
print(phone_book.values())

# 문제) phone_book를 강감찬 010-1234-5679 이런 방향으로 출력시키시오.
#       단, for문 사용
for keyName in phone_book.keys():
    print(keyName,phone_book[keyName])

    