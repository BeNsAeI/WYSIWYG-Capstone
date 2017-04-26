#########INFO#########
#   Project Name :   #
#  WYSIWYG Project   #
#--------------------#
# Class instructors: #
#   Kevin Mcgrath    #
#   Kirsten Winters  #
#--------------------#
#      Authors :     #
#   Behnam  Saeedi   #
#   Conner Sedwick   #
#   Collin Dorsett   #
#--------------------#
#  Project Manager : #
#     John Dodge     #
#--------------------#
#       Client :     #
# Professor Fuxin Li #
######################


# imaports:
import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
import sys
sys.path.append('../Blocks')
from Blocks import Block
from Channels import Channel

# Included Builds:
Builder.load_file('Scene.kv')
Builder.load_file('BuildSpace.kv')
Builder.load_file('ProgramBuilderSuite.kv')
Builder.load_file('DocumentOptions.kv')

#Class Deffinitions:

#######################CLASS########################
# Name: Channel Stack                              #
# Purpose: Store the list of channels              #
# Inputs: Channel objects                          #
# Outputs: List                                    #
# Private Variables: channelCount , channelStack   #
# Public Methods: set_source , set_destination     #
# Status: Edit tentetive                           #
####################################################
class ChannelStack():
    def __init__(self):
        self.channelCount = 0;
        self.channelStack = [];

    def set_source(self):
        self.channelStack.append(Channel())

    def set_destination(self):
        pass


#######################CLASS########################
# Name: Scatter                                    #
# Purpose: Dragable objects                        #
# Inputs: Scatter                                  #
# Outputs: Visual outputs                          #
# Private Variables: NA                            #
# Public Methods: NA                               #
# Status: FINISHED                                 #
####################################################

class Scatterer(Scatter):
    def __init__(self, **kwargs):
        super(Scatterer, self).__init__(**kwargs);
        self.name = Block;

    def set_name(self, newName):
        self.name = newName;


#######################CLASS########################
# Name: Scene, cl-button, method_button,           #
#       class_block, method_block,variable_block,  #
#       Output_block                               #
# Purpose: Offer the dragable space                #
# Inputs: NA                                       #
# Outputs: Visual Output                           #
# Private Variables: NA                            #
# Public Methods: NA                               #
# Status: FINISHED                                 #
####################################################
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


#######################CLASS########################
# Name: Build Space                                #
# Purpose: Provides the GUI environment            #
# Inputs: NA                                       #
# Outputs: NA                                      #
# Private Variables: NA                            #
# Public Methods: NA                               #
# Status: Edit tentetive                           #
####################################################
class BuildSpace(FloatLayout):
    def __init__(self, **kwargs):
        super(BuildSpace, self).__init__(**kwargs);
        self.methodCount = 0;
        self.classCount = 0;
        self.variableCount = 0;
        self.outputCount = 0;
        self.blocks = [];
        self.widgetStack = [];
        self.channelStack = ChannelStack();
        self.channelHolder = [];

    def addBlock(self, type):
        stringLabel = " "
        print(type)
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
        s = Scatterer()
        self.add_widget(s)
        s.set_name(self.blocks[len(self.blocks)-1])
        d.add_widget(Label(text=str(self.blocks[len(self.blocks)-1].Name)))
        s.add_widget(d)
        self.widgetStack.append(s)

        for i in self.widgetStack:
            print("button is pressed " + "ScatterLabel:" + i.name.Name + "Scatter type: " + i.name.Type)
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
