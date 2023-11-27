# import tkinter as tk
# tk._test()
###############################################################################
# import tkinter as tk
# from tkinter import ttk # Themed Tkinter(uses for widgets and buttons) 

# def greet():
#     print("Hello world")
    
# root = tk.Tk()
# root.title("Hello")

# greet_button = ttk.Button(root, text="Greet", command=greet)
# greet_button.pack(side="left", fill="x", expand=True)

# quit_button = ttk.Button(root, text="Quit", command=root.destroy)
# quit_button.pack(side="left", fill="x", expand=True)

# root.mainloop()

# greet()
###############################################################################


##################################
# Program-2 Labels and Fields
##################################

# import tkinter as tk
# from tkinter import ttk # Themed Tkinter(uses for widgets and buttons) 

# def greet():
#     print(f"Welcome, {user_name.get() or 'world' }")

# root = tk.Tk()
# root.title("Greeter")

# user_name = tk.StringVar() # "StringVar" is an object to track the ttk entry(as mentioned in line:42). 

# name_label = ttk.Label(root, text="Name: ")
# name_label.pack(side="left", padx=(0, 10))
# name_entry = ttk.Entry(root, width=15, textvariable=user_name)
# name_entry.pack(side="left")
# name_entry.focus()

# greet_button = ttk.Button(root, text="Greet", command=greet)
# greet_button.pack(side="left", fill="x", expand=True)

# root.mainloop()


##################################
# Program-3 Packing Components
##################################

# import tkinter as tk

# root = tk.Tk()

# # Indian Flag
# tk.Label(root, bg="orange").pack(side="top", fill="both", expand="True")
# tk.Label(root, bg="white").pack(side="top", fill="both", expand="True")
# tk.Label(root, bg="green").pack(side="top", fill="both", expand="True")

# # Russion Flag
# tk.Label(root, bg="blue").pack(side="top", fill="both", expand="True")
# tk.Label(root, bg="white").pack(side="top", fill="both", expand="True")
# tk.Label(root, bg="red").pack(side="top", fill="both", expand="True")

# root.mainloop()


################################################
# Program-4 Tkinter notebooks and creating files
################################################

# import tkinter as tk
# import tkinter.ttk as ttk

# def create_file():
#     text_area = tk.Text(notebook)
#     text_area.pack(fill="both", expand=True)

#     notebook.add(text_area, text="Untitled")
#     notebook.select(text_area)
    
# root = tk.Tk()

# main = ttk.Frame(root)
# main.pack(expand="True", fill="both", padx=1, pady=(4, 0))

# notebook = ttk.Notebook(None)
# notebook.pack(fill="both", expand=True)
# create_file()
# create_file()

# root.mainloop()


################################################
# Program-5 Adding a menu
################################################

# import tkinter as tk
# import tkinter.ttk as ttk

# def create_file():
#     text_area = tk.Text(notebook)
#     text_area.pack(fill="both", expand=True)

#     notebook.add(text_area, text="Untitled")
#     notebook.select(text_area)
    
# root = tk.Tk()
# root.title("Vasu Text Editor")
# root.option_add("*tearoff", False)

# main = ttk.Frame(root)
# main.pack(expand="True", fill="both", padx=1, pady=(4, 0))
# menubar = tk.Menu()
# root.config(menu=menubar)

# file_menu = tk.Menu(menubar)
# menubar.add_cascade(menu=file_menu, label="File")

# file_menu.add_command(label="New", command=create_file)

# notebook = ttk.Notebook(None)
# notebook.pack(fill="both", expand=True)
# create_file()

# root.mainloop()


################################################
# Program-6 Saving files to desk
################################################

# import os
# import tkinter as tk
# import tkinter.ttk as ttk
# import tkinter.filedialog as filedialog 

# def create_file():
#     text_area = tk.Text(notebook)
#     text_area.pack(fill="both", expand=True)

