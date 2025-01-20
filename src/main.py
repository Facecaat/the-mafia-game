from tkinter import *
from time import sleep
from game_settings import Settings
from application import Application

FONT_SETTING = ('Consolas', 13)

if __name__ == '__main__':
    current_settings = Settings()
    current_settings.setup()
    application = Application(current_settings)
    application.run()


















if 1 == 2:
    window = Tk()
    window.geometry('800x600')
    window.title('Мафия')
    BACKGROUND_IMAGE = PhotoImage(file='/\\background.png')
    background_image = Label(window, image=BACKGROUND_IMAGE)
    background_image.place(x=0, y=0, relwidth=1, relheight=1)
    def remove_intro():
        background_image.destroy()
    window.after(5000, remove_intro)
    window.config(background='black')
    window.mainloop()





#оформление текста чтобы не потерять
    #welcome_message_and_players_count = Label(window, text='Привет! Добро пожаловать в текстовую мафию, введите количество игроков:',
                                              #background='black', font=('Impact', 13), fg='white')
    #welcome_message_and_players_count.pack(side='bottom', padx=0, pady=15)



