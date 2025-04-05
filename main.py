import tkinter
import time
import datetime

COLOUR_BACKGROUND = '#1e1e2f'
TEXT_COLOUR = '#e0e0e0'
CANVAS_SIZE = (500, 300)
TIME_LIMIT = 5
timer = None


def on_key_release(event):
    reset_timer()
    timer_check(TIME_LIMIT)


def reset_timer():
    global timer
    if timer:
        window.after_cancel(timer)
        timer = None
        text_widget.tag_remove("fade", "1.0", "end")
        text_widget.tag_configure("fade", foreground=TEXT_COLOUR)
        text_widget.tag_add("fade", "1.0", "end")


def timer_check(count):
    if count > 0:
        global timer
        txt_timer.config(text=int(count))
        apply_fade_color(count)
        timer = window.after(40, timer_check, count - 0.04)
    else:
        delete_text()


def delete_text():
    text_widget.delete('1.0', 'end')
    txt_timer.config(text='0')


def apply_fade_color(count):
    min_brightness = 0
    max_brightness = 224
    brightness = int(min_brightness + (count / TIME_LIMIT) * (max_brightness - min_brightness))
    brightness = max(min(brightness, 255), 0)  # clamp to 0–255

    hex_color = f"#{brightness:02x}{brightness:02x}{brightness:02x}"
    text_widget.tag_configure("fade", foreground=hex_color)
    text_widget.tag_add("fade", "1.0", "end")


window = tkinter.Tk()
window.title = "Disappearing Text"
window.config(padx=0, pady=0, bg=COLOUR_BACKGROUND)

txt_timer = tkinter.Label(window, text=TIME_LIMIT, fg=TEXT_COLOUR, bg=COLOUR_BACKGROUND, font=("Consolas", 20))
text_widget = tkinter.Text(window,  font=("Consolas", 24), height=5, width=70, insertbackground=TEXT_COLOUR, fg=TEXT_COLOUR, background=COLOUR_BACKGROUND)
txt_timer.grid(column=1, row=0, columnspan=2)
text_widget.grid(column=0, row=1, columnspan=4)
text_widget.focus_set()

window.bind("<KeyRelease>", on_key_release)

window.mainloop()