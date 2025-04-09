import tkinter as tk
from courses import *

# C in CRUD dialog to ask for new course name
class CreateUI:
    def __init__(self, newCS, parent):
        self.cs = newCS
        self.parent = parent

    def click(self):
        c = Course(None, self.entry.get())
        self.cs.create(c) 
        self.dialog.destroy()

    def createClick(self):
        self.dialog = tk.Toplevel(self.parent)
        label = tk.Label(self.dialog, text="New Course Number")
        self.entry = tk.Entry(self.dialog, width = 10)

        add = tk.Button(self.dialog, text = "Add Course", command = self.click)
        cancel = tk.Button(self.dialog, text = "Cancel", command = self.dialog.destroy)
        
        label.pack()
        self.entry.pack()
        add.pack()
        cancel.pack()
        self.dialog.lift(self.parent)

# U in CRUD to update an entry in the database
class UpdateUI:
    def __init__(self,newCS,parent):
        self.cs = newCS #COMPLETED
        self.parent = parent
        self.update_id = None # added this so I can store the ID value later

    def click(self):
        c = Course(self.update_id, self.entry.get())
        self.cs.update(c) 
        self.dialog.destroy()

    def retrieveID(self):
        self.dialog = tk.Toplevel(self.parent)
        label = tk.Label(self.dialog, text = "ID of Course to Update") # creates a dialog which prompts for the ID of the course to be updated
        self.entry_id = tk.Entry(self.dialog, width = 10)

        confirm = tk.Button(self.dialog, text = "Confirm", command = self.updateClick)
        cancel = tk.Button(self.dialog, text = "Cancel", command = self.dialog.destroy)

        label.pack()
        self.entry_id.pack()
        confirm.pack()
        cancel.pack()
        self.dialog.lift(self.parent)

    def updateClick(self):
        self.update_id = self.entry_id.get()  # if user hits 'Confirm' the ID is stored
        self.dialog.destroy() # deletes old dialog

        self.dialog = tk.Toplevel(self.parent)
        label = tk.Label(self.dialog, text = "New Course Name") # creates new dialog which will update the course name with input
        self.entry = tk.Entry(self.dialog, width = 10)

        update = tk.Button(self.dialog, text= "Update Course",command=self.click)
        cancel = tk.Button(self.dialog ,text= "Cancel",command=self.dialog.destroy)

        label.pack()
        self.entry.pack()
        update.pack()
        cancel.pack()
        self.dialog.lift(self.parent) 

# D in CRUD to delete and entry in the database
class DeleteUI:
    def __init__(self,newCS,parent):
        self.cs = newCS
        self.parent = parent
    def click(self):
        c = Course(self.entry.get(), None)
        self.cs.delete(c) 
        self.dialog.destroy()
    def deleteClick(self):
        self.dialog = tk.Toplevel(self.parent)
        label = tk.Label(self.dialog, text = "ID of Course to Delete")
        self.entry = tk.Entry(self.dialog, width = 10)
     
        delete = tk.Button(self.dialog, text = "Delete Course", command = self.click)
        cancel = tk.Button(self.dialog, text = "Cancel", command = self.dialog.destroy)
        
        label.pack()
        self.entry.pack()
        delete.pack()
        cancel.pack()
        self.dialog.lift(self.parent)        
        
def refreshList(cs, text):
    text.config(state = "normal")
    text.delete(1.0, tk.END)
    text.insert(tk.END, cs.retrieve())
    text.config(state = "disabled")

window = tk.Tk()
cs = Courses()

createui = CreateUI(cs, window)
updateui = UpdateUI(cs, window)
deleteui = DeleteUI(cs, window)

createButton = tk.Button(text = "Add Course", command = createui.createClick)
updateButton = tk.Button(text = "Update Course", command = updateui.retrieveID)
deleteButton = tk.Button(text = "Delete Course", command = deleteui.deleteClick)
text = tk.Text(width = 25, height = 10)
text.config(state = "disabled")

# R in CRUD when windows gets focus
createButton.pack()
updateButton.pack()
deleteButton.pack()
text.pack()
window.bind("<FocusIn>",lambda event:refreshList(cs,text))

window.mainloop()