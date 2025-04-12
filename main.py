import tkinter as tk
from PIL import Image, ImageTk
from linklist import DoublyLinkedList

class WindowGenerator:
    def __init__(self):
        self.current_window = tk.Tk()
        self.current_window.title("Image Viewer")
        self.current_window.geometry("500x500")
        self.current_window.config(bg="#bbc6a4")

        self.current_window.grid_rowconfigure(0, weight=1)
        self.current_window.grid_columnconfigure(0, weight=1)

    def add_frame(self, row, column, padx=10, pady=10, sticky='nsew'):
        frame = tk.Frame(self.current_window)
        frame.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        return frame

    def add_label(self, frame, row=0, column=0, padx=2, pady=2, sticky='nsew'):
        label = tk.Label(frame)
        label.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        return label

    def add_button(self, text, command, frame, row=0, column=0, padx=10, pady=10):
        button = tk.Button(frame, text=text, command=command, bg="#444b3b", fg="#ffffff")
        button.grid(row=row, column=column, padx=padx, pady=pady, sticky="nsew")
        return button

    def run(self):
        self.current_window.mainloop()


class App:
    def __init__(self):
        self.__generator = WindowGenerator()
        self.__dll = DoublyLinkedList()
        self.image_label = None
        self.image_ref = None
        self.setupMain()

    def setupMain(self):
        for i in range(1, 5):
            self.__dll.insert(f"sample{i}.jpg")

        frame = self.__generator.add_frame(row=0, column=0)

        self.image_label = self.__generator.add_label(frame=frame, row=0, column=0)

        self.__generator.add_button("Previous", self.gotoPrevious, frame=frame, row=1, column=0)
        self.__generator.add_button("Next", self.gotoNext, frame=frame, row=1, column=1)

        self.displayImage(self.__dll.current())
        self.__generator.run()

    def gotoNext(self):
        image_path = self.__dll.next()
        if image_path:
            self.displayImage(image_path)

    def gotoPrevious(self):
        image_path = self.__dll.prev()
        if image_path:
            self.displayImage(image_path)

    def displayImage(self, path):
        if not path:
            return

        try:
            image = Image.open(path)
            image = image.resize((400, 400), Image.Resampling.LANCZOS)
            self.image_ref = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.image_ref, text="")
        except Exception as e:
            self.image_label.config(image="", text=f"Error loading {path}")

if __name__ == "__main__":
    App()

