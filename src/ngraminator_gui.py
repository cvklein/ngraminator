#trying tkinter


from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from find_ngrams import process_input_gui

separators = ['，','。','；','？','「','」','：','！','《','》','、','．']

gui = Tk()
gui.geometry("800x400")
gui.title("FC")



#adpting from https://stackoverflow.com/questions/51877124/how-to-select-a-directory-and-store-it-into-a-variable-in-tkinter
#but mutiple files rather than folders

class FolderSelect(Frame):
    def __init__(self,parent=None,folderDescription="",**kw):
        Frame.__init__(self,master=parent,**kw)
        self.folderPath = StringVar()
        self.lblName = Label(self, text=folderDescription)
        self.lblName.grid(row=0,column=0)
        self.entPath = Entry(self, textvariable=self.folderPath)
        self.entPath.grid(row=0,column=1)
        self.btnFind = ttk.Button(self, text="Browse For Files",command=self.setFolderPath)
        self.btnFind.grid(row=0,column=2)
    def setFolderPath(self):
        folder_selected = filedialog.askopenfilenames() #note that this allows for selection of multiple filenames
        self.folderPath.set(folder_selected)
    @property
    def folder_path(self):
        return self.folderPath.get()



#messy cleanup of returned line from file select dialog

def cleanup(s):
    s = s[1:-2]
    s = s.replace("'","")
    s = s.replace(" /","/")
    s = s.split(',')
    return s

def doStuff():
    files1 = cleanup(directory1Select.folder_path)

    files2 = cleanup(directory2Select.folder_path)
    process_input_gui(files1,files2,'test.xlsx',4,separators)



folderPath = StringVar()

directory1Select = FolderSelect(gui,"Select Folder 1")
directory1Select.grid(row=0)

directory2Select = FolderSelect(gui,"Select Folder 2")
directory2Select.grid(row=1)




c = ttk.Button(gui, text="Ngraminate!", command=doStuff)
c.grid(row=4,column=0)
gui.mainloop()
