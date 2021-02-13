"""
Usar a função em seu programa para mostrar o resultado.
O resultado pode ser em texto formatado impresso na tela
ou gráfico, usando o módulo ‘pygame’. Note que o uso do ‘pygame’ é opcional.
"""
from tkinter import *
from info_dir import dir_info
from info_files import file_info

# Vars
black = "#292929"
white = "#ababab"
font1 = "none 12 bold"
font2 = "none 11"


# Funcs
def click(out, func):
    """
    This func collect the text from the entry box
    and execute the function by clicking in the button.
    :return: None
    """
    entered_txt = textentry.get()
    out.delete(0.0, END)
    try:
        info = func(str(entered_txt))
    except:
        info = "Sorry, do you passed a wrong parameter"

    out.insert(END, info)


def close_window():
    window.destroy()
    exit()


# Screen set
window = Tk()
window.title("Projeto de Bloco Python")
window.configure(background=black)
# Content

#     Dir:
Label(window, text="Directory info:", bg=black, fg=white, font=font1).grid(row=0, column=0, sticky=W)
Label(window, text="Please enter with the path:", bg=black, fg=white, font=font2).grid(row=1, column=0, sticky=W)
textentry = Entry(window, width=27, bg=white)
textentry.grid(row=2, column=0, sticky=W)
output_dir = Text(window, width=100, height=7, wrap=WORD, background=white)
output_dir.grid(row=4, column=0, sticky=W)
Button(window, text="Submit", width=5, command=lambda: click(output_dir, dir_info)).grid(row=3, column=0, sticky=W)

#      File:
Label(window, text="\nFile info:", bg=black, fg=white, font=font1).grid(row=5, column=0, sticky=W)
Label(window, text="Please enter with the file name:", bg=black, fg=white, font=font2).grid(row=6, column=0, sticky=W)
textentry = Entry(window, width=27, bg=white)
textentry.grid(row=7, column=0, sticky=W)
output_file = Text(window, width=100, height=7, wrap=WORD, background=white)
output_file.grid(row=9, column=0, sticky=W)
Button(window, text="Submit", width=5, command=lambda: click(output_file, file_info)).grid(row=8, column=0, sticky=W)

# Exit
Button(window, text="EXIT", width=6, command=close_window).grid(row=10, column=0, sticky=W)

# Run the main loop
window.mainloop()