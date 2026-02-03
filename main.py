from kivy.app import App
from kivy.uix.label import Label

class CoreElite(App):
    def build(self):
        return Label(text='CORE ELITE SYSTEM ONLINE', font_size='30sp')

if __name__ == '__main__':
    CoreElite().run()
