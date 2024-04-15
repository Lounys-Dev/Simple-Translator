import os
import customtkinter as ctk
from PIL import Image
from deep_translator import GoogleTranslator

import settings
import utils

os.chdir(
    os.path.dirname(os.path.abspath(__file__))
)  # To be able to run the app from any folder


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Translator")
        self.geometry("800x500")

        self.columnconfigure((0, 2), weight=3)
        self.columnconfigure((1), weight=1)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=4)
        self.rowconfigure(3, weight=1)

        ctk.CTkLabel(self, text="Translator", font=("Roboto bold", 36)).grid(
            row=0, column=0, columnspan=3, padx=10, pady=10, sticky="news"
        )

        self.opt_menu_source_language = ctk.CTkOptionMenu(
            self,
            values=("Auto detection",) + settings.SUPPORTED_LANGUAGES,
            command=self.when_opt_menu_is_modified,
            fg_color=(settings.PRIMARY_COLOR, settings.SECONDARY_COLOR),
            button_color=settings.SECONDARY_COLOR,
            button_hover_color=settings.SECONDARY_COLOR,
        )
        self.opt_menu_source_language.grid(
            row=1, column=0, padx=10, ipady=1, sticky="ew"
        )

        self.opt_menu_target_language = ctk.CTkOptionMenu(
            self,
            values=settings.SUPPORTED_LANGUAGES,
            fg_color=(settings.PRIMARY_COLOR, settings.SECONDARY_COLOR),
            button_color=settings.SECONDARY_COLOR,
            button_hover_color=settings.SECONDARY_COLOR,
        )
        self.opt_menu_target_language.grid(
            row=1, column=2, padx=10, ipady=1, sticky="ew"
        )

        self.text_box_source_language = ctk.CTkTextbox(
            self,
            border_color=(settings.PRIMARY_COLOR, settings.SECONDARY_COLOR),
            border_width=3,
        )
        self.text_box_source_language.grid(
            row=2, column=0, padx=10, pady=10, sticky="news"
        )

        self.text_box_target_language = ctk.CTkTextbox(
            self, border_color=(settings.PRIMARY_COLOR, settings.SECONDARY_COLOR), border_width=3, state="disabled"
        )
        self.text_box_target_language.grid(
            row=2, column=2, padx=10, pady=10, sticky="news"
        )

        self.exchange_button = utils.InvisibleButton(
            self,
            Image.open("./assets/arrows left right.png"),
            lambda _: self.exchange(),
        )
        self.exchange_button.grid(row=1, column=1, padx=10, sticky="news")

        ctk.CTkButton(
            self,
            text="Translate",
            command=self.translate,
            font=("Roboto", 24),
            fg_color=(settings.PRIMARY_COLOR, settings.SECONDARY_COLOR),
        ).grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="news")

    def when_opt_menu_is_modified(self, new_value):
        self.exchange_button.disable() if new_value == "Auto detection" else self.exchange_button.enable()

    def translate(self):
        source_language = self.opt_menu_source_language.get()
        source_language = (
            "auto" if source_language == "Auto detection" else source_language.lower()
        )

        target_language = self.opt_menu_target_language.get().lower()

        source_text = self.text_box_source_language.get("1.0", "end-1c")
        if source_text == "":
            return

        translated_text = GoogleTranslator(
            source=source_language, target=target_language
        ).translate(source_text)

        self.text_box_target_language.configure(state="normal")
        self.text_box_target_language.delete("1.0", "end-1c")
        self.text_box_target_language.insert("1.0", translated_text)

    def exchange(self):
        source_language = self.opt_menu_source_language.get()
        target_language = self.opt_menu_target_language.get()

        self.opt_menu_source_language.set(target_language)
        self.opt_menu_target_language.set(source_language)


if __name__ == "__main__":
    app = App()
    app.mainloop()