#     notebook.add(text_area, text="Untitled")
#     notebook.select(text_area)


# def save_file():
#     file_path = filedialog.asksaveasfilename()

#     try:
#         filename = os.path.basename(file_path)
#         text_widget = root.nametowidget(notebook.select())
#         content = text_widget.get("1.0", "end-1c")

#         with open(file_path, "w") as file:
#             file.write(content)

#     except (AttributeError, FileNotFoundError):
#         print("Save operation cancelled")
#         return

#     notebook.tab("current", text=filename)


# root = tk.Tk()
# root.title("Teclado Text Editor")
# root.option_add("*tearOff", False)

# main = ttk.Frame(root)
# main.pack(fill="both", expand=True, padx=(1), pady=(4, 0))

# menubar = tk.Menu(root)
# root.config(menu=menubar)

# file_menu = tk.Menu(menubar)

# menubar.add_cascade(menu=file_menu, label="File")

# file_menu.add_command(label="New", command=create_file)
# file_menu.add_command(label="Save", command=save_file)

# notebook = ttk.Notebook(main)
# notebook.pack(fill="both", expand=True)

# create_file()

# root.mainloop()


################################################
# Program-7 Openning files
################################################

# import os
# import tkinter as tk
# import tkinter.ttk as ttk
# import tkinter.filedialog as filedialog 

# def create_file(content="", title="Untitled"):
#     text_area = tk.Text(notebook)
#     text_area.insert("end", content)
#     text_area.pack(fill="both", expand=True)
#     notebook.add(text_area, text=title)
#     notebook.select(text_area)


# def save_file():
#     file_path = filedialog.asksaveasfilename()

#     try:
#         filename = os.path.basename(file_path)
#         text_widget = root.nametowidget(notebook.select())
#         content = text_widget.get("1.0", "end-1c")

#         with open(file_path, "w") as file:
#             file.write(content)

#     except (AttributeError, FileNotFoundError):
#         print("Save operation cancelled")
#         return

#     notebook.tab("current", text=filename)


# def open_file():
#     file_path = filedialog.askopenfilename()
    
#     try:
#         filename = os.path.basename(file_path)
        
#         with open(file_path, "r") as file:
#             content = file.read()
#     except(AttributeError, FileNotFoundError):
#         print("Open operation cancelled")
#         return
    
#     create_file(content, filename)
    
# root = tk.Tk()
# root.title("Teclado Text Editor")
# root.option_add("*tearOff", False)

# main = ttk.Frame(root)
# main.pack(fill="both", expand=True, padx=(1), pady=(4, 0))

# menubar = tk.Menu(root)
# root.config(menu=menubar)

# file_menu = tk.Menu(menubar)

# menubar.add_cascade(menu=file_menu, label="File")

# file_menu.add_command(label="New", command=create_file)
# file_menu.add_command(label="Open...", command=open_file)
# file_menu.add_command(label="Save", command=save_file)

# notebook = ttk.Notebook(main)
# notebook.pack(fill="both", expand=True)
# create_file()

# root.mainloop()


################################################
# Program-8 Binding shortcuts in Tkinter
################################################

# import os
# import tkinter as tk
# import tkinter.ttk as ttk
# import tkinter.filedialog as filedialog 

# def create_file(content="", title="Untitled"):
#     text_area = tk.Text(notebook)
#     text_area.insert("end", content)
#     text_area.pack(fill="both", expand=True)
#     notebook.add(text_area, text=title)
#     notebook.select(text_area)


# def save_file():
#     file_path = filedialog.asksaveasfilename()

#     try:
#         filename = os.path.basename(file_path)
#         text_widget = root.nametowidget(notebook.select())
#         content = text_widget.get("1.0", "end-1c")

#         with open(file_path, "w") as file:
#             file.write(content)

#     except (AttributeError, FileNotFoundError):
#         print("Save operation cancelled")
#         return

#     notebook.tab("current", text=filename)


