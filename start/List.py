
def space() :
    print()
    print()
    print()

#리스트
colors = ['red', 'blue', 'green']
print(colors[0])
print(colors[2])
print(colors[1])
print(len(colors))
print()
print()
print()
#슬라이싱(파이썬에서 처음 봄)
cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
print("1부터 5번 인덱스까지(6번 전까지)")
print(cities[1 : 6])
print("다른 사용법(5번부터 끝까지")
print(cities[5:])
print()
print()
print()

#리버스 인덱싱
print("리버스 인덱싱")
print(cities[-8 : ])
print()
print()
print()

#증가값
#슬라이싱에서는 시작 인덱스와 마지막 인덱스 외에 마지막 자리에 증가값을 넣을 수 있다.

print("증가값")
print("2칸씩 이동")
print(cities[::2])
print("역순으로 이동")
print(cities[::-1])
print()
print()
print()

#리스트의 연산 
print("리스트의 연산(더하기)")
colors1 = ['red', 'blue', 'green']
colors2 = ['orange', 'black', 'white']
print(colors1 + colors2)
print()
print("연산 후에도 각 변수의 길이에는 변화가 없음")
print(len(colors1))
print("다른 변수에 연산 결과를 할당하면 결과를 저장할 수 있음")
total_colors = colors1 + colors2
print(total_colors)
print()
print()
print()

print("리스트의 연산 : 곱셈 -> 같은 리스트를  n번 반복")
print(colors1 * 3)
print()
print()
print()

print("리스트의 연산 : in연산 -> 하나의 값이 리스트에 있는지 확인하는 함수")
print('blue' in colors1)
print('blue' in colors2)
print()
print()
print()

#리스트 추가 및 삭제
#append()함수 
print("append()함수 : 리스트 추가 함수")
colors.append('white')
print(colors)
space()
#extend()함수
print("extend()함수 : 리스트의 덧셈 연산과 같음")
colors.extend(['black', 'purple'])
print(colors)
space()

#insert()함수
print("insert() : 원하는 위치에 요소삽입")
colors.insert(1, 'cyan')
print(colors)
space()

#remove()함수
print("remove() : 특정 값을 지우는 기능(매개변수가 인덱스 값아님)")
colors.remove('cyan')
print(colors)
space()

#인덱스의 재할당과 삭제
print("특정 인덱스에 들어있는 값을 삭제")
del colors[0]
print(colors)
space()

#packing과 unpacking
print("패킹과 언패킹")
t = [1, 2, 3]
a , b, c = t
print(t, a, b, c)
print("언패킹한 a값")
print(a)
print("언패킹한 b값")
print(b)
print("언패킹한 c값")
print(c)
space()
#패킹과 언패킹은 특별한 개념은 아님
#패킹은 한 변수에 여러 개의 데이터를 할당하는것(대표적으로 리스트)
#언패킹은 한 변수에 여러개의 데이터가 들어있을 때, 그것을 각각의 변수로 반환하는것(a,b,c,)
#언패킹을 할 때, 리스트에 들어있는 요소의 개수와 언패킹에 쓰일 변수의 개수가 일치해야함(아니면 오류)

#이차원 리스트
print("이차원 리스트")
kor_score = [49, 10, 40, 29, 59]
math_score = [56, 12, 56, 25, 67]
eng_score = [58 , 29, 20, 59, 15]

midterm_score = [kor_score, math_score, eng_score]
print(midterm_score[0])
print(midterm_score[2])
print(midterm_score[1])
space()

#리스트의 메모리 관리 방식