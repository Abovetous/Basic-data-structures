Aaron = [5,3,3,5,4]
Bilbo = [2,2,2,3]
Johnny = [4,5,5,2]
Khendrik = [4,4,3]
Steven = [5,5,5,4,5]
students = {'Johnny' : Johnny, 'Bilbo' : Bilbo , 'Steve':Steven , 'Khendrik':Khendrik, 'Aaron':Aaron}
#a=средний балл
#b=сумма оценок
#c=количество оценок
#name= input("Введите ваше имя ")
#b=float(input("Скажите сумму ваших оценок "))
#c=float(input("Скажите сколько у вас оценок "))
#a= (b/c)
#print('Здравствуйте  ',name,' ваш средний бал ',a)
name = input('Введите ваше имя: ')
b=sum(students[name])
c=len(students[name])
a=(b/c)
print('Здравствуй ', name, 'твой средний бал',a)


