from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import psycopg2

class AdminWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


    conn=psycopg2.connect(
        host="localhost",
        database="swat_cash_and_carry",
        user="postgres",
        password="root"
    )


    conn.close()
class AdminApp(App):
    def build(self):
        return AdminWindow()
    

if __name__ == "__main__":
    ao=AdminApp()
    ao.run()