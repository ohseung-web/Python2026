# 리스트 = 배열과 같은 역활을한다.
# 리스트 [숫자, 문자, 혼합] 사용가능
# 동적 => 고정길이가 아님
# 속도는 조금 느림

hores= []
# 리스트 추가하는 방법 
# append('추가할 문자') => 맨 뒤에 추가
# insert(인덱스번호, '추가 문자') => 인덱스 번호에 추가
hores.append('아이언맨')
hores.append('닥터 스트레인지')
hores.insert(1,'왕과 사는 남자')
print(hores[2])

# 리스트 삭제 : remove('삭제할 문자')
# 리스트 삭제 : del hores[0] => 0번째 데이터 삭제 됨
# 리스트 삭제 : pop() => 맨 마지막 데이터 삭제 됨
hores.remove('왕과 사는 남자')
print(hores)
del hores[1]
print(hores)
hores.pop()
print(hores)
hores.append("a")
hores.append("b")
hores.append("c")
hores.append("d")
print(hores)

# for문을 이용해서 출력하기
for title in hores:
    print(title,end=" ")

print()
# 리스트 슬라이스 하기
# hores[0:3] => 0번째 부터 3글자
# hores[:3] => 처음부터 3글자
# hores[3:] => 세번째 글자 부터 마지막까지
cut = hores[3:]
print(cut)

# 문제 ) movieTitle = []에 아래 영화 제목 4개를 추가하시오.
# 아이언맨, 토르, 헐크, 스칼렛 위치
movieTitle = []
movieTitle.append('아이언맨')
movieTitle.append('토르')
movieTitle.append('헐크')
movieTitle.append('스칼렛 위치')

# for movie in movieTitle:
#     print(movie, end=" ")

# 문제) movieTitle에서 '토르'가 존재하면 삭제하고 출력할 것
if '토르' in movieTitle:
    movieTitle.remove('토르')

movieTitle.sort(reverse=True)

for movie in movieTitle:
    print(movie, end=" ")
