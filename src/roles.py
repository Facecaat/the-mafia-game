class Civilian:
    def __init__(self, name, is_healed=False, is_shot=False, is_checked=False, is_fucked=False):
        self.name = name
        self.is_healed = is_healed
        self.is_shot = is_shot
        self.is_checked = is_checked
        self.is_fucked = is_fucked

    def act_message(self):
        return "Опиши свои мысли перед сном"

    def action(self, message: str = "") -> str:
        return message

class Doctor(Civilian):
    def act_message(self):
        return "Введите номер игрока, которого хотите спасти от смерти и сообщение"

    def action(self, act: int, message: str = "") -> list:
        return [act, message]

class Mafia(Civilian):
    def act_message(self):
        return "Введите номер игрока, которого хотите ебнуть и сообщение"

    def action(self, act: int, message: str = "") -> list:
        return [act, message]

class Detective(Civilian):
    def act_message(self):
        return "Введите номер игрока, которого хотите поймать как дешевку и сообщение"

    def action(self, act: int, message: str = "") -> list:
        return [act, message]

class Whore(Civilian):
    def act_message(self):
        return "Введите номер игрока, которого хотите выебать и сообщение"

    def action(self, act: int, message: str = "") -> list:
        return [act, message]








