from time import sleep as w8

class Application:
    def __init__(self, settings):
        self.settings = settings

    def run(self):
        while True:
            print(f"Добро пожаловать в мафию!")
            w8(1)
            print(f"Количество игроков = {self.settings.amount_of_players}")
            w8(1)
            print(f"Время на обсуждение = {self.settings.conversation_time}")
            break