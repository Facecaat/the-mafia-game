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
                print("Настройки успешно установлены")
                break
            except WrongConversationTime as e:
                print(e.message)
            except WrongAmountOfPlayers as e:
                print(e.message)





