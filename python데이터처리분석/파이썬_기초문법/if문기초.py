num=int(input('입력해라 : '))
res='10보다 큽니다'

if num > 10 :
    res
else :
    '10보다 작거나 같습니다'
print('\n',res)

repeat='='
print('\n',"".join(repeat * 60),'\n')

#성적 입력받아 학점을 출력하는 프로그램
print('[성적 계산기]','\n')
국어 = int(input('국어 성적을 입력하세요 : '))
영어 = int(input('영어 성적을 입력하세요 : '))
수학 = int(input('수학 성적을 입력하세요 : '))

국어 = (국어*0.4)
영어 = (영어*0.4)
수학 = (수학*0.2)

sum = 국어+수학+영어
print('\n[성적 결과]')
print(f'총 평균 점수 : {sum:.2f}')

print('학점 : ')
if sum>=90:
    print('A')
elif sum>=80:
    print('B')
elif sum>=70:
    print('C')
elif sum>=60:
    print('D')
else : print('F')
print('\n',"".join(repeat * 60),'\n')