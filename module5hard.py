#  Дополнительное практическое задание по модулю: "Классы и объекты."

class UrTube:
        def __init__(self, users, videos:list, current_user=None):
            self.users = users
            self.videos = videos
            self.current_user = current_user

        def __add__(self, other):
            pass

        def add_video(self, video):
            self.videos.append(video)

        def log_in(self, nickname, password):
            if nickname in self.users :
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

        def logout(self):
            self.current_user = None

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:

        def __init__(self, nickname: str, password: int, age: int):
            self.nickname = nickname
            self.password = hash(str(password))
            self.age = age

        def __eq__(self, other):
            return self.nickname == other


#user = User(nickname:=input("Имя пользователя: "), password := input("Пароль: "), age := input("Возвраст: "))
user = User('dim', 123, 23)
user2 = User('den', 421, 24)
user3 = User('max', 231, 26)
print(user.nickname, user.password, user.age)

film = Video('comedy', 100)
clip = Video('musical', 20)
doc = Video('documental', 50)

urban = UrTube([user,user2,user3], [film,clip,doc])

urban.log_in('max',231)
print(urban.current_user)

urban.add_video(film)
urban.add_video(clip)

for i in urban.videos:
    print(i.title)