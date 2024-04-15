import customtkinter as ctk
from PIL import Image

class InvisibleButton(ctk.CTkLabel):
    def __init__(self, master, picto, command):
        super().__init__(master, text="", fg_color="transparent", image=ctk.CTkImage(picto), width=0, height=0)
        self.bind("<Button-1>", command)
        self.picto = picto
        self.command = command

    def disable(self):
        self.configure(state="disabled")
        self.unbind("<Button-1>")

        # Transform the picto into a light gray
        light_gray_picto = self.picto.convert('LA')
        light_gray_picto = light_gray_picto.point(lambda x: min(x + 100, 255))  # Ajoute une luminosité
        self.configure(image=ctk.CTkImage(light_gray_picto))



    def enable(self):
        self.configure(state="normal")
        self.bind("<Button-1>", self.command)
        self.configure(image=ctk.CTkImage(self.picto))