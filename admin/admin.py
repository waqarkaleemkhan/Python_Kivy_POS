from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class AdminWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
class AdminApp(App):
    def build(self):
        return AdminWindow()
    

if __name__ == "__main__":
    ao=AdminApp()
    ao.run()