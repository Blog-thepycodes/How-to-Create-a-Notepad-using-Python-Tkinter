from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
 
 
#creating the main window
root = Tk()
root.title("NotePad - The Pycodes")
root.geometry("600x600")
root.config(bg='lightblue')
 
 
#defining functions
def save_file():
    file = filedialog.asksaveasfile(defaultextension='.txt')
    if file:
        text = text_editor.get(1.0,END)
        file.write(text)
        file.close()
 
 
def open_file():
    file = filedialog.askopenfile(filetype=[('text files','*.txt')])
    if file:
        content = file.read()
        text_editor.delete(1.0,END)
        text_editor.insert(INSERT,content)
 
 
#creating menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)
 
 
#creating a file menu with options
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Open File",command=open_file)
file_menu.add_command(label="Save File",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
 
 
#adding a text editor area
text_editor = scrolledtext.ScrolledText(root,wrap=WORD,width=60,height=50)
text_editor.pack(pady=20)
 
 
#running the GUI application
root.mainloop()
