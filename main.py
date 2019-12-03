from tkinter import *
from tkinter import messagebox as msg
from tkinter import simpledialog
from tkinter import filedialog

import pandas as pd 
import csv

class CSV_FILE_CREATOR():
    def __init__(self,master):
        self.master = master
        self.master.title("Csv-File-Creator")
        self.master.geometry("250x120")
        self.master.resizable(False,False)
        # BUTTON

        self.createcsv = Button(self.master,text ="Create Csv File",command = self.createb)
        self.createcsv.pack()
        
        #MENU
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label ="Create Csv File",accelerator = 'Alt+O',command = self.createb)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        self.master.bind('<Alt-O>',lambda event:self.createb())
    
    #MENU FUNCTIONS
    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        msg.showinfo("Help","Press the create button")
    
    def aboutmenu(self):
        msg.showinfo("About","CSV FILE CREATOR \nVersion 1.0")
    
    def createb(self):
        """create csv file function """
        col = msg.askyesno("COLUMNS", "DO YOU WANT YOUR CSV FILE TO HAVE COLUMNS?")
        if col == False:
            fillcsv = msg.askyesno("FILL","DO YOU WANT TO FILL THE CSV FILE NOW")
            if fillcsv == False:
                filenamesave = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
                if ".csv" in filenamesave:
                    msg.showinfo("SUCCESS","THE CSV FILE SAVED SUCCESSFULLY")
                    pd.DataFrame(None,None).to_csv(filenamesave,index = False)
            else:
                numberoflinestofill = simpledialog.askinteger("NUMBER OF LINES","HOW MANY LINES DO YOU WANT TO WRITE",parent = self.master,minvalue = 1,maxvalue =50)
                """enter the name of the file you want to create"""
                filenamesave = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
                if ".csv" in filenamesave:
                    pd.DataFrame(None,None).to_csv(filenamesave,index = False)
                    with open(filenamesave,'a+') as f:
                        thewriter = csv.writer(f)
                        for i in range(numberoflinestofill):
                            csvwrite = simpledialog.askstring("CSV WRITER" , "Enter the line which will be added to the csv file seperated by ,", parent = self.master)
                            splited = csvwrite.split(",")
                            print(splited)
                            thewriter.writerow(splited)
                        f.close()
        else:
            header = simpledialog.askstring("COLUMN NAME", "Enter the names of the columns line seperated by ,", parent = self.master)
            spheader = header.split(",")
            filenamesave = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
            if ".csv" in filenamesave:
                pd.DataFrame(columns = spheader).to_csv(filenamesave,index = False)
                fillcsv = msg.askyesno("FILL","DO YOU WANT TO FILL THE CSV FILE NOW")
                if fillcsv == False:
                    msg.showinfo("SUCCESS","THE CSV FILE SAVED SUCCESSFULLY")
                else:
                    numberoflinestofill = simpledialog.askinteger("NUMBER OF LINES","HOW MANY LINES DO YOU WANT TO WRITE",parent = self.master,minvalue = 1,maxvalue =50)
                """enter the name of the file you want to create"""
                filenamesave = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
                if ".csv" in filenamesave:
                    pd.DataFrame(None,None).to_csv(filenamesave,index = False)
                    with open(filenamesave,'a+') as f:
                        thewriter = csv.writer(f)
                        for i in range(numberoflinestofill):
                            csvwrite = simpledialog.askstring("CSV WRITER" , "Enter the line which will be added to the csv file seperated by ,", parent = self.master)
                            splited = csvwrite.split(",")
                            print(splited)
                            thewriter.writerow(splited)
                        f.close()
                    
                    
            
            

def main():
    root=Tk()
    CFC = CSV_FILE_CREATOR(root)
    root.mainloop()
    
if __name__=='__main__':
    main()
