#사용자로부터 cm 단위의 길이를 입력 받는다.
#입력 값이 음수이면 "잘못 입력하였습니다"라는 메시지를 출력하고 양수이면
#길이를 인치로 변환하여 출력하는 프로그램을 작성하라. 1인치 = 2.54cm
cm = int(input('cm를 입력하세요 : '))
if cm<0 :
    print('잘못 입력함')
else :
    inch = cm * 2.54
    print(f'inch 변환 : {inch:.2f}')
    
repeat ='='
re = "".join(repeat*60)
#학점 출력하기
print('\n',re,'\n')
credit=int(input('학점 입력 : '))
if credit>=80 :
    print('졸업반입니다.')
elif 40<=credit<80 :
    print('2학년입니다')
else :
    print('1학년입니다.')
print('\n',re,'\n')

#현재시각 출력
now=int(input('시간을 입력하세요 : '))
시각=input('am/pm 입력 : ')
경과시간=int(input('몇 시간이 경과되었습니까? : '))

