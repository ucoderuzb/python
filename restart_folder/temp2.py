print("           Bu dastur kodlangan, iltimos kodni yozing.")

code = str(input('Kodni kiriting: '))
if code == '04302008':
    print("Bu",code,"kod to'g'ri")
    
    
    roof = input("Ismingizni kiriting: ")
    if roof == "Umidjon":
        print("Tug'ilgan kuni: 30.")
        print("Tug'ilga oyi: 04.")
        print("Tug'ilgan yili: 2008.")
        
        
    elif roof == "Og'abek":
        print("Tug'ilgan kuni: 9.")
        print("Tug'ilga oyi: 03.")
        print("Tug'ilgan yili: 2009.")
        
    else:
         print(roof,"nomli ism dasturda mavjud emas.")
         
         
else:
    print("Bu",code,"noto'g'ri kod")

while roof:
    roof = input("Ismingizni kiriting: ")
    if roof == "Umidjon":
        print("Tug'ilgan kuni: 30.")
        print("Tug'ilga oyi: 04.")
        print("Tug'ilgan yili: 2008.")
        
        
    elif roof == "Og'abek":
        print("Tug'ilgan kuni: 9.")
        print("Tug'ilga oyi: 03.")
        print("Tug'ilgan yili: 2009.")
        
    else:
         print(roof,"nomli ism dasturda mavjud emas.")