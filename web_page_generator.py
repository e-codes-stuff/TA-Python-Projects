import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.label = Label(self.master, text="Add custom text here")
        self.label.grid(padx=(10, 10), pady=(10, 0))

        self.text_entry = Entry(self.master, width=30)
        self.text_entry.grid(padx=(10, 10), pady=(0, 10))

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10, 10), pady=(10, 10))

        self.custom_btn = Button(self.master, text="Custom HTML Page", width=30, height=2, command=self.customHTML)
        self.custom_btn.grid(padx=(10, 10), pady=(10, 10))

    def defaultHTML(self):
        html_text = "Stay tuned for our amazing summer sale!"
        html_file = open("index.html", "w")
        html_content = "<html>\n<body>\n<h1>" + html_text + "</h1>\n</body>\n</html>"
        html_file.write(html_content)
        html_file.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        html_text = self.text_entry.get()
        html_file = open("index.html", "w")
        html_content = "<html>\n<body>\n<h1>" + html_text + "</h1>\n</body>\n</html>"
        html_file.write(html_content)
        html_file.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()