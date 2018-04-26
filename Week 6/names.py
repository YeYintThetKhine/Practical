from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label

class ListNames(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"Bob Brown", "Cat Cyan", "Oren Ochre", "Benjamin Stanley"}

    def build(self):
        self.title = "Names Lister"
        self.root = Builder.load_file('names.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            # temp_button.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_label)



ListNames().run()
