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
sys.path.append('../Core')
from Table import ParsingTable
from Parser import Tree
from Parser import Parser
from Generator import Generator
sys.path.append('../Debugger')
from errorHandler import errorHandler

# Included Builds:
Builder.load_file('Scene.kv')
Builder.load_file('BuildSpace.kv')
#Builder.load_file('ProgramBuilderSuite.kv')
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
        self.parserTable = ParsingTable();

    def set_source(self, sourceBlk):
        self.channelStack.append(Channel());
        self.channelCount += 1;
        self.channelStack[len(channelStack)-1].changeSourceID(sourceBlk);

    def set_destination(self, destBlk):
        self.channelStack[len(channelStack)-1].changeDestinationID(destBlk);

    def updateList(self):
        self.parsingTable.addChannel(self.channelStack)



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
blocks = []
class BuildSpace(FloatLayout):
    def __init__(self, **kwargs):
        super(BuildSpace, self).__init__(**kwargs);
        self.methodCount = 0;
        self.classCount = 0;
        self.variableCount = 0;
        self.outputCount = 0;
        self.widgetStack = [];
        self.channelStack = ChannelStack();
        self.channelHolder = [];

    def addBlock(self, type):
        stringLabel = " "
        print(type)
        if type == "class":
            d = class_Block()
            blocks.append(Block(type+str(self.classCount),type,"Add Caption",0,0,0,0,0))
            self.classCount+=1;
        elif type == "method":
            d = method_Block()
            blocks.append(Block(type+str(self.methodCount),type,"Add Caption",0,0,0,0,0))
            self.methodCount+=1;
        elif type == "variable":
            d = variable_Block()
            blocks.append(Block(type+str(self.variableCount),type,"Add Caption",0,0,0,0,0))
            self.variableCount+=1;
        elif type == "output":
            d = output_Block()
            blocks.append(Block(type+str(self.outputCount),type,"Add Caption",0,0,0,0,0))
            self.outputCount+=1;
        else:
            print("Error with request")
            pass
        #print("Status:");
        #for i in blocks:
            #print(i.Name)
        #print("___")
        s = Scatterer()
        self.add_widget(s)
        s.set_name(blocks[len(blocks)-1])
        d.add_widget(Label(text=str(blocks[len(blocks)-1].Name)))
        s.add_widget(d)
        self.widgetStack.append(s)

        for i in self.widgetStack:
            print("button is pressed " + "ScatterLabel:" + i.name.Name + "Scatter type: " + i.name.Type)

    def ChannelDraw(self, block):
        self.channelHolder.append(block);
        if len(channelHolder) == 2:
            self.channelStack.set_source(channelHolder[0].name)
            self.channelStack.set_destination(channelHolder[1].name)
            self.channelHolder.pop();
            self.channelHolder.pop();
            self.channelStack.updateList()

    def getBlock(self, widget):
        for i in self.widgetStack:
            if i.name.Name == widget.name.Name:
                self.ChannelDraw(i.name)

class BuilderSuite(BoxLayout):
	def __init__(self, **kwargs):
		super(BuilderSuite, self).__init__(**kwargs);
		print("POTATO!")
	def extract(self):
		print("EXTRACT: Status:");
		temp = Generator()
		II = 0
		for i in blocks:
			print(i.Name+", "+i.Type+", "+i.Caption+", "+str(i.ID)+".")
			comment = "Code for "+i.Name+" block; "+i.Caption+":"
			if(i.Type == "variable"):
				genType = "var"
				arg1 = "var"+str(i.ID)
				arg2 = '"Hello World!"'#i.Value
				args=[comment,arg1,arg2]
			if(i.Type == "method"):
				pass
			if(i.Type == "class"):
				pass
			if(i.Type == "output"):
				genType="print"
				arg1 = "var0"#i.Value
				args=[comment,arg1]
			temp.addBlock(genType,II,args)
		print(temp.spaghetti)
		temp.release()
		myHandler=errorHandler("Output.py")
		myHandler.Monitor()
		myHandler.makeReport()
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
