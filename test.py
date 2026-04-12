class mainpage(tk.Frame):
    def __init__(self,gui_manager,manager):
        super().__init__(gui_manager)
        self.manager=manager # This is your Manager
        
        tk.Label(self,text="Player Stats",font=("Arial",18)).pack()
        tk.Button(self,text="Back to Menu",command=lambda: controller.show_screen("Menu")).pack()