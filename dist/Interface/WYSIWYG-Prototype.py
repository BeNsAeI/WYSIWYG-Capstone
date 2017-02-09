import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file('DocumentOptions.kv')
Builder.load_file('BlockMenu.kv')

class SampGridLayout(GridLayout):
    pass

class WYSIWYGApp(App):

    def build(self):
        return SampGridLayout()

sample_app = WYSIWYGApp()
sample_app.run()
