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
    print("Manual")

def automatic():
    import requests

res = requests.get('https://ipinfo.io/')
data = res.json()

city = data['city']

location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]
    print("City :",city)