# def open_file():
#     file_path = filedialog.askopenfilename()
    
#     try:
#         filename = os.path.basename(file_path)
        
#         with open(file_path, "r") as file:
#             content = file.read()
#     except(AttributeError, FileNotFoundError):
#         print("Open operation cancelled")
#         return
    
#     create_file(content, filename)
    
# root = tk.Tk()
# root.title("Teclado Text Editor")
# root.option_add("*tearOff", False)

# main = ttk.Frame(root)
# main.pack(fill="both", expand=True, padx=(1), pady=(4, 0))

# menubar = tk.Menu(root)
# root.config(menu=menubar)

# file_menu = tk.Menu(menubar)

# menubar.add_cascade(menu=file_menu, label="File")

# file_menu.add_command(label="New", command=create_file, accelerator="Ctrl+N")
# file_menu.add_command(label="Open...", command=open_file, accelerator="Ctrl+O")
# file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")

# notebook = ttk.Notebook(main)
# notebook.pack(fill="both", expand=True)
# create_file()

# root.bind("<Control-n>", lambda event: create_file())
# root.bind("<Control-o>", lambda event: open_file())
# root.bind("<Control-s>", lambda event: save_file())

# root.mainloop()


#################################################
# Program-9 Checking our tabs for unsaved changes
#################################################

# import os
# import tkinter as tk
# import tkinter.ttk as ttk
# import tkinter.filedialog as filedialog 

# text_contents = dict()

# def create_file(content="", title="Untitled"):
#     text_area = tk.Text(notebook)
#     text_area.insert("end", content)
#     text_area.pack(fill="both", expand=True)
#     notebook.add(text_area, text=title)
#     notebook.select(text_area)
    
#     text_contents[str(text_area)] = hash(content)
#     print(str(text_area))

# def check_for_changes():
#     current = get_text_widget()
#     content = current.get("1.0", "end-1c")
#     name = notebook.tab("current")["text"]
    
#     if hash(content) != text_contents[str(current)]:
#         if name[-1] != "*":
#             notebook.tab("current", text=name + "*")
#     elif name[-1] == "*":
#         notebook.tab("current", text=name[:-1])
        
# def get_text_widget():
#     text_widget = root.nametowidget(notebook.select())
#     return text_widget

# def save_file():
#     file_path = filedialog.asksaveasfilename()

#     try:
#         filename = os.path.basename(file_path)
#         text_widget = get_text_widget()
#         content = text_widget.get("1.0", "end-1c")

#         with open(file_path, "w") as file:
#             file.write(content)

#     except (AttributeError, FileNotFoundError):
#         print("Save operation cancelled")
#         return

#     notebook.tab("current", text=filename)


# def open_file():
#     file_path = filedialog.askopenfilename()
    
#     try:
#         filename = os.path.basename(file_path)
        
#         with open(file_path, "r") as file:
#             content = file.read()
#     except(AttributeError, FileNotFoundError):
#         print("Open operation cancelled")
#         return
    
#     create_file(content, filename)
    
# root = tk.Tk()
# root.title("Teclado Text Editor")
# root.option_add("*tearOff", False)

# main = ttk.Frame(root)
# main.pack(fill="both", expand=True, padx=(1), pady=(4, 0))

# menubar = tk.Menu(root)
# root.config(menu=menubar)

# file_menu = tk.Menu(menubar)

# menubar.add_cascade(menu=file_menu, label="File")

# file_menu.add_command(label="New", command=create_file, accelerator="Ctrl+N")
# file_menu.add_command(label="Open...", command=open_file, accelerator="Ctrl+O")
# file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")

# notebook = ttk.Notebook(main)
# notebook.pack(fill="both", expand=True)
# create_file()

# root.bind("<KeyPress>", lambda event: check_for_changes())
# root.bind("<Control-n>", lambda event: create_file())
# root.bind("<Control-o>", lambda event: open_file())
# root.bind("<Control-s>", lambda event: save_file())

