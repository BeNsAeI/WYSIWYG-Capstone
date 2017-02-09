import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file('cl_button.kv')
Builder.load_file('class_Block.kv')
Builder.load_file('Scene.kv')
Builder.load_file('BuildSpace.kv')
Builder.load_file('ProgramBuilderSuite.kv')
Builder.load_file('DocumentOptions.kv')
Builder.load_file('BlockMenu.kv')

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

class BuildSpace(BoxLayout):
    scene = ObjectProperty(None)
    menu = ObjectProperty(None)
    pass

class Scene(BoxLayout):
    pass

class BuilderSuite(BoxLayout):
    pass

class DocumentOptions(BoxLayout):
    pass

class BlockMenu(BoxLayout):
    pass

class SampGridLayout(GridLayout):
    pass

class WYSIWYGApp(App):

    def build(self):
        return SampGridLayout()

sample_app = WYSIWYGApp()
sample_app.run()
