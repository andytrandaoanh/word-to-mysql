import tkinter as tk
import lexicon_gui
from db_updater import upload_data



win = tk.Tk()

win.title("Upload Words To MySQL")
win.geometry("760x540") 
win.resizable(0, 0) 


myGUI = lexicon_gui.LexGUI(win)

myGUI.createGUI()


win.mainloop()