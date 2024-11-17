#  Дополнительное практическое задание по модулю: "Классы и объекты."

import time


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def add(self, *video):
        add_videos = list(video).copy()
        for i in video:
            for j in self.videos:
                if i.title == j.title:
                    add_videos.remove(j)
                    break
        self.videos += add_videos

    def log_in(self, nickname, password):
        log_user = [u for u in self.users if u.nickname == nickname]
        if log_user:
            user = log_user[0]
            if user.password == hash(str(password)):
                self.current_user = user
            else:
                print('Incorrect password')

    def logout(self):
        self.current_user = None

    def register(self, nickname: str, password: int, age: int):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User(nickname, password, age))

    def get_videos(self, search_word):
        find_videos = [v.title for v in self.videos if search_word in v]
        if find_videos:
            return find_videos

    def watch_video(self, film_title):
        find_video = [video for video in ur.videos if video.title == film_title]
        if find_video:
            watch = find_video[0]
            if self.current_user == None:
                print("Войдите в аккаунт, чтобы смотреть видео")
            else:
                if watch.adult_mode and int(self.current_user.age) < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    while watch.time_now <= watch.duration:
                        watch.time_now += 1
                        time.sleep(1)
                        print(watch.time_now, end=' ')
                    print("Конец видео")


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Название: {self.title}, Длительность: {self.duration}, Возрастное ограничение: {self.adult_mode}"

    def __contains__(self, item):
        return item.upper() in self.title.upper()


class User:

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(str(password))
        self.age = age

    def __eq__(self, other):
        return self.nickname == other

    def __str__(self):
        return f"{self.nickname}"


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
ur.add(v1)
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
ur.watch_video('Для чего девушкам парень программист?')
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
