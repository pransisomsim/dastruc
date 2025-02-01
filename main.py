import tkinter as tk
from linklist import Queue

class WindowGenerator:
    def __init__(self):
        self.current_window = None

    def create_window(self, title):
        if self.current_window is not None:
            self.current_window.destroy()

        self.current_window = tk.Tk()
        self.current_window.title(title)
        self.current_window.geometry('400x400')
        self.current_window.config(bg='#bbc6a4')

        self.current_window.grid_rowconfigure(0, weight=1)
        self.current_window.grid_columnconfigure(0, weight=1)
        return self

    def add_frame(self, row, column, padx=10, pady=10, sticky='nsew',frame=None):
        frame = tk.Frame(frame if frame else self.current_window)
        frame.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        return frame

    def add_label(self, text, frame=None, row=0, column=0, padx=2, pady=2, sticky='nsew'):
        label = tk.Label(frame if frame else self.current_window, text=text)
        label.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        return label

    def add_button(self, text, command, frame=None, row=0, column=0, columnspan=1, padx=10, pady=10,bg='#444b3b',fg='#ffffff', sticky='nsew'):
        button = tk.Button(frame if frame else self.current_window, text=text, command=command, bg=bg, fg=fg)
        button.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        return button

    def run(self):
        if self.current_window:
            self.current_window.mainloop()


class App:
    def __init__(self):
        self.__generator = WindowGenerator()
        self.__queue = Queue()
        self.setupMain()

    def setupMain(self):
        for i in range(1, 5):
            self.__queue.enqueue(f'sample{i}.jpg')

        self.__generator.create_window('Image viewer')
        frame = self.__generator.add_frame(row=0, column=0, sticky='wes')
        self.__generator.add_button('Next', self.gotoNext, frame=frame, row=0, column=0)
        self.__generator.run()

    def gotoNext(self):
        self.__queue.display()

if __name__ == '__main__':
    App()