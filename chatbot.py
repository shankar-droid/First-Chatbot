def greet_and_introduce():
    responses = "Hi I am chatbot. I can help you to know about SmartPhones and its models"
    print(responses)

def show_menu():
    print("These are the companies")
    print("1.Apple" )
    print("2.Samsung" )
    print("3.Xiaomi" )
    print("4.Vivo")
    print("5.Realme")
    return int(input("enter your choice [1-5]: "))

def apple():
    print("These are the models")
    print('1.iPhone 11 Pro Max.')
    print('2.iPhone 11.')
    print('3.Apple iPhone Xs Max.')
    return int(input("enter your choice[1-3]: "))

def apple_iphone11promax():
    print("Model Name : iPhone 11 Pro Max")
    print("price:₹1,24,599")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 64 GB")
    print("Camera :  12MP + 12MP + 12MP")
    print("Display Size :16.51 cm (6.5 inch)")
    print("Resolution :2688 x 1242 Pixels")
    return("colour: Midnight Green")

def apple_iphone11():
    print("Model Name : iPhone 11")
    print("price:₹68,721")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 64 GB")
    print("Camera :  12MP + 12MP")
    print("Display Size :15.49 cm (6.1 inch)")
    print("Resolution : 1792 x 828 Pixels")
    return("colour: Black,Purple, Green")

def apple_iphonexsmax():
    print("Model Name : iPhone XS Max")
    print("price:₹1,09,999")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 512 GB")
    print("Camera :  12MP + 12MP")
    print("Display Size :16.51 cm (6.5 inch)")
    print("Resolution :2688 x 1242 Pixels")
    return("colour: Space Grey")
	
def samsung():
    print("These are the models")
    print('1.Samsung Galaxy Note 20 Ultra 5G.')
    print('2.Samsung Galaxy S20+')
    print('3.Samsung Galaxy S20 Ultra.')
    return int(input("enter your choice[1-3]: "))

def samsung_galaxynote20ultra5g():
    print("Model Name : Galaxy Note 20 Ultra 5G")
    print("price:₹1,04,999")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 256 GB")
    print("Camera :  108MP + 12MP + 12MP")
    print("Display Size :17.53 cm (6.9 inch)")
    print("Resolution :3088 x 1440 Pixels")
    return("colour: Mystic Black,Mystic Bronze")

def samsung_galaxys20():
    print("Model Name : Galaxy S20+")
    print("price:₹83,000")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 128 GB")
    print("Camera :  64 MP + 12 MP +12 MP + VGA Depth Camera")
    print("Display Size :17.02 cm (6.7 inch)")
    print("Resolution : 3200 x 1440 Pixels")
    return("colour: Cosmic Black,Cosmic Gray")

def samsung_galaxys20ultra():
    print("Model Name : Galaxy S20 Ultra")
    print("price:₹97,999")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 128 GB")
    print("Camera :  108 MP + 48 MP + 12 MP + VGA Depth Camera")
    print("Display Size :17.53 cm (6.9 inch)")
    print("Resolution :3200 x 1440 Pixels")
    return("colour: Cosmic Black")

def xiaomi():
    print("These are the models")
    print('1.Redmi Note 9 Pro Max.')
    print('2.Redmi Note 9 Pro.')
    print('3.Redmi K20 Pro.')
    return int(input("enter your choice[1-3]: "))

def xiaomi_redminote9promax():
    print("Model Name : Redmi Note 9 Pro Max")
    print("price:₹18,000")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 64 GB")
    print("Camera :  64MP Rear Camera")
    print("Display Size :16.94 cm (6.67 inch)")
    print("Resolution :2400 x 1080 Pixels")
    return("colour: Champagne Gold")

def xiaomi_redminote9pro():
    print("Model Name : Redmi Note 9 Pro")
    print("price:₹17,260")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 128 GB")
    print("Camera : 48MP + 8MP + 5MP + 2MP")
    print("Display Size :16.94 cm (6.67 inch)")
    print("Resolution : 2400 x 1080 pixel")
    return("colour: Glacier White")

def xiaomi_redmik20pro():
    print("Model Name : iPhone XS Max")
    print("price:₹22,999")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 256 GB")
    print("Camera :  48MP + 13MP + 8MP")
    print("Display Size :16.23 cm (6.39 inch)")
    print("Resolution :2340 x 1080  Pixels")
    return("colour: Carbon Black,Flame Red")

