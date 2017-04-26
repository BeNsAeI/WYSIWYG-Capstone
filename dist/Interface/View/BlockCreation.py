import kivy
kivy.require("1.9.0")

#import Block Class object
from Blocks import Block

#import Kivy modules
from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout

class Scatterer(Scatter):
    pass

class block_Class(Widget):
    #def __init__(self, **kwargs):
        #Block("test", "class", "testing block", 001, 20, 10, 0, 0)
    pass

class myLayout(FloatLayout):
    def addfunction(self, *args):
        root = myLayout()

        s = Scatterer()
        d = block_Class()

        self.add_widget(s)
        s.add_widget(d)
        print("button is pressed")



class MyTestApp(App):
    def build(self):
        mL = myLayout()
        return mL

if __name__=="__main__":
    MyTestApp().run()