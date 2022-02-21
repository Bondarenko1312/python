"""
створити пустый список users_list = []

стврорити меню в якому потрібно реалізувати:

1) додававання нового юзера
2) вивід всіх юзерів
3) вивід всіх юзерів за віком
4) видалення юзера по id
5) заміна статуса юзера на протилежний
6) вихід з меню

приклад юзера {'id':1,'name':'Max', 'age':35,'status':False}
"""
user_list = []

while True:
    print("1) Add new user")
    print("2) Get all users")
    print("3) Get all users by age")
    print("4) Delete user by id")
    print("5) Change user status to opposite")
    print("6) Exit")


    choice = input("What do you need bro?")
    if choice == '1':
        user = {}
        print("Type user details :")
        id = int(input('Type user id'))
        name = str(input('Type user name'))
        age = int(input('Type user age'))
        status = bool(input("Type user status"))

        user = {
            'id': id,
            'name': name,
            'age': age,
            'status': status
                }
        user_list.append(user)

        answer = input("Add another user data? yes=1 / no = 0")
        if answer == "1":
            choice == "1"
        elif answer == "0":
            print(user_list)
        continue

    elif choice == "2":
        for element in user_list:
            print(element)

    elif choice == "3":
        age = input("Type user age :")
        for element in user_list:
            if element['age'] == age:
                print(element)

    elif choice == "4":
        id = input("Type user id for delete :")
        for element in range(len(user_list)):
            if element['id'] == id:
                del user_list[element]
                print(user_list)

    elif choice == "5":
        status = input("Type user status: ")
        for element in range(len(user_list)):
            if user_list[element] == status['True']:
                user_list[element] = 'False'

    elif choice == "6":
        break

