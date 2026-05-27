import tkinter as tk

window = tk.Tk()
window.title("Pink Calculator")
window.geometry("520x700")
window.resizable(False, False)
window.config(bg="#2d123f")

current_text = ""


screen = tk.Entry(
    window,
    font=("Arial", 34, "bold"),
    bg="#f8c8ff",
    fg="#3b0054",
    bd=0,
    justify="right"
)
screen.pack(padx=35, pady=35, ipady=22, fill="x")


def add_to_screen(char):
    global current_text

    current_text += str(char)
    screen.delete(0, tk.END)
    screen.insert(tk.END, current_text)


def clear_screen():
    global current_text

    current_text = ""
    screen.delete(0, tk.END)


def backspace():
    global current_text

    current_text = current_text[:-1]
    screen.delete(0, tk.END)
    screen.insert(tk.END, current_text)


def get_result():
    global current_text

    try:
        text = current_text.replace("×", "*").replace("÷", "/")
        answer = eval(text)

        screen.delete(0, tk.END)
        screen.insert(tk.END, answer
        )

        current_text = str(answer)

    except:
        screen.delete(0, tk.END)
        screen.insert(tk.END, "Error")
        current_text = ""


button_area = tk.Frame(window, bg="#2d123f")
button_area.pack(padx=30, pady=25)


buttons = [
    ["C", "⌫", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]


for row_index, row in enumerate(buttons):
    for col_index, item in enumerate(row):

        if item == "C":
            bg_color = "#ff4fa3"
            text_color = "white"
            action = clear_screen

        elif item == "⌫":
            bg_color = "#c77dff"
            text_color = "white"
            action = backspace

        elif item == "=":
            bg_color = "#ff70c8"
            text_color = "white"
            action = get_result

        elif item in ["+", "-", "×", "÷", "%"]:
            bg_color = "#ffd6ff"
            text_color = "#3b0054"
            action = lambda value=item: add_to_screen(value)

        else:
            bg_color = "#f3a6ff"
            text_color = "#3b0054"
            action = lambda value=item: add_to_screen(value)

        btn = tk.Button(
            button_area,
            text=item,
            command=action,
            font=("Arial", 22, "bold"),
            bg=bg_color,
            fg=text_color,
            activebackground="#ffb3ec",
            activeforeground="#3b0054",
            bd=0,
            width=4,
            height=1,
            cursor="hand2"
        )

        btn.grid(row=row_index, column=col_index, padx=10, pady=10)


window.mainloop()