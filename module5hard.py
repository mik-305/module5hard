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
    """def __init__(self): #, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user       # текущий пользователь
    """
    users = ''                                # список объектов User
    videos = []                               # список объектов Video

    def log_in(self, nickname, password):
        pass
    def register(self, nickname, password, age):
        pass
    def log_out(self):
        current_user = 'None'   # Сбрасываем текущего пользователя
    def add(self, *video):
        for i in video:
#            print(i.title, i.duration)
            self.videos.append(i.title)     # Записали названия фильмов
        #print(type(video))
#        print('Тип Videos -=_>',type(self.videos))
#        print('Длина Videos >>>', len(self.videos))
        #print('Добавление videos ---', self.videos)
#        for j in self.videos:
#            print('videos=====>', j)

    def get_videos(self, poisk_vid):    # Поисковое слово  poisk_vid
        print(poisk_vid)
        print(list(self.videos))
        if self.videos.__contains__(poisk_vid):
        #if poisk_vid in self.videos:
            print('777')
            #print(f'Поисковое слово --->,{poisk_vid}')
            #pass
    def watch_video(self, video):
        pass

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('Лучший'))
print(ur.get_videos('ПРОГ'))
