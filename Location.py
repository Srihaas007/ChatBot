def mainMenu():
    print("1.Do you want to enter location manually")
    print("2.DO you want to do it automatically")
    selection=int(input("Enter your choice:"))
    if selection==1:
        manual()
    elif selection==2:
        automatic()
    else:
        print("Invalid choice. Enter 1 or 2")
        mainMenu()

def manual():
    print("1.location(1)")
    print("2.location(2)")
    print("3.location(3)")
    print("4.location(4)")
    selection=int(input("Enter your choice:"))
    if selection==1:
        print("1.restaurant name1")
        print("1.restaurant name2")
        print("1.restaurant name3")
        selection=int(input("Enter your choice: "))
        if selection==1:
            restaurant1_inlocation1()
        elif selection==2:
            restaurant2_inlocation1()
        elif selection == 3:
            restaurant3_inlocation1()
        else :
            print("Invalid choice. Enter 1-3 ")

    elif selection==2:
        print("1.restaurant name1")
        print("1.restaurant name2")
        print("1.restaurant name3")
        selection = int(input("Enter your choice: "))
        if selection == 1:
            restaurant1_inlocation2()
        elif selection == 2:
            restaurant2_inlocation2()
        elif selection == 3:
            restaurant3_inlocation2()
        else:
            print("Invalid choice. Enter 1-3 ")
    elif selection==3:
        print("1.restaurant name1")
        print("1.restaurant name2")
        print("1.restaurant name3")
        selection = int(input("Enter your choice: "))
        if selection == 1:
            restaurant1_inlocation3()
        elif selection == 2:
            restaurant2_inlocation3()
        elif selection == 3:
            restaurant3_inlocation3()
        else:
            print("Invalid choice. Enter 1-3 ")
    elif selection==4:
        print("1.restaurant name1")
        print("1.restaurant name2")
        print("1.restaurant name3")
        selection = int(input("Enter your choice: "))
        if selection == 1:
            restaurant1_inlocation4()
        elif selection == 2:
            restaurant2_inlocation4()
        elif selection == 3:
            restaurant3_inlocation4()
        else:
            print("Invalid choice. Enter 1-3 ")
    else:
        print("Invalid choice. Enter 1-4")
    print("Manual")
    return
def restaurant1_inlocation1():
    print("1. item")
    print("2. item")
    print("3. item")
    print("4. item")
    print("5. item")
    print("6. item")
    selection = int(input("Enter your choice:"))
    if selection == 1:
        print("Okay")
    elif selection == 2:
        print("Okay")
    elif selection == 3:
        print("Okay")
    elif selection == 4:
        print("Okay")
    elif selection == 5:
        print("Okay")
    elif selection == 6:
        print("Okay")
    else:
        print("Invalid choice. Enter 1-6")
    print("This is the Menu")
def restaurant2_inlocation1():
    print("1. item")
    print("2. item")
    print("3. item")
    print("4. item")
    print("5. item")
    print("6. item")
    selection = int(input("Enter your choice:"))
    if selection == 1:
        print("This is the Menu")
    elif selection == 2:
        print("This is the Menu")
    elif selection == 3:
        print("This is the Menu")
    elif selection == 4:
        print("This is the Menu")
    elif selection == 5:
        print("This is the Menu")
    elif selection == 6:
        print("This is the Menu")
    else:
        print("Invalid choice. Enter 1-6")
    print("Now lets do payment")

def restaurant3_inlocation1():
    print("1. item")
    print("2. item")
    print("3. item")
    print("4. item")
    print("5. item")
    print("6. item")
    selection = int(input("Enter your choice:"))
    if selection == 1:
        print("This is the Menu")
    elif selection == 2:
        print("This is the Menu")
    elif selection == 3:
        print("This is the Menu")
    elif selection == 4:
        print("This is the Menu")
    elif selection == 5:
        print("This is the Menu")
    elif selection == 6:
        print("This is the Menu")
    else:
        print("Invalid choice. Enter 1-6")
    print("Now lets do payment")
def restaurant1_inlocation2():
    print("1. item")
    print("2. item")
    print("3. item")
    print("4. item")
    print("5. item")
    print("6. item")
    selection = int(input("Enter your choice:"))
    if selection == 1:
        print("This is the Menu")
    elif selection == 2:
        print("This is the Menu")
    elif selection == 3:
        print("This is the Menu")
    elif selection == 4:
        print("This is the Menu")
    elif selection == 5:
        print("This is the Menu")
    elif selection == 6:
        print("This is the Menu")
    else:
        print("Invalid choice. Enter 1-6")
    print("Now lets do payment")
