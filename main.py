#Посчитайте манулов от 10 до 100
for i in range (1,101):
    if i==1:
        print(i,"манул")
    elif i % 10 == 2 or i % 10 ==3 or i % 10 == 4:
        print (i, "манула")
    elif i==21 or i==31 or i==41 or i==41 or i==51 or i==61 or i==71 or i==81 or i==91:
         print (i, "манул")
    else:
        print(i,"манулов")
