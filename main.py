import tkinter
import time
import datetime

COLOUR_BACKGROUND = 'white'
CANVAS_SIZE = (900, 700)
TIME_LIMIT = 5
timer = None


def on_key_release(event):
    print("key pressed")
    reset_timer()
    timer_check(TIME_LIMIT)


def reset_timer():
    if timer:
        print("reset")
        window.after_cancel(timer)


def timer_check(count):

    if count > 0:
        global timer
        print(int(count))
        timer = window.after(1000, timer_check, count - 1)
        txt_timer.config(text=count)
    else:
        delete_text()


def delete_text():
    text_widget.delete('1.0', 'end')
    txt_timer.config(text='0')


window = tkinter.Tk()
window.title = "Disappearing Text"
window.config(padx=0, pady=0, bg=COLOUR_BACKGROUND)


txt_timer = tkinter.Label(text=5)
text_widget = tkinter.Text(window,  font=("Consolas", 16), height=8, width=100, background=COLOUR_BACKGROUND)
txt_timer.grid(column=1, row=0, columnspan=2)
text_widget.grid(column=0, row=1, columnspan=4)
text_widget.focus_set()

window.bind("<KeyRelease>", on_key_release)

window.mainloop()