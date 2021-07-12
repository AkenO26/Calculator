import tkinter as tk

main_window = tk.Tk()
main_window.title("Calculator")
w = 335; h = 180
main_window.minsize(w, h); main_window.maxsize(w, h)
ws = main_window.winfo_screenwidth()
hs = main_window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
main_window.geometry('%dx%d+%d+%d' % (w, h, x, y))


expression = ""




def keypress(key):
    global expression
    expression = expression + str(key)
    input_variable.set(expression)

def clear():
    global expression
    expression = ""
    input_variable.set(expression)

def key_eval():
    global expression
    expression= eval(expression)
    input_variable.set(expression)


input_variable = tk.StringVar()
entry = tk.Entry(main_window, justify = "right", textvariable = input_variable, state="disabled")
entry.grid(columnspan = 4, ipadx = "70")






# k=0
# for i in range(3):
#     for j in range(3):
#         k+=1
#         button = tk.Button(main_window, text =k, height = 2, width = 7, command = lambda: keypress(k))
#         button.grid(row = i+1, column = j,sticky ="nsew")

button = tk.Button(main_window, text =1, height = 2, width = 7, command = lambda: keypress(1))
button.grid(row = 1, column = 0,sticky ="nsew")

button = tk.Button(main_window, text =2, height = 2, width = 7, command = lambda: keypress(2))
button.grid(row = 1, column = 1,sticky ="nsew")

button = tk.Button(main_window, text =3, height = 2, width = 7, command = lambda: keypress(3))
button.grid(row = 1, column = 2,sticky ="nsew")

button = tk.Button(main_window, text =4, height = 2, width = 7, command = lambda: keypress(4))
button.grid(row = 2, column = 0,sticky ="nsew")

button = tk.Button(main_window, text =5, height = 2, width = 7, command = lambda: keypress(5))
button.grid(row = 2, column = 1,sticky ="nsew")

button = tk.Button(main_window, text =6, height = 2, width = 7, command = lambda: keypress(6))
button.grid(row = 2, column = 2,sticky ="nsew")

button = tk.Button(main_window, text =7, height = 2, width = 7, command = lambda: keypress(7))
button.grid(row = 3, column = 0,sticky ="nsew")

button = tk.Button(main_window, text =8, height = 2, width = 7, command = lambda: keypress(8))
button.grid(row = 3, column = 1,sticky ="nsew")

button = tk.Button(main_window, text =9, height = 2, width = 7, command = lambda: keypress(9))
button.grid(row = 3, column = 2,sticky ="nsew")





button_plus = tk.Button(main_window, text ="+", height = 2, width = 7, command = lambda: keypress("+"))
button_plus.grid(row = 1, column = 3, sticky = "nsew")

button_minus = tk.Button(main_window, text ="-", height = 2, width = 7, command = lambda: keypress("-"))
button_minus.grid(row = 2, column = 3, sticky = "nsew")

button_mult = tk.Button(main_window, text ="*", height = 2, width = 7, command = lambda: keypress("*"))
button_mult.grid(row = 3, column = 3, sticky = "nsew")

button_div = tk.Button(main_window, text ="/", height = 2, width = 7, command = lambda: keypress("/"))
button_div.grid(row = 4, column = 3, sticky = "nsew")

button_eq = tk.Button(main_window, text ="=", height = 2, width = 7, command = key_eval)
button_eq.grid(row = 4, column = 2, sticky = "nsew")

button_clear = tk.Button(main_window, text ="Clear", height = 2, width = 7, command = clear)
button_clear.grid(row = 4, column = 1, sticky = "nsew")

button_z = tk.Button(main_window, text ="0", height = 2, width = 7, command = lambda :keypress(0))
button_z.grid(row = 4, column = 0, sticky = "nsew")







main_window.mainloop()