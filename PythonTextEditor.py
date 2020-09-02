from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext

filename = None

#The following methods are called in the filemenu of the window
def newFile():
    '''
    Creates a new file to be edited and saved
    '''
    global filename
    filename = None
    editor.title("untitled.txt")
    text.delete(0.0, END)
    
def saveFile():
    '''
    Saves all edits from previously saved .txt file. If not previously saved, saveAs is called in exception.
    '''
    global filename
    #within filename, all text from 0th row and 0th column to the end is gotten
    t = text.get(0.0, END)
    #file is saved under provided filename and text is written
    try:
        f = open(filename, 'w')
        f.write(t)
        f.close
    except:
        #if the file isn't already created, this does a saveAs
        f = filedialog.asksaveasfile(confirmoverwrite=False, mode = 'w', defaultextension = '.txt')
        t = text.get(0.0, END)
        try:
            filename = f.name
            display_name = filename[filename.rindex('/')+1:]
            f.write(t)
            editor.title(f"{display_name}")
        except:
            messagebox.showerror(title = "Oops!", message = "Unable to save file...")


def saveAs():
    '''
    Saves text in OS under designated name with default .txt extension
    '''
    global filename
    f = filedialog.asksaveasfile(confirmoverwrite=False, mode = 'w', defaultextension = '.txt')
    t = text.get(0.0, END)
    try:
        filename = f.name
        display_name = filename[filename.rindex('/')+1:]
        f.write(t)
        editor.title(f"{display_name}")
    except:
        messagebox.showerror(title = "Oops!", message = "Unable to save file...")
        
        
def openFile():
    '''
    Opens a .txt file created prior and displays text to edit
    '''
    global filename
    f = filedialog.askopenfile(mode = 'r')
    filename = f.name
    display_name = filename[filename.rindex('/')+1:]
    editor.title(f"{display_name}")
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

    
#setting up text editing window with Tkinter
editor = Tk()
editor.title("untitled.txt")
editor.minsize(width = 500, height = 380)
editor.maxsize(width = 500, height = 380)

#adding text editing feature with scroll bar to Tkinter window
text = scrolledtext.ScrolledText(editor, undo=True)
text['font'] = ('consolas', '14')
text.pack(expand=True, fill='both')

#adding menu bar to Tkinter window
menubar = Menu(editor)

#filemenu items
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
menubar.add_cascade(label="File", menu=filemenu)

#editmenu items
editmenu = Menu(menubar, tearoff=1)
editmenu.add_command(label="Undo", command=text.edit_undo)
editmenu.add_command(label="Redo", command=text.edit_redo)
editmenu.add_separator()
menubar.add_cascade(label="Edit", menu=editmenu)


editor.config(menu=menubar)
editor.mainloop()

