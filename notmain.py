import random

User = int(input('Введите количество символов в пароле: '))

UserNumberTwo = int(input('Введите количество точек: '))

alphar = ''

for i in range(1,UserNumberTwo + 1):
    alphar = ''
    
    for i2 in range(1,User + 1):

        list = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

 


        alphar = alphar + random.choice(list )

    print(f'{i}. {alphar}' )