import tkinter as tk #tkinter is one of pythons standerd librarby for gui

class gui_manager:
    def __init__(self,root=tk.Tk(),title="untitled widget",background="white",start_size=(500,500),min_size=(250,250),max_size=(1000,1000)):
        self.root=root
        self.root.title(title)
        self.root.configure(background=background)
        self.root.geometry(f"{start_size[0]}x{start_size[1]}")
        self.root.minsize(*min_size)
        self.root.maxsize(*max_size)
        self.buttons={}
        self.texts=[]
        self.images=[]
    def __bool__(self):
        return self.root.winfo_exists()
    def add_button(self,name,x,y,text,width=100, height=30,command=None):
        button = tk.Button(self.root,text=text,command=command)
        button.place(x=x,y=y,width=width,height=height)
        self.buttons[name]=button
        return button
    def activate_deactivate_button(self,name,active=True):
        state="normal" if active else "disabled"
        self.buttons[name].config(state=state)
    def remove_button(self, name):
        if name in self.buttons:
            self.buttons[name].destroy()
            del self.buttons[name]
    def get_buttons(self):
        return self.buttons
    def add_text(self, text, x, y, font=("Arial", 12)):
        label=tk.Label(self.root,text=text,font=font,bg=self.root["bg"])
        label.place(x=x,y=y)
        self.texts.append(label)
        return label
    def remove_text(self,label):
        label.destroy()
        if label in self.texts:
            self.texts.remove(label)
    def get_texts(self):
        return self.texts
    def add_image(self,file_path,x,y):
        image=tk.PhotoImage(file=file_path)
        lbl=tk.Label(self.root,image=image,bg=self.root["bg"])
        lbl.image=image # Keep a reference so garbage collection doesn't delete it
        lbl.place(x=x,y=y)
        self.images.append(lbl)
        return lbl
    def remove_image(self,image_label):
        image_label.destroy()
        if image_label in self.images:
            self.images.remove(image_label)
    def get_images(self):
        return self.images
    def add_input(self,name,x,y,width=150,show=None):
        # show="*" will hide text for passwords
        entry = tk.Entry(self.root,show=show)
        entry.place(x=x,y=y,width=width)
        if not hasattr(self,"inputs"):
            self.inputs={}
        self.inputs[name]=entry
        return entry
    def get_input_text(self,name):
        if name in self.inputs:
            return self.inputs[name].get()
        return ""
    def clear_input(self,name):
        if name in self.inputs:
            self.inputs[name].delete(0,tk.END)
    def pack(self,names=[]):
        all_widgets={**self.buttons,**(getattr(self,"inputs",{}))}
        for name,widget in all_widgets.items():
            if name in names:
                widget.pack_forget() 
                continue
            widget.pack()


