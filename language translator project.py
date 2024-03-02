from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from tkinter import messagebox  # Added import for messagebox

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.setup_gui()

    def setup_gui(self):
        self.root.geometry('1080x400')
        self.root.resizable(0, 0)
        self.root.config(bg='ghost white')
        self.root.title("Language Translator")

        Label(self.root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='white smoke').pack()

        Label(self.root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=200, y=60)

        self.input_text = Text(self.root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
        self.input_text.place(x=30, y=100)

        Label(self.root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=60)

        self.output_text = Text(self.root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
        self.output_text.place(x=600, y=100)

        language = list(LANGUAGES.values())

        self.src_lang = ttk.Combobox(self.root, values=language, width=22)
        self.src_lang.place(x=20, y=60)
        self.src_lang.set('choose input language')

        self.dest_lang = ttk.Combobox(self.root, values=language, width=22)
        self.dest_lang.place(x=890, y=60)
        self.dest_lang.set('choose output language')

        trans_btn = Button(self.root, text='Translate', font='arial 12 bold', pady=5, command=self.translate,
                           bg='royal blue1', activebackground='sky blue')
        trans_btn.place(x=490, y=180)

    def translate(self):
        translator = Translator()
        try:
            translated = translator.translate(text=self.input_text.get(1.0, END), src=self.src_lang.get(),
                                              dest=self.dest_lang.get())
            self.output_text.delete(1.0, END)
            self.output_text.insert(END, translated.text)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()
