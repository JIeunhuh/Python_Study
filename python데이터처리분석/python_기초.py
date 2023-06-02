name = 'Tom'
age = 20
cnt1=3; cnt2=2; cnt3=1;
res=1.23
sc=90
print(f'My name is {name} and I am {age} years old') #문자열 포매팅
print(f'I have {cnt1} apples, {cnt2} oranges, and {cnt3} banana')
print(f'The result is {res}')

repeat = '='
repeat_str = "".join(repeat*50)
print(repeat_str,'\n')
num1 = int(input('첫 번째 숫자를 입력하세요 : '))
num2 = int(input('두 번째 숫자를 입력하세요 : '))
num3 = int(input('세 번째 숫자를 입력하세요 : '))

max_num = num1

if max_num < num2:
    max_num = num2
    
if max_num < num3:
    max_num = num3

print('\n')   
print(f'입력한 숫자 중 가장 큰 수 는 {max_num}입니다.')
print(repeat_str,'\n')
num = int(input('사과의 개수를 입력하세요 : '))
price = int(input('사과의 가격을 입력하세요 : '))
tax = float(input('부가세율을 입력하세요 : '))/100

totalPrice = num * price
totaltax = totalPrice * tax

print(f'총 가격 : {totalPrice + totaltax:.2f}')


