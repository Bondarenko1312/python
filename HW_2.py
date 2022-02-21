"""
написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
- первый записывает в эту переменную запись
- второй возвращает все записи

запишите 5 тудушек
и выведете все
"""
def notebook():
    todo_list = []

    def add_todo(new_todo):
        nonlocal todo_list
        todo_list.append(new_todo)

    def get_all():
        return todo_list
    return add_todo, get_all

add_todo, get_all = notebook()

while True:
    for item in range (5):
        new_todo = (input("Enter to do list:"))
        add_todo(new_todo)
    break

print(get_all())


#WITH TYPING 2) протипизировать первое задание
"""
def notebook():
    todo_list: list = []
    def add_todo(new_todo:str) -> None:
        nonlocal todo_list
        todo_list.append(new_todo)

    def get_all() -> list[str]:
        return todo_list

    return add_todo, get_all
add_todo, get_all = notebook()

while True:
    for item in range(5):
        add_todo(input("Enter to do list :"))
    break
print(get_all())
"""


"""
3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)

Пример:

expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'
"""