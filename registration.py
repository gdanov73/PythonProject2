from random import choice


class Database:
    def __init__(self):
        self.data={}

    def add_user(self, username, password):
        self.data[username] = password

class User: # класс пользователя, содержащий атрибуты:логин, пароль
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm :
            self,password = password

if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1-вход\n2-регистрация"))
        if choice == 1 :
            login = input('Введите логин:')
            password = input("Введите пароль:")