class User:
    nickname = ''           # имя пользователя
    password = 0            # пароль
    age = 0                 # Возраст
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    title = ''             # заголовок
    duration = 0           # продолжительность
    time_now = 0           # секунда остановки (изначально 0)
    adult_mode = False     # (ограничение по возрасту
    def __init__(self, title, duration, *time_now, **adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    users = ''             # список объектов User
    videos = {}            # список объектов Video

    def log_in(self, nickname, password):
        pass
    def register(self, nickname, password, age):
        pass
    def log_out(self):
        current_user = 'None'   # Сбрасываем текущего пользователя
    def add(self, *Video):
        #if Video.title in videos:
        #videos = {}
        print(v1.title, '- два объекта -', v2.title)
        #pass
    def get_videos(self, poisk_vid):    # Поисковое слово  poisk_vid
        pass
    def watch_video(self, video):
        pass

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
