sum=0
while True:
    num = int(input("숫자를 입력하세요 : "))
    if num==0:
        break
    sum += num
    print('입력한 값들의 합 : ', sum)
    
rep = "".join('='*60)
print('\n',rep,'\n')

fruits = ["apple",'banana','cherry']
for fruit in fruits:
    
    print(fruit)
    
print('\n',rep,'\n')

text = 'python' #문자열의 각 문자를 순차적으로 출력하기
for char in text:
    print(char)

print('\n',rep,'\n')   

for i in range(1,11):
    print(i,end=" ") #print() 는 기본적으로 개행문자이기 때문에 end=옵션을 통해 바꿔줄 수 있음
    
print('\n',rep,'\n')   
#1. 3의 배수와 5의 배수의 합 구하기
print('[3의 배수와 5의 배수의 합 구하기]')
num = int(input('양의 정수 n을 입력하세요 : '))
sum=0
for i in range(1,num+1):
    if i%3==0 or i%5==0:
        sum += i 
print('\n[결과]')
print(f'1부터 {num}까지의 자연수 중에서 3의 배수와 5의 배수의 합 : {sum}')
print('\n',rep,'\n')
#2. 최댓값 최솟값 찾기
num = []
max = int(0) #아주 작은값
min = 10000000 #아주 큰값?
for i in range(5):
    val = int(input(f'{i+1}번째 숫자를 입력하세요 : '))
    num.append(val)
    #.append() 이용해서 값 추가
    if min > int(num[i]):
        min=num[i]
    if max < int(num[i]):
        max = num[i]
print(f'최댓값 : {max}')
print(f'최솟값 : {min}')

print('\n',rep,'\n')

#3. 숫자의 합이 100보다 작을때까지 입력
sum=0
while sum<100:
    num = int(input('숫자를 입력하세요 : '))
    sum += num
print(f'입력받은 숫자들의 합 : {sum}')
print('\n',rep,'\n')
#4. 피보나치 수열 n번째 항 출력하기
num = int(input('몇 번째 항을 출력할까요? '))
if num==1 or num==2:
    res = 1
else :
    a,b=1,1
    for _ in range(3,num+1): #반복변수의 값을 무시 ; 반복변수를 사용하지 않을때
        res = a + b #초기 res값 계산
        a , b = b , res #다음 항 값
print(f'피보나치 수열의 {num}번째 항은 {res}입니다.')