def restaurant2_inlocation2():
    print("1. item")
    print("2. item")
    print("3. item")
    print("4. item")
    print("5. item")
    print("6. item")
    selection = int(input("Enter your choice:"))
    if selection == 1:
        print("This is the Menu")
    elif selection == 2:
        print("This is the Menu")
    elif selection == 3:
        print("This is the Menu")
    elif selection == 4:
        print("This is the Menu")
    elif selection == 5:
        print("This is the Menu")
    elif selection == 6:
        print("This is the Menu")
    else:
        print("Invalid choice. Enter 1-6")
    print("Now lets do payment")
def restaurant3_inlocation2():
    print("1. item")
    print("2. item")
    print("3. item")
    print("4. item")
    print("5. item")
    print("6. item")
    selection = int(input("Enter your choice:"))
    if selection == 1:
        print("This is the Menu")
    elif selection == 2:
        print("This is the Menu")
    elif selection == 3:
        print("This is the Menu")
    elif selection == 4:
        print("This is the Menu")
    elif selection == 5:
        print("This is the Menu")
    elif selection == 6:
        print("This is the Menu")
    else:
        print("Invalid choice. Enter 1-6")
    print("Now lets do payment")
def restaurant1_inlocation3():
    print("1. item")
    print("2. item")
    print("3. item")
    print("4. item")
    print("5. item")
    print("6. item")
    selection = int(input("Enter your choice:"))
    if selection == 1:
        print("This is the Menu")
    elif selection == 2:
        print("This is the Menu")
    elif selection == 3:
        print("This is the Menu")
    elif selection == 4:
        print("This is the Menu")
    elif selection == 5:
        print("This is the Menu")
    elif selection == 6:
        print("This is the Menu")
    else:
        print("Invalid choice. Enter 1-6")
    print("Now lets do payment")
def restaurant2_inlocation3():
    print("1. item")
    print("2. item")
    print("3. item")
    print("4. item")
    print("5. item")
    print("6. item")
    selection = int(input("Enter your choice:"))
    if selection == 1:
        print("This is the Menu")
    elif selection == 2:
        print("This is the Menu")
    elif selection == 3:
        print("This is the Menu")
    elif selection == 4:
        print("This is the Menu")
    elif selection == 5:
        print("This is the Menu")
    elif selection == 6:
        print("This is the Menu")
    else:
        print("Invalid choice. Enter 1-6")
    print("Now lets do payment")
def restaurant3_inlocation3():
    print("1. item")
    print("2. item")
    print("3. item")
    print("4. item")
    print("5. item")
    print("6. item")
    selection = int(input("Enter your choice:"))
    if selection == 1:
        print("This is the Menu")
    elif selection == 2:
        print("This is the Menu")
    elif selection == 3:
        print("This is the Menu")
    elif selection == 4:
        print("This is the Menu")
    elif selection == 5:
        print("This is the Menu")
    elif selection == 6:
        print("This is the Menu")
    else:
        print("Invalid choice. Enter 1-6")
    print("Now lets do payment")
def restaurant1_inlocation4():
    print("1. item")
    print("2. item")
    print("3. item")
    print("4. item")
    print("5. item")
    print("6. item")
    selection = int(input("Enter your choice:"))
    if selection == 1:
        print("This is the Menu")
    elif selection == 2:
        print("This is the Menu")
    elif selection == 3:
        print("This is the Menu")
    elif selection == 4:
        print("This is the Menu")
    elif selection == 5:
        print("This is the Menu")
    elif selection == 6:
        print("This is the Menu")
    else:
        print("Invalid choice. Enter 1-6")
    print("Now lets do payment")
def restaurant2_inlocation4():
    print("1. item")
    print("2. item")
    print("3. item")
    print("4. item")
    print("5. item")
    print("6. item")
    selection = int(input("Enter your choice:"))
    if selection == 1:
        print("This is the Menu")
    elif selection == 2:
        print("This is the Menu")
    elif selection == 3:
        print("This is the Menu")
    elif selection == 4:
        print("This is the Menu")
    elif selection == 5:
        print("This is the Menu")
    elif selection == 6:
        print("This is the Menu")
    else:
        print("Invalid choice. Enter 1-6")
    print("Now lets do payment")
def restaurant3_inlocation4():
    print("1. item")
    print("2. item")
    print("3. item")
    print("4. item")
    print("5. item")
    print("6. item")
    selection = int(input("Enter your choice:"))
    if selection == 1:
        print("This is the Menu")
    elif selection == 2:
        print("This is the Menu")
    elif selection == 3:
        print("This is the Menu")
    elif selection == 4:
        print("This is the Menu")
    elif selection == 5:
        print("This is the Menu")
    elif selection == 6:
        print("This is the Menu")
    else:
        print("Invalid choice. Enter 1-6")
    print("Now lets do payment")

def automatic():
    import requests

    res = requests.get('https://ipinfo.io/')
    data = res.json()

    city = data['city']

    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]
    print("Latitude : ", latitude)
    print("Longitude : ", longitude)
    print("City : ", city)

print(mainMenu())
