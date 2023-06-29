#1. 0이 되면 종료하는 프로그램
while True:
    x = int(input('숫자를 입력하세요 :'))
    if x ==0:
        break #break = 특정조건이 만족될때 break문 넣으면 그 즉시 종료하고 그 밖의 코드로 벗어남
    elif x!=0:
        print(f'입력된 숫자는 {x}입니다.')
        pass #아무것도 안하고 넘어감(특별한 작업이 없을 경우)
#2. 입력한 문자열에서 모음 제거하기
rep="".join('='*60)
print('\n',rep,'\n')
모음 = ['a','e','i','o','u']
str = str(input('Enter a string : '))
out = ''
for char in str:
    if char in 모음:
        pass
    else :
        out += char
print(out)
print('\n',rep,'\n')
#3. 숫자 맞추기 게임
import random as rd
#1부터 100사이의 임의의 수 선택
secretNum = rd.randint(1,100)

while True:
    숫자 = int(input('숫자를 입력하세요(1부터 100사이의 수) : '))
    if 숫자 > secretNum:
        print('Down👎🏻')
    elif 숫자<secretNum:
        print('UP👍🏻')
    else :
        print('Correct💖')
        break
print('\n',rep,'\n')    
#4. 두 주사위의 합이 7되면 이기는 주사위 게임
dice1 = rd.randint(1,6)
dice2 = rd.randint(1,6)
print('[주사위 게임]')
 
if dice1 + dice2 ==7:
    print(f'dice1 = {dice1}, dice2 = {dice2}' )
    print('YOU WIN!') 
        
else:
    print(f'dice1 = {dice1}, dice2 = {dice2}' )
    print('YOU DIED')
print('\n',rep,'\n')