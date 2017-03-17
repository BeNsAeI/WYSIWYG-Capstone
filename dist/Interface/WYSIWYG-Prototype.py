import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from Blocks import Block

#Builder.load_file('cl_button.kv')
#Builder.load_file('class_Block.kv')
Builder.load_file('Scene.kv')
Builder.load_file('BuildSpace.kv')
Builder.load_file('ProgramBuilderSuite.kv')
Builder.load_file('DocumentOptions.kv')
#Builder.load_file('BlockMenu.kv')
class Scatterer(Scatter):
    pass

class Scene(ScatterLayout):
    pass

class cl_button(ToggleButton):
    pass

class method_button(ToggleButton):
    pass

class class_Block(Widget):
    pass

class method_Block(Widget):
    pass

class variable_Block(Widget):
    def varButton(self, type):
        print("TEST")
    
class output_Block(Widget):
    pass

class BuildSpace(FloatLayout):
    def __init__(self,**kwargs):
        super(BuildSpace,self).__init__(**kwargs);
        self.methodCount=0;
        self.classCount=0;
        self.variableCount=0;
        self.outputCount = 0;
        self.blocks = [];
    def addBlock(self, type):
        print(type)
        s = Scatterer()
        if type == "class":
            d = class_Block()
            self.blocks.append(Block(type+str(self.classCount),type,"Add Caption",0,0,0,0,0))
            self.classCount+=1;
        elif type == "method":
            d = method_Block()
            self.blocks.append(Block(type+str(self.methodCount),type,"Add Caption",0,0,0,0,0))
            self.methodCount+=1;
        elif type == "variable":
            d = variable_Block()
            self.blocks.append(Block(type+str(self.variableCount),type,"Add Caption",0,0,0,0,0))
            self.variableCount+=1;
        elif type == "output":
            d = output_Block()
            self.blocks.append(Block(type+str(self.outputCount),type,"Add Caption",0,0,0,0,0))
            self.outputCount+=1;
        else:
            print("Error with request")
        print("Status:");
        for i in self.blocks:
            print(i.Name)
        print("___")
        self.add_widget(s)
        s.add_widget(d)
        print("button is pressed")

class BuilderSuite(BoxLayout):
    pass

class DocumentOptions(BoxLayout):
    pass

class SampGridLayout(GridLayout):
    pass

class WYSIWYGApp(App):
    def build(self):
        return SampGridLayout()

if __name__=="__main__":
    sample_app = WYSIWYGApp()
    sample_app.run()
