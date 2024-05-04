from kivy.app import App
from kivy.uix.label import Label
class MyApp(App):
    def build(self):
        a=Label(text="hello")
        return a
if __name__ == '__main__':
    MyApp().run()