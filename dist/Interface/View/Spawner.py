from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class Scatterer(Scatter):
    pass
class Drawer(Widget):
    pass
class MainWindowWidget(FloatLayout):
    def addfunction(self, *args):
        root = MainWindowWidget()

        s = Scatterer()
        d = Drawer()

        self.add_widget(s)
        s.add_widget(d)
        print("button is pressed")

class RegularApp(App):
    def build(self):

        return MainWindowWidget()

if __name__ == '__main__':
    RegularApp().run()