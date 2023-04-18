from tkinter import *
from tkinter import filedialog, ttk
import os


title = 'писькин дришь'
root = Tk()
root.geometry('800x600')
root.title(title)


tabs = {'ky': 0}
tab_list = []
notebook = ttk.Notebook(root)
# --------------------

def open_file():
    textWidget = Text(root)
    file = open(filedialog.askopenfilename(), 'r')
    title = os.path.basename(file.name)
    add_tab(title)
    root.title(title + " - Senior Code Editor")
    data = file.read()
    textWidget.delete(1.0, "end")
    textWidget.insert(1.0, data)
    file.close()

def add_tab(name):
    notebook.pack(expand=True, fill='both')
    tab = Tab(notebook, name)
    print(name)
    notebook.add(tab, text=name)
    tab_list.append(tab)

def save_file():
    tab_to_save = get_tab()
    print(tab_to_save)
    tab_to_save.save_tab()

def get_tab():
    print(notebook.index('current'))
    #Get the tab object from the tab_list based on the index of the currently selected tab
    tab = tab_list[notebook.index('current')]
    return tab

def generate_tab():
    if tabs['ky'] < 20:
        tabs['ky'] += 1
        add_tab('Document ' + str(tabs['ky']))

def run():
        root.mainloop()


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New...", command= generate_tab)
filemenu.add_command(label="Open", command = open_file)
filemenu.add_command(label="Save", command= save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command= root.quit)
menubar.add_cascade(label="File", menu = filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
menubar.add_cascade(label="Edit", menu=editmenu)
root.config(menu=menubar)

class Tab(Frame):

    def __init__(self, root, name):
        Frame.__init__(self, root)

        self.root = root
        self.name = name

        self.textWidget = Text(self)
        self.textWidget.pack(fill='both', expand=True)

    def save_tab(self):
        print(self.textWidget.get("1.0", 'end-1c'))
        file = open(filedialog.asksaveasfilename() + '.txt', 'w+')
        file.write(self.textWidget.get("1.0", 'end-1c'))
        print(os.path.basename(file.name))
        #title = os.path.basename(file.name)
        file.close()



if __name__ == '__main__':
    print("running...")
    run()