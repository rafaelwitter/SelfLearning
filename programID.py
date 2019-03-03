import os
os.system("pause")
arq = open('programID.txt', 'w')
Drugs = ['Weed', 'Cocain', 'Lsd', 'Ecstasy']
name = str(input("Hello, Welcome!! Please, insert your name to keep browsering: "))
while name is '':
    print("Name cannot be null.")
    while True:
        name = str(input("What's your name? "))
        break
while name is not '':
    print("Hello ", name)
    try:
        age = int(input("Insert your age here: "))
    except(ValueError, BaseException):
        print("You must type your age with numbers.")
    else:
        if age >= 18:
            print ("You are a adult")
            Like_Alcohol = str(input("Do you like drinking alcohol? (Y/N): "))
            if Like_Alcohol == 'y':
                print("You are alcoholic.")
            Like_Drugs = str(input("Tell me another thing about you. Do you use any drugs? (Y/N): "))
            if Like_Drugs == 'y':
                print("Oh shit. You are a bastard!")
                print(Drugs)
                Drugs_Prefer = str(input("Wich one? "))
                if Drugs_Prefer == 'weed':
                    print("Okay, weed is good")
                elif Drugs_Prefer == 'cocain':
                    print("You are fuckin your life and your parents life")
                else:
                    Drugs_Prefer == 'lsd'
                    print("Fuckin HIPPIE")
                    if Drugs_Prefer == 'ecstasy':
                        id_DJ = str(input("You are DJ? (Y/N) :"))
                        if id_DJ == 'y':
                            name_DJ = str(input("Please insert your DJ name here: "))
                            cpf_DJ = int(input("Please inser you cpf here: "))
                            print(name_DJ, "\n", cpf_DJ, "\n", Drugs_Prefer, "\n I am calling the Pollice Officer!")
                        else:
                            job_normal = str(input("What do you do as job/hobbie? "))
                            if job_normal == 'hacker':
                                print("FuCk ThE SyStEm")
                            else:
                                job_normal == 'system anal'
                                print("Oh fuck")
            else:
                print("Good choice!")    
        if age <18:
            minor_Want = str(input("What do you want here? "))
            if minor_Want == 'hacker':
                print("Get OUT!")
                hacker_want = str(input("What do you wanna hack? "))
                if hacker_want == "win cash":
                    print("Calling 190")
            else:
                print("Ok, study hard.")
    break

"""
arq.write(name)
'\n'
arq.write("Teste")
'\n'
arq.write(Like_Alcohol)
'\n'
"""
arq.close()
