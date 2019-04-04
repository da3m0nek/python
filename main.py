

import module
class Menu:

    def __init__(self):
        self.notebook=module.Notebook()
        self.options = {"1": self.show_notes, "2": self.search_notes, "3": self.add_note,"4": self.modify_note, "5": self.quit}

    def show_menu(self):
        print("""
                1. show notes
                2. search notes
                3. add note
                4. modify note
                5. quit""")


    def run(self):
        x=input("choose an option: ")

        if x in self.options:
            option= self.options[x]
            option()
        else:
            print("wrong input")

    def show_notes(self, str= ""):
        if str =="":
            self.notebook.getNotes()
        else:
            x=self.notebook.search(str)
            for z in x:
                print(z)

    def search_notes(self):
        looking_for=input("what are you looking for?: ")
        self.show_notes(looking_for)


    def add_note(self):
        text=input("text: ")
        tag=input("tag: ")
        self.notebook.new_note(text,tag)

    def modify_note(self):
        choice=input("what do u want to edit? Type text or tag: ")
        number=input("number of note: ")

        if choice =="text":
            self.notebook.modify_text(number)
        elif choice =="tag":
            self.notebook.modify_tag(number)
        else:
            print("wrong!")

    def quit(self):
        exit()


object = Menu()

while True:
    object.show_menu()
    object.run()