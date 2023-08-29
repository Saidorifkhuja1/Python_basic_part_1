# MyProfile app


info={'name':'','old':'','phone':'','e_mail':'','mail_indeks':'','mail_number':'','more':'',
      'orgnip':'','inn':'','accaunt':'','bank':'','bik':'','accaunt2':''}



def personal_informations():
    name =input('Enter name and first name:')
    info['name']=name
    old =input('Enter your old:')
    info['old']=old
    phone =input('Enter phone number:')
    info['phone']=phone
    e_mail =input('Enter e-mail: ')
    info['e_mail']=e_mail
    mail_indeks=input('Enter mail indeks:')
    info['mail_indeks']=mail_indeks
    mail_number =input('Enter mail number:')
    info['mail_number']=mail_number
    more =input('Enter more informations:')
    info['more']=more
    informations1()

def general_informations():
    orgnip =input('Enter ОРГНИП (must be 15 numbers):')
    info['orgnip']=orgnip
    inn =input('Enter ИНН: ')
    info['inn']=inn
    accaunt =input('Enter checking accaunt:')
    info['accaunt']=accaunt
    bank =input('Enter bank name:')
    info['bank']=bank
    bik =input('Enter БИК:')
    info['bik']=bik
    accaunt2 =input('Enter correspondent accaunt: ')
    info['accaunt2'] = accaunt2
    informations1()
def special_informations():

    print('Name:' ,info['name'])
    print('old:' ,info['old'])
    print('Phone number:' ,info['phone'])
    print('E-mail:' ,info['e_mail'])
    print('Indeks:' ,info['mail_indeks'])
    print('Adress:' ,info['mail_number'])
    informations2()

def all_informatioms():
    print('Name:',info['name'])
    print('old:', info['old'])
    print('Phone number:',info['phone'])
    print('E-mail:',info['e_mail'] )
    print('Indeks:',info['mail_indeks'])
    print('Adress:',info['mail_number'])
    print('ОРГНИП:' ,info['orgnip'])
    print('ИНН:' ,info['inn'])
    print('Checking ccaunt:' ,info['accaunt'])
    print('Bank:' ,info['bank'])
    print('БИК:' ,info['bik'])
    print('Correspond accaunt:' ,info['accaunt2'])
    informations2()



def informations1():
    print('\nSave or update information')
    print('-' * 30)
    x=input('\nPersonal informations  1'
            '\nBusiness informations  2'
            '\nMain menu  0 '
            '\n>>')
    if x=='1':
        personal_informations()
    elif x=='2':
        general_informations()
    elif x=='0':
        main()

def informations2():
    print('\nSaved information')
    print('-' * 30)
    x = input('\nSpecial informations  1'
              '\nAll informations  2'
              '\nMain menu  0 '
              '\n>>')
    if x=='1':
        special_informations()
    elif x=='2':
        all_informatioms()
    elif x=='0':
        main()






def main():
    print('\nProgram about informations')
    print('-'*30)
    inf=input('Save or update information 1'
              '\nSee saved informations  2'
              '\nFinish program 0'
              '\n >> ')
    if inf=='1':
        informations1()
    elif inf=='2':
        informations2()
    elif inf=='0':
        print('Program finished')


main()


