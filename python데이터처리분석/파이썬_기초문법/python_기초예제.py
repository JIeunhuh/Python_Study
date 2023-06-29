#1.초를 입력하면 분과 초로 표시하는 프로그램
num = int(input('초를 입력하세요'))
n = num/60
s = num%60
print(f'{n}분 {s}초')

#2.분을 입력하면 일,시간,분으로 출력하는 프로그램을 만들어라
min = int(input('분을 입력하세요 : '))
day = min/(60*24)
hour = (min%(60*24))/60
m = (min%(60*24))%60
print(f'{day}일 {hour}시 {m}분')