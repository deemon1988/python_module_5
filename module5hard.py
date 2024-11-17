#  Дополнительное практическое задание по модулю: "Классы и объекты."

import time


class UrTube:
        def __init__(self, users:list=None, videos:list=None, current_user=None):
            self.users = []
            self.videos = videos
            self.current_user = current_user

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
                    print("Добавленные видео:", [v.title for v in add_videos])
            else:
                self.videos = video
                print("Добавленные видео:", [v.title for v in add_videos])


        def log_in(self, nickname, password):
            if self.users != None and nickname in self.users :
                for i in self.users:
                    if i.nickname == nickname:
                        if i.password == hash(str(password)):
                            self.current_user = nickname
                            print("Log in")
                            break
                        else:
                            print('Incorrect password')
                            break
                    else:
                        continue
            else:
                print("Зарегистрируйтесь")

        def logout(self):
            self.current_user = None

        def register(self, nickname: str, password: int, age: int):
             if nickname in self.users :
                    print(f"Пользователь {nickname} уже существует")
             else:
                 self.users.append(User(nickname,password,age))

        def get_videos(self, search_word):
            find_videos = []
            for i in ur.videos:
                if search_word.upper() in i.title.upper():
                    find_videos.append(i.title)
            return find_videos

        def watch_video(self, film_title):
           watch = [Video for Video in ur.videos if Video.title == film_title]
           if watch != None and self.current_user != None:
               film = watch.pop()
               if int(self.current_user.age) >= 18 and film.adult_mode:
                   while film.time_now <= film.duration:
                       print(film.time_now)
                       time.sleep(1)
                       film.time_now += 1
                   print("Конец видео")
               else:
                   print("Вам нет 18 лет, пожалуйста покиньте страницу")
           else:
               print("Войдите в аккаунт, чтобы смотреть видео")

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Название: {self.title}, Длительность: {self.duration}"

class User:

        def __init__(self, nickname: str, password: int, age: int):
            self.nickname = nickname
            self.password = hash(str(password))
            self.age = age

        def __eq__(self, other):
            return self.nickname == other

        def __str__(self):
            return f"{self.nickname}"
#user = User(nickname:=input("Имя пользователя: "), password := input("Пароль: "), age := input("Возвраст: "))
user = User('dim', 123, 23)
user2 = User('den', 421, 24)
user3 = User('max', 231, 26)
print(user.nickname, user.password, user.age)

film = Video('comedy', 100)
clip = Video('musical', 20, adult_mode=True)
doc = Video('documental', 50)



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2)
ur.add(clip, film)
ur.add(clip, film)
print("Все видео:",[v.title for v in ur.videos])

ur.register('dim',123, 23)
ur.register('den', 421, 24)


print(ur.get_videos('Прог'))

ur.log_in("dim", 123)


ur.watch_video("musical")