def vivo():
    print("These are the models")
    print('1.Vivo X50 Pro.')
    print('2.Vivo Y20.')
    print('3.Vivo V17.')
    return int(input("enter your choice[1-3]: "))

def vivo_vivox50pro():
    print("Model Name : X50 Pro")
    print("price:₹49,990")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 256 GB")
    print("Camera :  48MP + 13MP + 8MP + 8MP")
    print("Display Size :16.66 cm (6.56 inch)")
    print("Resolution :2376 x 1080 Pixels")
    return("colour: Alpha Grey")

def vivo_vivoy20():
    print("Model Name :Y20")
    print("price:₹17,990")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 64 GB")
    print("Camera :  13MP + 2MP + 2MP")
    print("Display Size :16.54 cm (6.51 inch)")
    print("Resolution : 1600 x 720 Pixels")
    return("colour:Purist Blue,Obsidian Black")

def vivo_vivov17():
    print("Model Name : V17")
    print("price:₹27,990")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 128 GB")
    print("Camera :  48MP + 8MP + 2MP + 2MP")
    print("Display Size :16.36 cm (6.44 inch)")
    print("Resolution :2400 x 1080 Pixels")
    return("colour: Midnight Ocean Black")

def realme():
    print("These are the models")
    print('1.realme 7i')
    print('2.realme 7 Pro')
    print('3.realme 6 Pro')
    return int(input("enter your choice[1-3]: "))

def realme_realme7i():
    print("Model Name : 7i")
    print("price:₹13,999")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 64 GB")
    print("Camera :  64MP + 8MP + 2MP + 2MP")
    print("Display Size :16.51 cm (6.5 inch)")
    print("Resolution :1600 x 720 Pixels")
    return("colour: Fusion Green")

def realme_realme7pro():
    print("Model Name : 7 Pro")
    print("price:₹20,999")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 128 GB")
    print("Camera :  64MP + 8MP + 2MP + 2MP")
    print("Display Size :16.26 cm (6.4 inch)")
    print("Resolution : 2400 x 1080 Pixels")
    return("colour: Mirror Blue,Mirror Silver")

def realme_realme6pro():
    print("Model Name : 6 Pro")
    print("price:₹17,999")
    print("SIM Type : Dual Sim ")
    print("Internal Storage : 64 GB")
    print("Camera :  64MP + 12MP + 8MP + 2MP")
    print("Display Size :16.76 cm (6.6 inch)")
    print("Resolution :2400 x 1080 Pixels")
    return("colour: Lightning Red")

def bot():
    greet_and_introduce()
    choice = show_menu()
    if choice == 1:
        choice1=apple()
        if choice1==1:
            print(apple_iphone11promax())
        elif choice1==2:
            print(apple_iphone11())
        elif choice1==3:
            print(apple_iphonexsmax())
        else:
            print("enter the correct choice[1-3]:")
    elif choice == 2:
        choice2=samsung()
        if choice2==1:
            print(samsung_galaxynote20ultra5g())
        elif choice2==2:
            print(samsung_galaxys20())
        elif choice2==3:
            print(samsung_galaxys20ultra())
        else:
            print("enter the correct choice[1-3]:")
    elif choice==3:
        choice3=xiaomi()
        if choice3==1:
            print(xiaomi_redminote9promax())
        elif choice3==2:
            print(xiaomi_redminote9pro())
        elif choice3==3:
            print(xiaomi_redmik20pro())
        else:
            print("enter the correct choice[1-3]:")
    elif choice==4:
        choice4=vivo()
        if choice4==1:
            print(vivo_vivox50pro())
        elif choice4==2:
            print(vivo_vivoy20())
        elif choice4==3:
            print(vivo_vivov17())
        else:
            print("enter the correct choice[1-3]:")
    elif choice==5:
        choice5=realme()
        if choice5==1:
            print(realme_realme7i())
        elif choice5==2:
            print(realme_realme7pro())
        elif choice5==3:
            print(realme_realme6pro())
        else:
            print("enter the correct choice[1-3]:")
    else:
        print("enter the correct choice[1-5]:")
bot()