from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKM(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        Window.size = (400, 200)
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_increment(self, increment):
        try:
            if not self.root.ids.input_number.text:
                new_value = 0 + increment
                self.root.ids.input_number.text = str(new_value)
            else:
                new_value = int(self.root.ids.input_number.text) + increment
                self.root.ids.input_number.text = str(new_value)
        except ValueError:
            new_value = 0 + increment
            self.root.ids.input_number.text = str(new_value)

    def handle_miles_to_km(self):
        try:
            miles = int(self.root.ids.input_number.text) * 1.60934
            self.root.ids.output_label.text = str(miles)
        except ValueError:
            self.root.ids.output_label.text = "0.0"


MilesToKM().run()
