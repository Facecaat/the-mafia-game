import os.path

from exceptions.exceptions import WrongAmountOfPlayers, WrongConversationTime

class Settings:
    def __init__(self, amount_of_players=None, conversation_time=None):
        self.amount_of_players = amount_of_players
        self.conversation_time = conversation_time

    def setup(self):
        while True:
            try:
                if self.amount_of_players is None:
                    try:
                        self.amount_of_players = int(input("Введите количество игроков: "))
                    except ValueError as e:
                        print("Введите целое число")
                        continue
                if self.amount_of_players not in range (4, 11):
                    self.amount_of_players = None
                    raise WrongAmountOfPlayers
                try:
                    self.conversation_time = int(input("Введите количество времени на обсуждение: "))
                except ValueError as e:
                    print("Введите целое число")
                    continue
                if self.conversation_time not in range(1, 6):
                    raise WrongConversationTime
                print("Настройки успешно установлены\n")
                break
            except WrongConversationTime as e:
                print(e.message)
            except WrongAmountOfPlayers as e:
                print(e.message)

def get_image(role):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    img_dir = os.path.join(current_directory, 'img')
    image_file = [f for f in os.listdir(img_dir) if
                   f.lower().startswith(role.lower()) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return os.path.join(img_dir, *image_file)




