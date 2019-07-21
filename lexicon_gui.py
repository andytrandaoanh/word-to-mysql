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
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text = 'Words to MySQL')
        self.tabControl.add(self.tab2, text = 'Stop Words')      
        self.tabControl.add(self.tab3, text = 'Mappings')
        self.tabControl.add(self.tab4, text = 'Word Pairs')


        #display tabs
        self.tabControl.pack(expand = 1, fill = "both")

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "E:/FULLTEXT/WORD/DATABASE", 
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

    def fileDialog2(self):
        self.filename21 = filedialog.askopenfilename(initialdir = "E:/FULLTEXT/DICTIONARY/SPECIALTY", 
            title = "Select a file", 
            filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
        if (self.filename21):
            self.filepath21.set(self.filename21) 
            
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_FILE_2,self.filename21)

    def uploadData2(self):
        if(self.filepath21.get()):
            text_processor.uploadSpecialWords(self.filepath21.get())
        else:
            messagebox.showwarning("Error", "Missing input file")
  
    def createTab2(self):
        #frame
        
        self.labelFrame2 = ttk.LabelFrame(self.tab2, text= 'Select a stop-word data file:')
        self.labelFrame2.grid(column=0, row=0, padx = 20, pady = 20)

        #textbox 21
        self.filepath21 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OPEN_FILE_2)
        self.filepath21.set(value) 
        self.path21 = ttk.Entry(self.labelFrame2, width=90, textvariable = self.filepath21)
        self.path21.grid(column = 0, row =1, sticky = "w")
        
   

        #button 21
        self.button21 = ttk.Button(self.labelFrame2, text = "Browse A File", command=self.fileDialog2)
        self.button21.grid(column = 1, row = 1, sticky = "w")

         #label 21
        self.label21 = ttk.Label(self.labelFrame2, text="Click button to start processing text:")
        self.label21.grid(column = 0, row = 4, sticky = "w")
        #button no 22
        self.button22 = ttk.Button(self.labelFrame2, text = "Start Upload", command=self.uploadData2)
        self.button22.grid(column = 0, row = 5)

    def fileDialog31(self):
        self.filename31 = filedialog.askopenfilename(initialdir = "E:/FULLTEXT/MAP/CLEANMAP", 
            title = "Select a file", 
            filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
        if (self.filename31):
            self.filepath31.set(self.filename31) 
            
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_FILE_3,self.filename31)

    def uploadData31(self):
        if(self.filepath31.get()):
            text_processor.uploadMappings(self.filepath31.get())
        else:
            messagebox.showwarning("Error", "Missing input file")
  
    def createTab3(self):
        #frame
        
        self.labelFrame3 = ttk.LabelFrame(self.tab3, text= 'Select a mapping data file:')
        self.labelFrame3.grid(column=0, row=0, padx = 20, pady = 20)

        #textbox 31
        self.filepath31 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OPEN_FILE_3)
        self.filepath31.set(value) 
        self.path31 = ttk.Entry(self.labelFrame3, width=90, textvariable = self.filepath31)
        self.path31.grid(column = 0, row =1, sticky = "w")
        
   

        #button 31
        self.button31 = ttk.Button(self.labelFrame3, text = "Browse A File", command=self.fileDialog31)
        self.button31.grid(column = 1, row = 1, sticky = "w")

         #label 31
        self.label31 = ttk.Label(self.labelFrame3, text="Click button to start processing text:")
        self.label31.grid(column = 0, row = 4, sticky = "w")
        #button no 32
        self.button32 = ttk.Button(self.labelFrame3, text = "Start Upload", command=self.uploadData31)
        self.button32.grid(column = 0, row = 5)


    def fileDialog41(self):
        self.filename41 = filedialog.askopenfilename(initialdir = "E:/FULLTEXT/PAIR/CLEANMERGE", 
            title = "Select a file", 
            filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
        if (self.filename41):
            self.filepath41.set(self.filename41) 
            
            cf = config_handler.ConfigHandler()
            cf.set_config_value(cf.RECENT_OPEN_FILE_4,self.filename41)

    def uploadData41(self):
        if(self.filepath41.get()):
            text_processor.uploadWordPairs(self.filepath41.get())
        else:
            messagebox.showwarning("Error", "Missing input file")
  
    def createTab4(self):

        self.labelFrame4 = ttk.LabelFrame(self.tab4, text= 'Select a word pair file:')
        self.labelFrame4.grid(column=0, row=0, padx = 20, pady = 20)

        #textbox 41
        self.filepath41 = tk.StringVar()
        #load config value
        cf = config_handler.ConfigHandler()
        value = cf.get_config_value(cf.RECENT_OPEN_FILE_4)
        self.filepath41.set(value) 
        self.path41 = ttk.Entry(self.labelFrame4, width=90, 
            textvariable = self.filepath41)
        self.path41.grid(column = 0, row =1, sticky = "w")
        
   

        #button 41
        self.button41 = ttk.Button(self.labelFrame4, text = "Browse A File", command=self.fileDialog41)
        self.button41.grid(column = 1, row = 1, sticky = "w")

         #label 41
        self.label41 = ttk.Label(self.labelFrame4, text="Click button to start processing text:")
        self.label41.grid(column = 0, row = 4, sticky = "w")
        #button no 32
        self.button42 = ttk.Button(self.labelFrame4, text = "Start Upload", command=self.uploadData41)
        self.button42.grid(column = 0, row = 5)


    def createGUI(self):
        self.createTabs()    
        self.createTab1()
        self.createTab2()
        self.createTab3()
        self.createTab4()
  
  