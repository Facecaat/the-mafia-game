class WrongAmountOfPlayers(Exception):
    '''
    Исключение возникает, когда неверно вводится количество игроков
    '''

    def __init__(self):
        self.message = "Введите верное количество игроков (число от 4 до 10)"
        super().__init__(self.message)

class WrongConversationTime(Exception):
    '''
    Исключение возникает, когда неверно вводится количество времени на обсуждение
    '''

    def __init__(self):
        self.message = "Введите верное количество времени в минутах (число от от 1 до 5)"
        super().__init__(self.message)