# root.mainloop()

#################################################
# Program-17 Adding Menus
#################################################
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

text_contents = dict()


def check_for_changes():
    current = get_text_widget()
    content = current.get("1.0", "end-1c")
    name = notebook.tab("current")["text"]

    if hash(content) != text_contents[str(current)]:
        if name[-1] != "*":
            notebook.tab("current", text=name + "*")
    elif name[-1] == "*":
        notebook.tab("current", text=name[:-1])


def get_text_widget():
    current_tab = get_current_tab()
    text_widget = current_tab.winfo_children()[0]

    return text_widget


def get_current_tab():
    return notebook.nametowidget(notebook.select())


def close_current_tab():
    if current_tab_unsaved() and not confirm_close():
        return

    current_tab = get_current_tab()

    if len(notebook.tabs()) == 1:
        create_file()

    notebook.forget(current_tab)


def current_tab_unsaved():
    text_widget = get_text_widget()
    content = text_widget.get("1.0", "end-1c")
    return hash(content) != text_contents[str(text_widget)]


def confirm_close():
    return messagebox.askyesno(
        message="You have unsaved changes. Are you sure you want to close?",
        icon="question",
        title="Unsaved changes",
    )


def confirm_quit():
    unsaved = False

    for tab in notebook.tabs():
        tab_widget = root.nametowidget(tab)
        text_widget = tab_widget.winfo_children()[0]
        content = text_widget.get("1.0", "end-1c")

        if hash(content) != text_contents[str(text_widget)]:
            unsaved = True
            break

    if unsaved and not confirm_close():
        return

    root.destroy()


def create_file(content="", title="Untitled"):
    container = ttk.Frame(notebook)
    container.pack()

    text_area = tk.Text(container)
    text_area.insert("end", content)
    text_area.pack(side="left", fill="both", expand=True)

    notebook.add(container, text=title)
    notebook.select(container)

    text_contents[str(text_area)] = hash(content)

    text_scroll = ttk.Scrollbar(container, orient="vertical", command=text_area.yview)
    text_scroll.pack(side="right", fill="y")
    text_area["yscrollcommand"] = text_scroll.set


def open_file():
    file_path = filedialog.askopenfilename()

    try:
        filename = os.path.basename(file_path)

        with open(file_path, "r") as file:
            content = file.read()

    except (AttributeError, FileNotFoundError):
        print("Open operation cancelled")
        return

    create_file(content, filename)


def save_file():
    file_path = filedialog.asksaveasfilename()

    try:
        filename = os.path.basename(file_path)
        text_widget = get_text_widget()
        content = text_widget.get("1.0", "end-1c")

        with open(file_path, "w") as file:
            file.write(content)

    except (AttributeError, FileNotFoundError):
        print("Save operation cancelled")
        return

    notebook.tab("current", text=filename)
    text_contents[str(text_widget)] = hash(content)


def show_about_info():
    messagebox.showinfo(
        title="About",
        message="The Teclado Text Editor is a simple tabbed text editor designed to help you learn Tkinter!",
    )


root = tk.Tk()
root.title("Teclado Text Editor")
root.option_add("*tearOff", False)

main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=(1), pady=(4, 0))

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
help_menu = tk.Menu(menubar)

menubar.add_cascade(menu=file_menu, label="File")
menubar.add_cascade(menu=help_menu, label="Help")

file_menu.add_command(label="New", command=create_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open...", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(
    label="Close Tab", command=close_current_tab, accelerator="Ctrl+Q"
)
file_menu.add_command(label="Exit", command=confirm_quit)

help_menu.add_command(label="About", command=show_about_info)

notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)

create_file()

root.bind("<KeyPress>", lambda event: check_for_changes())
root.bind("<Control-n>", lambda event: create_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-q>", lambda event: close_current_tab())
root.bind("<Control-s>", lambda event: save_file())

root.mainloop()