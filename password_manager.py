import random

def logo():
    print("""
  _____         _____ _______          ______  _____  _____    __  __          _   _          _____ ______ _____   
 |  __ \ /\    / ____/ ____\ \        / / __ \|  __ \|  __ \  |  \/  |   /\   | \ | |   /\   / ____|  ____|  __ \  
 | |__) /  \  | (___| (___  \ \  /\  / | |  | | |__) | |  | | | \  / |  /  \  |  \| |  /  \ | |  __| |__  | |__) | 
 |  ___/ /\ \  \___ \\___ \  \ \/  \/ /| |  | |  _  /| |  | | | |\/| | / /\ \ | . ` | / /\ \| | |_ |  __| |  _  /  
 | |  / ____ \ ____) ____) |  \  /\  / | |__| | | \ \| |__| | | |  | |/ ____ \| |\  |/ ____ | |__| | |____| | \ \  
 |_| /_/    \_|_____|_____/    \/  \/   \____/|_|  \_|_____/  |_|  |_/_/    \_|_| \_/_/    \_\_____|______|_|  \_\ 
                                                         @amaresh-git-dev                                                                                                                                                                
         """)

logo()

def choice():
    print("[+]A Strong password is minimum of 8 char and consists  of small letters capital letters numbers and special characters.[+]")
    print("[+]Enter your choice:")
    print("[+] 1 for password checking")
    print("[+] 2 for password generatation ")

    option = input().strip()

    if option == '1':

        def pass_check():

            small = 'abcdefghijklmnopqrstuvwxyz'
            capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            number = '123546890'
            special_chr = '!@#$%^&*()_+|\{}[]'
            all = capital + small + number + special_chr + number
            Pass = input("Enter your password: ")

            i = 8

            

            if (len(Pass)) < i:
                print("Your Password is Weak")

            else:
                s = 0
                c = 0
                n = 0
                ch = 0

                

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

        pass_check()

    elif option == '2':
        

        def pass_gen():
            def len():
                length = int(input("Enter your password lenght(minimum 8): ").strip())
                if length < 7:
                    print("Please choose your length above 7 chr", )
                    len()
                else:

                    
            
            
                    small = 'abcdefghijklmnopqrstuvwxyz'
                    capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    number = '123546890'
                    special_chr = '!@#$%^&*()_+|\{}[]'
                    all = capital + small + number + special_chr + number

                    
                    password = "".join(random.sample(all, length))
                    
                    print(password)
            len()
        pass_gen()
    else:
        print("invalid choice..", choice())  
choice()

