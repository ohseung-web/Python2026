# code의 값을 input()으로 키보드로부터 입력 받는다.
code = int(input("상태코드를 입력하세요:"))

a = "123"
print(len(a))



# 다중 if ~ elif ~ elif ~ else
if code == 200:
    print("상태: 200 ok - 요청 성공")
elif code == 201:
    print("상태: 201 Created - 리소스 생성 성공")   
elif code == 400:
    print("상태: 400 Bad Request - 잘 못된 요청")   
elif code == 401:
    print("상태: 401 Unauthorized - 인증  필요")   
elif code == 403:
    print("상태: 403 Forbidden - 접근 권한 없음")   
elif code == 404:
    print("상태: 404 Not Found - 리소스 없음")
elif code == 500:
    print("상태: 500 Internal Server error - 서버 내부 오류")
else:
    print(f"상태 : {code} Unkonwn Status Code")    


# 200이상이고 299이하면 성공 계열
if code >=200 and code<=299:
    print("계열 : 2xx - 성공")
# 400 이상이고 499이하면 클라이언트 오류
elif code>=400 and code<=499:
    print("계열 : 4xx - 클라이언트 오류")
# 500 이상이고 599이하면 서버 오류
elif code>=500 and code<=599:
    print("계열 : 5xx - 서버 오류")  