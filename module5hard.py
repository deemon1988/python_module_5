#  Дополнительное практическое задание по модулю: "Классы и объекты."

import time

class UrTube:
        def __init__(self):
            self.users = []
            self.videos = []
            self.current_user = None

        def add(self, *video):
            add_videos = list(video).copy()
            if self.videos != None:
                for i in video:
                    for j in self.videos:
                        if i.title == j.title:
                            add_videos.remove(j)
                            break
                if len(add_videos) > 0:
                    self.videos += video
            else:
                self.videos = video


        def log_in(self, nickname, password):
            log_user = [u for u in self.users if u.nickname == nickname]
            if log_user:
                user = log_user[0]
                if user.password == hash(str(password)):
                    self.current_user = user
                    print("Log in")
                else:
                    print('Incorrect password')

        def logout(self):
            self.current_user = None

        def register(self, nickname: str, password: int, age: int):
             if nickname in self.users :
                    print(f"Пользователь {nickname} уже существует")
             else:
                 self.users.append(User(nickname,password,age))

        def get_videos(self, search_word):
            find_videos = [v.title for v in self.videos if search_word.upper() in v.title.upper()]
            if find_videos:
                return find_videos

        def watch_video(self, film_title):
           find_video = [video for video in ur.videos if video.title == film_title]
           if find_video:
               watch = find_video[0]
               if self.current_user == None:
                   print("Войдите в аккаунт, чтобы смотреть видео")
               else:
                   if int(self.current_user.age) >= 18 and not watch.adult_mode:
                       while watch.time_now <= watch.duration:
                           print(watch.time_now)
                           time.sleep(1)
                           watch.time_now += 1
                       print("Конец видео")
                   else:
                       print("Вам нет 18 лет, пожалуйста покиньте страницу")


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Название: {self.title}, Длительность: {self.duration}, Возрастное ограничение: {self.adult_mode}"

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

