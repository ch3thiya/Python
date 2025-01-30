import tkinter
import math

FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    global reps
    window.after_cancel(timer)
    title_label.config(text="Pomodoro", fg="white")
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="")
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_sec = (WORK_MIN * 60)
    short_break_sec = (SHORT_BREAK_MIN * 60)
    long_break_sec = (LONG_BREAK_MIN * 60)

    if reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg="GREEN")
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg="GREEN")
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg="RED")

def count_down(count):
    mark = ""

    count_min = math.floor(count / 60)
    count_seconds = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔️"
            timer_label.config(text=mark)


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="black")

title_label = tkinter.Label(text="Pomodoro", font=("DM Sans", 27, "bold"), bg="black", fg="white")
title_label.grid(column=1, row=0)

timer_label = tkinter.Label(text="", font=("DM Sans", 15, "bold"), bg="black", fg="green")
timer_label.grid(column=1, row=3)

start_button = tkinter.Button(text="Start ", font=("DM Sans", 10, "bold"), bg="black", fg="white", width=6, height=1,
                              borderwidth=4, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", font=("DM Sans", 10, "bold"),bg="black", fg="white", width=6, height=1,
                              borderwidth=4, command=reset_timer)
reset_button.grid(column=2, row=2)

canvas = tkinter.Canvas(width=203, height=224, bg="black", highlightthickness=0)
tomato = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)

timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=("kanit", 30, "bold"))
canvas.grid(column=1, row=1, padx=20, pady=20)

window.mainloop()
