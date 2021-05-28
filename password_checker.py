import random
print("A Strong password is minimum of 8 char and consists  of small letters capital letters numbers and special characters.")
Pass = input("Enter your password: ")

i = 8

small = 'abcdefghijklmnopqrstuvwxyz'
capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '123546890'
special_chr = '!@#$%^&*()_+|\{}[]'

if (len(Pass)) < i:
    print("Your Password is Weak")

    all = capital + small + number + special_chr + number

    length = int(input("Enter your password lenght(minimum 8): "))
    password = "".join(random.sample(all, length))

    print(password)

else:
    s = 0
    c = 0
    n = 0
    ch = 0

    #small = 'abcdefghijklmnopqrstuvwxyz'
    #capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #number = '123546890'
    #special_chr = '!@#$%^&*()_+|\{}[]'

    for j in range(len(Pass)):
        if Pass[j] in small:
            s = 1
        elif Pass[j] in capital:
            c = 1
        elif Pass[j] in number:
            n = 1
        elif Pass[j] in special_chr:
            ch = 1

    sum = s + c + n + ch

    if sum == 4:
        print("YOUT PASSWORD IS  STRONG")

    elif sum == 3:
        print("Your Password is MEDIUM")

    else:
        print("Your Password is WEAK")

        all = capital + small + number + special_chr + number

        length = int(input("Enter your password lenght(minimum 8): "))
        password = "".join(random.sample(all, length))

        print(password)

print(" ***HAVE A GOOD DAY!!!*** ❤\n ***By: AMARESH👨‍🎓")



