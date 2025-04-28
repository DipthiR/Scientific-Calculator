import tkinter as tk
import math

def click(event):
    current = entry.get()
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            expression = current.replace("^", "**")
            result = eval(expression, {"__builtins__": None}, vars(math))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text in ["sin", "cos", "tan", "log", "sqrt"]:
        entry.insert(tk.END, f"{text}(")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("350x500")

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

# Buttons layout
buttons = [
    ["7", "8", "9", "/", "sqrt"],
    ["4", "5", "6", "*", "log"],
    ["1", "2", "3", "-", "sin"],
    ["0", ".", "=", "+", "cos"],
    ["(", ")", "^", "C", "tan"]
]

for row in buttons:
    frame = tk.Frame(root)
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 14", height=2, width=5)
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
        btn.bind("<Button-1>", click)
    frame.pack(expand=True, fill=tk.BOTH)

root.mainloop()
