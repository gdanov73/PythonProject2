import time # импортируем модуль


class User : # создание класса
    def __init__(self, nickname : str, password : int, age : int): # конструкор класса
        self.nickname = nickname # присвоение значения атрибуту
        self.password = hash(password) # -//-//-
        self.age = age # -//-//-
    def __str__(self): # метод вывода на печать
        return self.nickname # возврат nickname
class Video : # конструкор класса
    def __init__(self, title : str, duration : int, adult_mode = False): # конструкор класса
        self.title = title # присвоение значения атрибуту
        self.duration = duration # -//-//-
        self.time_now = 0 # -//-//-
        self.adult_mode = adult_mode # -//-//-
class UrTube : # конструкор класса
    def __init__(self): # конструкор класса
        self.users : list[User] = [] # присвоение значения атрибуту
        self.videos : list[Video] = [] # -//-//-
        self.current_user = None # -//-//-



    def log_in(self, nickname, password): # метод авторизациим
        for user in self.users : # цикл по списку users
            if user.nickname == nickname and user.password == hash(password) : # сравнение никнейма и пароля
                self.current_user = user # присвоение текущему пользователю
                break # конец цикла

    def register(self, nickname, password, age): # метод регистрации
        user_register = User(nickname, password, age) # создаем юзера
        for user in self.users : # цикл по списку юзеров
            if user.nickname == nickname : # сравнение никнеймов
                print("Пользователь " + nickname + " уже существует") # вывод существующего пользователя
                return # выход из метода
        self.users.append(user_register) # добавление в список юзеров
        self.log_in(nickname, password) # авторизация

    def log_out(self): # метод выхода
        self.current_user = None # выкидыш текущего юзера

    def add(self, *video: Video): # метод добавления видео
        self.videos = self.videos + [*video] # добавляем видео к списку

    def get_videos(self, search : str): # метод поиска видео
        title_list = [] # создаем пустой список
        for video in self.videos : # цикл по списку видео
            if search.lower() in video.title.lower() : # проверка условия на наличие видео
                title_list.append(video.title) # добавление названия видео в список
        return title_list # возврат заполненного списка

    def watch_video(self, title : str): # метод просмотра видео
        if self.current_user is None: # проверка авторизации пользователя
            print("Войдите в аккаунт, чтобы смотреть видео") # печать ссообщения
            return # выход из метода
        for video in self.videos: # цикл по списку видео
            if title.lower() == video.title.lower() : # проверка на наличие видео в списке
                if video.adult_mode == True and self.current_user.age < 18 : # проверка на возраст
                    print("Вам нет 18 лет, пожалуйста покиньте страницу") # печать строки
                    return # выход из метода
                for t in range(video.time_now, video.duration) : # цикл продолжительности видео
                    print(t+1, end=" ", sep=" ") # печать текущей секунды видео
                    time.sleep(1) # задержка программы на 1 секунду
                print("Конец видео") # печать строки



 # ввод данных
ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео

ur.add(v1, v2)

# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)

# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')

