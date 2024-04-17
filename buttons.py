from tkinter import *
red_shades = ["#FF2D00","#DC2700", "#BC2100","#9D1B00","#6E1300"]
def edit_label(event,self):
    pressed_key1 = event.keysym
    pressed_key = event.char

    config=self.text['text']
    if pressed_key1 == "BackSpace":
        self.text.config(text=config[:len(config)-1])
    else:
        self.index=0
        self.text.config(text=config+pressed_key)
    self.restart_timer=True
    self.words.config(text=f'{count_words(self.text['text'])}w')
def count_words(text):
    return len(text.split())
class Buttons:
    def __init__(self):
        self.text = Label(text="", font=("Arial", 15, "bold"),
                          bg="white", fg="red", wraplength=500)
        self.text.pack()
        self.config = ""
        self.text.focus_set()
        self.restart_timer = False
        self.start_timer = Label(text='', font=("Arial", 20, "bold"), bg="white", fg="green")
        self.start_timer.place(x=0, y=0)
        self.timer_remaining=0
        self.index=0
        self.words=Label(text="0w", font=("Arial", 15, "bold"),
                          bg="white", fg="green", wraplength=500)
        self.words.place(x=450,y=550)
        self.game_timer(6)

        self.text.bind('<Key>', lambda event: edit_label(event, self))
    def game_timer(self,remaining=None):
        if remaining is not None and self.restart_timer is False:
            self.timer_remaining = remaining
        if self.restart_timer is True:
            self.timer_remaining = 6
            self.restart_timer=False
        self.timer_remaining = self.timer_remaining - 1

        self.text.config(fg=red_shades[self.index])
        self.index+=1
        if self.index==5:
            self.index=0
        if self.timer_remaining<=0:
            self.text.config(text="GAME OVER",fg="black")
            self.text.place(x=180,y=250)
        self.start_timer.after(1000, self.game_timer)