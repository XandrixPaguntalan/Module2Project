import tkinter as tk

class Keypad(tk.Frame):

    cells = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#'],
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target = None
        for y, row in enumerate(self.cells):
            for x, item in enumerate(row):
                b = tk.Button(self, text=item, command=lambda text=item:self.append(text))
                b.grid(row=y, column=x, sticky='news')

        x = tk.Button(self, text='Backspace', command=self.backspace)
        x.grid(row=0, column=10, sticky='news')
        x = tk.Button(self, text='Clear', command=self.clear)
        x.grid(row=1, column=10, sticky='news')
        x = tk.Button(self, text='Hide', command=self.hide)
        x.grid(row=10, column=0, columnspan=11, sticky='news')

    def get(self):
        if self.target:
            return self.target.get()
    def append(self, text):
        if self.target:
            self.target.insert('end', text)
    def clear(self):
        if self.target:
            self.target.delete(0, 'end')
    def backspace(self):
        if self.target:
            text = self.get()
            text = text[:-1]
            self.clear()
            self.append(text)
    def show(self, show):
        self.target = show
        self.place(relx=0.5, rely=0.5, anchor='c')
    def hide(self):
        self.target = None
        self.place_forget()

root = tk.Tk()
root.geometry('300x300')
keypad = Keypad(root)
f = tk.Frame(root)
f.pack()
e1 = tk.Entry(f)
e1.grid(row=0, column=0, sticky='news')
b1 = tk.Button(f, text='Keypad', command=lambda:keypad.show(e1))
b1.grid(row=0, column=1, sticky='news')

root.mainloop()