# exercise 1
letter =input('Enter a letter :')

if letter in 'AEOIUaeiou':
    print('It is vowel:',letter)
else:
    print('It is consonant:', letter)


# exercise 2
num = int(input('Enter a number:'))

if num > 1000 and num < 2000:
    print('This number is between 1000 and 2000:',num)
elif num < 1000:
    print('less  number:',num)
elif num > 2000:
    print('more  number:',num)
else:
    print('excluded')

# exercise 2
num = int(input('Enter a number:'))

if num > 1000 and num < 2000:
    print('This number is between 1000 and 2000:')
elif num < 1000:
    print('This number is lower than 1000:')
elif num > 2000:
    print('This number is greater than 2000:')
else:
    print('excluded:')


# Exercise 3
a = float(input('Enter the first number'))
b = float(input('Enter the second number'))
c = float(input('Enter the third number'))
d=a+b+c
e=a*b*c
f=d*4

if a==b==c:
    print('product:',f)
elif a!=b!=c:
    print('sum:',d)
else:
    print('unknown:')

# exercise 4
a = int(input('Enter the 1st number:'))
b = int(input('Enter the 2nd number:'))
c = int(input('Enter the 3rd number:'))
d = int(input('Enter the 4th number:'))

if a > b and a > c and a > d:
    print('The largest number is',a)
elif b > a and b > c and b > d:
    print('The largest number is',b)
elif c > a and c > b and c >d:
    print('The lagest number is',c)
else:
    print('The largest number is',d)

    
# exercise 5
bto=int(input('Enter salary:'))
sala1 = 67000*0.24
sala2 = 97000*0.31
sala3 =97000*0.34
if (bto)<67000 and bto*0.24:
    print(sala1,'have to pay:')
elif int(bto)<97000 and bto*0.31:
    print(sala2,'have to pay:')
elif int(bto) > 97000 and bto*0.34:
    print(sala3,'have to pay:')

# Exercise 6
letter= input('Enter your letter betweeen 1 and 5:')

if len(letter)==1:
    print(f'{letter *6}')
elif len(letter)==2:
    print(f'{letter[1]}{letter[0]}')
elif len(letter)==3:
    print(f'{letter[2]}{letter[0]}{letter[1]}')
elif len(letter)==4:
    print(f'{letter[::-1]}')
elif len(letter)==5:
    print(letter[0],letter[1],letter[2],letter[3],letter[4],sep='t')

# Exercise 7

