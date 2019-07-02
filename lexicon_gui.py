import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import config_handler
import text_processor




class LexGUI:



    def __init__(self, win):
    	self.master = win
    	



    def createTabs(self):
        s = ttk.Style()
        s.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [40, 10],
                                        "font" : ('URW Gothic L', '11', 'bold')},}})
        s.theme_use("MyStyle")
        s.configure('TButton', relief='raised', padding= 6)
        

        self.tabControl = ttk.Notebook(self.master)
        
        self.tab1 = ttk.Frame(self.tabControl)
        #self.tab2 = ttk.Frame(self.tabControl)
        #self.tab3 = ttk.Frame(self.tabControl)
        #self.tab4 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text = 'Upload To MySQL')
        #self.tabControl.add(self.tab2, text = 'Recycle')      
        #self.tabControl.add(self.tab3, text = 'Settings')
        #self.tabControl.add(self.tab4, text = 'Upload')


        #display tabs
        self.tabControl.pack(expand = 1, fill = "both")

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "E:/FULLTEXT/DATABASE", 
            title = "Select a file", 
            filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
        if (self.filename):
            self.filepath.set(self.filename) 
            
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_FILE,self.filename)

    def dirDialog(self):
        self.filename2 = filedialog.askdirectory()
        if (self.filename2):
            self.filepath2.set(self.filename2) #set the textbox to the file path        
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OUTPUT_DIR,self.filename2)

    def saveBookID(self):       
        cf = config_handler.ConfigHandler()
        cf.set_config_value(cf.RECENT_BOOK_ID,str(self.bookid.get()))

   
    def uploadData(self):
        if(self.filepath.get() and self.bookid.get()):
            text_processor.prepareForUpload(self.filepath.get(), self.bookid.get())
        else:
            messagebox.showwarning("Error", "Missing input file databse ID")
   
    def createTab1(self):
        #frame

        self.labelFrame = ttk.LabelFrame(self.tab1, text= 'Select a word data file:')
        self.labelFrame.grid(column=0, row=0, padx = 20, pady = 20)

        s = ttk.Style()
        s.configure('TEntry', font = ('Courier', 24), padding = 4)


        #textbox 1
        self.filepath = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OPEN_FILE)
        self.filepath.set(value) 
        self.path3 = ttk.Entry(self.labelFrame, width=90, textvariable = self.filepath)
        self.path3.grid(column = 0, row =1, sticky = "w")
        
   

        #button 1
        self.button1 = ttk.Button(self.labelFrame, text = "Browse A File", command=self.fileDialog)
        self.button1.grid(column = 1, row = 1, sticky = "w")


 
        #label 7
        self.label7 = ttk.Label(self.labelFrame, text="Book ID:")
        self.label7.grid(column = 0, row = 2, sticky = "w")

        #textbox 4
        self.bookid = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_BOOK_ID)

        self.bookid.set(value) 
        self.textbox4 = ttk.Entry(self.labelFrame, width=90, textvariable = self.bookid)
        self.textbox4.grid(column = 0, row = 3, sticky = "w")
      
        #button no 6
        self.button6 = ttk.Button(self.labelFrame, text = "Save ID", command=self.saveBookID)
        self.button6.grid(column = 1, row = 3, sticky = "w")

         #label 7
        self.label8 = ttk.Label(self.labelFrame, text="Click button to start processing text:")
        self.label8.grid(column = 0, row = 4, sticky = "w")
        #button no 7
        self.button7 = ttk.Button(self.labelFrame, text = "Start Upload", command=self.uploadData)
        self.button7.grid(column = 0, row = 5)

  

        

    def createGUI(self):
        self.createTabs()    
        self.createTab1()
  