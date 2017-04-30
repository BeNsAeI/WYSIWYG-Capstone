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
from kivy.config import Config
Config.set("input", "mouse", "mouse, disable_multitouch")

from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics.vertex_instructions import Line
from kivy.properties import ObjectProperty
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
import os, sys
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
#Builder.load_file('BuildSpace.kv')
#Builder.load_file('ProgramBuilderSuite.kv')
Builder.load_file('DocumentOptions.kv')

parsingTable = ParsingTable();
blocks = []
channelHolder = [];
scatterStack = [];
widgetStack = [];
channelStack = [];
channelCount = 0;
widgetCount = 0;
scatterCount = 0;

def createDirectory():
    directory = os.getcwd();
    directory = directory + '../MyFolder'
    if not os.path.exists(directory):
        os.makedirs(directory)

#Class Definitions:

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

    def create_Channel(self, sourceBlk, destinationBlk):
        self.channelCount += 1;
        self.channelStack.append(Channel(self.channelCount, sourceBlk, destinationBlk));
        #self.channelStack[len(channelStack)-1].changeSourceID(sourceBlk);


    def updateList(self):
        self.parsingTable.addChannel(self.channelStack)


def ChannelDraw(scatter, build):
    if len(channelHolder) == 2:
        channelHolder.pop();
        channelHolder.pop();
    channelHolder.append(scatter);
    if len(channelHolder) == 2:
        channelStack.append(Channel(channelCount, channelHolder[0].name, channelHolder[1].name))
        previous_X = channelHolder[0].center_x;
        current_X = channelHolder[1].center_x;
        previous_Y = channelHolder[0].center_y;
        current_Y = channelHolder[1].center_y;
        with build.canvas:
            # Line(points=[self.blocks[self.i - 1].x, self.blocks[self.i - 1].y, self.blocks[self.i].x, self.blocks[self.i].y], width=10)
            Line(points=(previous_X, previous_Y, current_X, current_Y), width=3)

        parsingTable.addChannel(channelStack)
        parsingTable.printTable()


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

    def get_name(self):
        return self.name;

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
    def __init__(self, buildSpc,**kwargs):
        super(class_Block, self).__init__(**kwargs);
        self.name = Block;
        self.build = buildSpc;
    def set_name(self, newName):
        self.name = newName;

    def channel_dr(self):
        for i in scatterStack:
            if i.name.Name == self.name.Name:
                ChannelDraw(i, self.build)

class method_Block(Widget):
    def __init__(self, buildSpc,**kwargs):
        super(method_Block, self).__init__(**kwargs);
        self.name = Block;
        self.build = buildSpc;
    def set_name(self, newName):
        self.name = newName;

    def channel_dr(self):
        for i in scatterStack:
            if i.name.Name == self.name.Name:
                ChannelDraw(i, self.build)

class variable_Block(Widget):
    def __init__(self, buildSpc,**kwargs):
        super(variable_Block, self).__init__(**kwargs);
        self.name = Block;
        self.build = buildSpc;
    def set_name(self, newName):
        self.name = newName;

    def channel_dr(self):
        for i in scatterStack:
            if i.name.Name == self.name.Name:
                ChannelDraw(i, self.build)
    
class output_Block(Widget):
    def __init__(self, buildSpc,**kwargs):
        super(output_Block, self).__init__(**kwargs);
        self.name = Block;
        self.build = buildSpc;
    def set_name(self, newName):
        self.name = newName;

    def channel_dr(self):
        for i in scatterStack:
            if i.name.Name == self.name.Name:
                ChannelDraw(i, self.build)

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
        self.directory = os.getcwd();
        self.directory = self.directory + '/../../MyProjectFolder'
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def addBlock(self, type):
        stringLabel = " "
        print(type)
        if type == "class":
            blocks.append(Block(type+str(self.classCount),type,"Add Caption",0,0,0,0,0))
            self.classCount+=1;
            d = class_Block(self);
            d.set_name(blocks[len(blocks)-1]);
        elif type == "method":
            blocks.append(Block(type+str(self.methodCount),type,"Add Caption",0,0,0,0,0))
            self.methodCount+=1;
            d = method_Block(self);
            d.set_name(blocks[len(blocks)-1]);
        elif type == "variable":
            blocks.append(Block(type+str(self.variableCount),type,"Add Caption",0,0,0,0,0))
            self.variableCount+=1;
            d = variable_Block(self);
            d.set_name(blocks[len(blocks)-1]);
        elif type == "output":
            blocks.append(Block(type+str(self.outputCount),type,"Add Caption",0,0,0,0,0))
            self.outputCount+=1;
            d = output_Block(self);
            d.set_name(blocks[len(blocks)-1]);
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
        scatterStack.append(s)
        widgetStack.append(d)

        for i in scatterStack:
            print("button is pressed " + "ScatterLabel:" + i.name.Name + "Scatter type: " + i.name.Type)

class BuilderSuite(BoxLayout):
	def __init__(self, **kwargs):
		super(BuilderSuite, self).__init__(**kwargs);

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
