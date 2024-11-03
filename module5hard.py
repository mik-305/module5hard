class User:
    nickname = ''           # имя пользователя
    password = 0            # паролб
    age = 0                 # Возраст

class Video:
    title = ''             # заголовок
    duration = 0           # продолжительность
    time_now = 0           # секунда остановки (изначально 0)
    adult_mode = False     # (ограничение по возрасту

class UrTube:
    users = ''             # (список объектов User
    videos = ''            # (список объектов Video

    def log_in(self, nickname, password):
        pass
    def register(self, nickname, password, age):
        pass
    def log_out(self):
        pass
    def add(self, *video):
        videos = {}

    def videos(self, poisk_vid):    # Поисковое слово  poisk_vid
        pass
    def watch_video(self, video):
        pass