from tkinter import Tk
from guiFP import GUI

def main():
    root = Tk()
    root.title('Area Calculator')
    root.geometry('600x600')
    root.resizable(False, False)

    gui = GUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
