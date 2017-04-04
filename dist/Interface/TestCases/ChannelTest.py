import kivy
kivy.require("1.9.0")

#import Block Class object
from Blocks import Block

#import Kivy modules
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout

class Scatterer(Scatter):
    pass

class block_Class(Widget):
    #def __init__(self, **kwargs):
        #Block("test", "class", "testing block", 001, 20, 10, 0, 0)
    pass

class myLayout(FloatLayout):
    def __init__(self, **kwargs):
        self.i = 0;
        super(myLayout, self).__init__(**kwargs);
        self.methodCount = 0;
        self.classCount = 0;
        self.variableCount = 0;
        self.outputCount = 0;
        self.previous_X = 0;
        self.current_X = 0;
        self.previous_Y = 0;
        self.current_Y = 0;
        self.blocks = [];
    def addfunction(self, *args):
        root = myLayout()

        s = Scatterer()
        d = block_Class()

        self.add_widget(s)
        s.add_widget(d)
        print("button is pressed")
        self.blocks.append(s)
        self.i += 1

    def addLine(self, *args):
        root = myLayout()
        if len(self.blocks) <= 1:
            print(self.blocks[self.i-1].x)
        else:
            self.previous_X = self.blocks[self.i-1].x;
            self.current_X = self.blocks[1].x;
            self.previous_Y = self.blocks[self.i-1].y;
            self.current_Y = self.blocks[1].y;
            with self.canvas:
                #Line(points=[self.blocks[self.i - 1].x, self.blocks[self.i - 1].y, self.blocks[self.i].x, self.blocks[self.i].y], width=10)
                Line(points=[self.previous_X, self.previous_Y, self.current_X, self.current_Y], width=10)





class LineTestApp(App):
    def build(self):
        mL = myLayout()
        return mL

if __name__=="__main__":
    LineTestApp().run()