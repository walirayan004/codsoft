from tkinter import *
from tkinter import ttk
class todo:
    def __init__(self,root):
        self.root=root
        self.root.title("TO DO LIST")
        self.root.geometry("650x410+300+150")

        self.label1=Label(self.root,text="TO-DO-LIST",font=("ariel",25,"bold"), width=10,bd=5,bg="red",fg="black")
        self.label1.pack(side="top",fill=BOTH)


        self.label2=Label(self.root,text="ADD TASK",font=("ariel",18,"bold"), width=10,bd=5,bg="red",fg="black")
        self.label2.place(x=40,y=55)

        self.label3=Label(self.root,text="TASKS",font=("ariel",18,"bold",), width=10,bd=5,bg="red",fg="black")
        self.label3.place(x=340,y=55)

        self.main_text = Listbox(self.root,height=10,width=23,bd=5,font=("ariel",18,"italic bold") ) 
        self.main_text.place(x=280,y=100)
        

        self.text=Text(self.root,bd=5,height=1,width=15,font=("ariel",18,"italic bold") )
        self.text.place(x=20,y=120)


        def add():
            content=self.text.get(1.0,END)
            self.main_text.insert(END,content)
            with open("data.txt","a") as  file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0,END)    

        def delete():
         delete_ = self.main_text.curselection()
         if delete_:  # check if something is selected
            look = self.main_text.get(delete_)
            with open("data.txt", "r") as f:
             lines = f.readlines()
            with open("data.txt", "w") as f:
             self.main_text.delete(delete_)  

        with open("data.txt","r") as file:
            read=file.readlines()
            for i in read:
                ready=i.split()
                self.main_text.insert(END,ready)   
            file.close()

        self.button1=Button(self.root,text="ADD",font=("ariel",18,"italic bold"),width=10,bd=5,bg="steelblue2",fg="black",command=add)    

        self.button1.place(x=30,y=180)

        self.button2=Button(self.root,text="DELETE",font=("ariel",18,"italic bold"),width=10,bd=5,bg="red",fg="black",command=delete)              
        self.button2.place(x=30,y=280)
def main():
    root=Tk()
    obj=todo(root)
    root.mainloop()        
if __name__ =="__main__":
    main()