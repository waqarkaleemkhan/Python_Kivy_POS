from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SigninWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    def validate_user(self):
        username=self.ids.username_field # here the ids are all the ids that are comming from kivy file like username_field,pwd_field
        password=self.ids.pwd_field
        info=self.ids.info

        uname=username.text
        passw=password.text

        if uname=='' or passw == '':
            info.text='[color=#FF0000]username and password is required[/color]'
        else:
            if uname=='admin' and passw=='admin':
                info.text='[color=#00FF00]Login Succesfully[/color]'
            else:
                info.text='[color=#FF0000]Invalid username or password[/color]'



class SigninApp(App): # for displaying the layout of the application and the .kv file name should be same ass the class like signin.kv
    def build(self) : # the build function the build in function of App which we are overriding here and returning the signinwindow 
        return SigninWindow()



if __name__ == "__main__":
    sa = SigninApp() # sa is the object of SiginApp
    sa.run() # run is the buildin function of App which will run the window