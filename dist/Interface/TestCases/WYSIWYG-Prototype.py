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
from kivy.lang import Builder

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
    pass
class output_Block(Widget):
    pass

class BuildSpace(FloatLayout):
    def addBlock(self, type):
        print(type)
        s = Scatterer()
        if type == "class":
            d = class_Block()
        elif type == "method":
            d = method_Block()
        elif type == "variable":
            d = variable_Block()
        elif type == "output":
            d = output_Block()
        else:
            print("Error with request")

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
