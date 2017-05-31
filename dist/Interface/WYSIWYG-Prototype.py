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
import os
os.environ['KIVY_TEXT'] = 'sdl2'
os.environ['KIVY_WINDOW'] = 'sdl2'
os.environ['KIVY_IMAGE'] = 'sdl2'

import kivy
kivy.require("1.9.0")
from kivy.config import Config
Config.set("input", "mouse", "mouse, disable_multitouch")

from kivy.uix.scrollview import ScrollView
from kivy.event import EventDispatcher
from kivy.properties import StringProperty
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
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock
from functools import partial
#from projectPath import projectPath
import os, sys
sys.path.append('../Blocks')
from Blocks import Block
from Probe import Probe
from Channels import Channel
from Channels import FindSrc
from Channels import FindDst
sys.path.append('../Core')
from Table import ParsingTable
from Parser import Tree
from Parser import Parser
from Generator import Generator
sys.path.append('../Debugger')
from errorHandler import errorHandler
sys.path.append('../Core')
from projectPath import projectPath

# Included Builds:
Builder.load_file('Scene.kv')
#Builder.load_file('BuildSpace.kv')
#Builder.load_file('ProgramBuilderSuite.kv')
Builder.load_file('DocumentOptions.kv')


def getArgNum(type):
    from TemplateHandler import fileIO
    input = fileIO("python")
    src = input.read_fil(type)
    print("*** getArgNum -> "+type+"\n"+src)
    h = 0
    for i in range(0,50):
        mystr = "<<ARG"+str(i)+">>"
        if mystr in src:
            h = i
            print(mystr)
    return h

buildSpaceRef = None
parsingTable = ParsingTable();
lineStack = [];
blocks = [];
channelHolder = [];
scatterStack = [];
widgetStack = [];
channelStack = [];
channelCount = 0;
widgetCount = 0;
scatterCount = 0;
debugText="Debugger View"
PATH = "Output.py"
layerCount = 0

def createDirectory():
    directory = os.getcwd();
    directory = directory + '../MyFolder'
    if not os.path.exists(directory):
        os.makedirs(directory)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False
#Class Definitions:

class LineData():
    def __init__(self, scatter1, scatter2):
        self.scatt1 = scatter1;
        self.scatt2 = scatter2;

#######################CLASS########################
# Name: Channel Stack                              #
# Purpose: Store the list of channels              #
# Inputs: Channel objects                          #
# Outputs: List                                    #
# Private Variables: channelCount , channelStack   #
# Public Methods: set_source , set_destination     #
# Status: Edit tentetive                           #
####################################################
def ChannelInDraw(scatter, build, argn=None):
    if len(channelHolder) == 2:
        channelHolder.pop();
        channelHolder.pop();
    channelHolder.append(scatter);
    if len(channelHolder) == 2:
        channelStack.append(Channel(channelCount, channelHolder[0].name, channelHolder[1].name, argN=argn))
        for x in scatterStack:
            if x.name == channelHolder[0].name:
                for i in scatterStack:
                    if i.name == channelHolder[1].name:
                        lineStack.append(LineData(x, i));

        with build.canvas:
            Line(points=(lineStack[len(lineStack)-1].scatt1.center_x, lineStack[len(lineStack)-1].scatt1.center_y,
                         lineStack[len(lineStack)-1].scatt2.center_x, lineStack[len(lineStack)-1].scatt2.center_y), width=3)

        if len(channelStack) > 1:
            for x in channelStack:
                if x == channelStack[len(channelStack)-1]:
                    break
                if x == channelStack[len(channelStack)-1]:
                    channelStack.pop()

        parsingTable.addChannel(channelStack)
        parsingTable.printTable()
        for i in channelStack:
            print("Source:" + i.SourceID.Name + ", Destination:" + i.DestinationID.Name)

def ChannelOutDraw(scatter, build):
    if len(channelHolder) == 2:
        channelHolder.pop();
        channelHolder.pop();
    channelHolder.append(scatter);
    if len(channelHolder) == 2:
        channelStack.append(Channel(channelCount, channelHolder[1].name, channelHolder[0].name))
        for x in scatterStack:
            if x.name == channelHolder[0].name:
                for i in scatterStack:
                    if i.name == channelHolder[1].name:
                        lineStack.append(LineData(x, i));

        with build.canvas:
            Line(points=(lineStack[len(lineStack) - 1].scatt1.center_x, lineStack[len(lineStack) - 1].scatt1.center_y,
                         lineStack[len(lineStack) - 1].scatt2.center_x, lineStack[len(lineStack) - 1].scatt2.center_y),
                 width=3)

        if len(channelStack) > 1:
            for x in channelStack:
                if x == channelStack[len(channelStack)-1]:
                    break
                if x == channelStack[len(channelStack)-1]:
                    channelStack.pop()

        parsingTable.addChannel(channelStack)
        parsingTable.printTable()
        for i in channelStack:
            print("Source:" + i.SourceID.Name + ", Destination:" + i.DestinationID.Name)
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
3
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
class CornerRectangleWidget(Widget):
    #DLW = StringProperty(debugText)
    def __init__(self, **kwargs):
        self.log=debugText
        super(CornerRectangleWidget, self).__init__(**kwargs)
        with self.canvas:
            pass
    #self.bind(DLW=self.update_rect)
        Clock.schedule_interval(self.update_rect,0.1)
        self.myLabel = Label(text="", pos=(self.width+200,0))
        self.add_widget(self.myLabel)

    def update_rect(self, *args):
        self.log = debugText
        self.myLabel.text = self.log
        self.myLabel.size_hint_y = None

class Scene(ScatterLayout):
    pass

class cl_button(ToggleButton):
    pass

class method_button(ToggleButton):
    pass

class LayersDropDown(DropDown):
    def __init__(self, **kwargs):
        super(LayersDropDown, self).__init__(**kwargs);
        self.Layers = []

    def updateLayers(self, layername):
        self.Layers.append(layername)
        self.add_widget(Label(text=layername))


class probe_Block(GridLayout):
    def __init__(self, buildSpc, **kwargs):
        super(probe_Block, self).__init__(**kwargs);
        self.val = None;
        self.build = buildSpc;

    def spawnProbe(self):
        self.add_widget(Label(text='Value:'))
        self.val = Label(text='')
        self.add_widget(self.val)
        self.add_widget(Button(text='Link', on_release=self.probeLink))

    def probeLink(self, rand):
        pass

    def channel_out_dr(self):
        for i in scatterStack:
            if i.name.Name == self.name.Name:
                ChannelOutDraw(i, self.build)

    def channel_in_dr(self):
        for i in scatterStack:
            if i.name.Name == self.name.Name:
                ChannelInDraw(i, self.build)


class class_Block(Widget):
    def __init__(self, buildSpc,**kwargs):
        super(class_Block, self).__init__(**kwargs);
        self.name = Block;
        self.build = buildSpc;

    def set_name(self, newName):
        self.name = newName;

    def channel_out_dr(self):
        for i in scatterStack:
            if i.name.Name == self.name.Name:
                ChannelOutDraw(i, self.build)

    def channel_in_dr(self):
        for i in scatterStack:
            if i.name.Name == self.name.Name:
                ChannelInDraw(i, self.build)

class method_Block(GridLayout):
    def __init__(self, buildSpc,**kwargs):
        super(method_Block, self).__init__(**kwargs);
        self.name = Block;
        self.build = buildSpc;
        self.method = '';
        self.argN = 0;
        self.CID = [];

    def set_name(self, newName):
        self.name = newName;

    def set_method(self, methodType):
        self.method = methodType;
        print(self.method)

    def tailorMethod(self, argn, methodType):
        p = 0;
        if (argn == 4):
            while p < argn:
                p += 1
                self.argN = p
                self.add_widget(Button(text="Arg" + str(p), on_release=partial(self.channel_in_dr, argN=p)));
                self.argN = 0
        if (argn == 3):
            while p < argn:
                p += 1
                self.argN = p
                self.add_widget(Button(text="Arg" + str(p), on_release=partial(self.channel_in_dr, argN=p)));
                self.argN = 0
        elif (argn == 2):
            self.argN = 1
            self.add_widget(Button(text="Arg1", on_release=partial(self.channel_in_dr, argN=1)));
            self.add_widget(Label(text=''))
            self.argN = 2
            self.add_widget(Button(text="Arg2", on_release=partial(self.channel_in_dr, argN=2)));
            self.argN = 0
        elif (argn == 1):
            self.add_widget(Label(text=''))
            self.argN = 1
            self.add_widget(Button(text="Arg1", on_release=partial(self.channel_in_dr, argN=1)));
            self.argN = 0
            self.add_widget(Label(text=''))
        else:
            print("Error with call")
        self.add_widget(Label(text=''))
        self.add_widget(Label(text=str(methodType)))
        self.add_widget(Label(text=''))
        self.add_widget(Label(text=''))
        self.add_widget(Button(text="Output", on_release=self.channel_out_dr))
        if argn != 4:
            self.add_widget(Label(text=''))

    def channel_out_dr(self, rand):
        for i in scatterStack:
            if i.name.Name == self.name.Name:
                ChannelOutDraw(i, self.build)

    def channel_in_dr(self, rand, argN=0):
        for i in scatterStack:
            if i.name.Name == self.name.Name:
                ChannelInDraw(i, self.build, argn=argN)

class variable_Block(Widget):
    def __init__(self, buildSpc,**kwargs):
        super(variable_Block, self).__init__(**kwargs);
        self.name = Block;
        self.build = buildSpc;

    def set_name(self, newName):
        self.name = newName;

    def delete_self(self):
        self.build.remove_widget(self)

    def takeValue(self, text):
        self.name.Value = text;
        print("Value: " + self.name.Value)

    def takeName(self, text):
        self.name.Name = text;
        print("Name: " + self.name.Name)

    def channel_out_dr(self):
        for i in scatterStack:
            if i.name.Name == self.name.Name:
                ChannelOutDraw(i, self.build)

    def channel_in_dr(self):
        for i in scatterStack:
            if i.name.Name == self.name.Name:
                ChannelInDraw(i, self.build)

class output_Block(Widget):
    def __init__(self, buildSpc,**kwargs):
        super(output_Block, self).__init__(**kwargs);
        self.name = Block;
        self.build = buildSpc;

    def set_name(self, newName):
        self.name = newName;

    def channel_in_dr(self):
        for i in scatterStack:
            if i.name.Name == self.name.Name:
                ChannelInDraw(i, self.build)

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
        self.probeCount = 0;
        self.directory = os.getcwd();
        self.directory = self.directory + '/../../MyProjectFolder'
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def addBlock(self, type, argN=0, methodType=None):
        if type == "class":
            blocks.append(Block(type+str(self.classCount),type,"Add Caption",self.classCount,0))
            self.classCount+=1;
            d = class_Block(self);
            d.set_name(blocks[len(blocks)-1]);
        elif type == "method":
            blocks.append(Block(methodType+str(self.methodCount),type,"Add Caption",self.methodCount,0))
            self.methodCount+=1;
            d = method_Block(self);
            d.set_name(blocks[len(blocks)-1]);
        elif type == "variable":
            blocks.append(Block(type+str(self.variableCount),type,"Add Caption",self.variableCount,0))
            self.variableCount+=1;
            d = variable_Block(self);
            d.set_name(blocks[len(blocks)-1]);
        elif type == "output":
            blocks.append(Block(type+str(self.outputCount),type,"Add Caption",self.outputCount,0))
            self.outputCount+=1;
            d = output_Block(self);
            d.set_name(blocks[len(blocks)-1]);
        elif type == "probe":
            blocks.append(Probe())
            self.probeCount += 1;
            d = probe_Block(self);
        else:
            print("Error with request")
            pass

        s = Scatterer()
        self.add_widget(s)
        s.set_name(blocks[len(blocks)-1])
        if type == "method":
            d.tailorMethod(argN, methodType)
        elif type == "probe":
            d.spawnProbe()
        scatterStack.append(s)
        widgetStack.append(d)
        s.add_widget(d)

    def delete_widgets(self):
        print("channelStack: " + str(channelStack))
        print("scatterStack: " + str(scatterStack))
        print("widgetStack: " + str(widgetStack))
        print("blocks: " + str(blocks))
        self.methodCount = 0
        self.variableCount = 0
        self.outputCount = 0
        self.probeCount = 0
        self.classCount = 0
        for i in scatterStack:
            self.remove_widget(i)
        while len(widgetStack) != 0:
            widgetStack.pop()
        while len(scatterStack) != 0:
            scatterStack.pop()
        while len(channelStack) != 0:
            channelStack.pop()
        while len(blocks) != 0:
            blocks.pop()
        print("channelStack: " + str(channelStack))
        print("scatterStack: " + str(scatterStack))
        print("widgetStack: " + str(widgetStack))
        print("blocks: " + str(blocks))


class BuilderSuite(BoxLayout):
    def __init__(self, **kwargs):
        super(BuilderSuite, self).__init__(**kwargs);
        self.projectPath = projectPath()

    def updatePathname(self, text):
        self.projectPath.updatePath(text)
        global PATH
        PATH = self.projectPath.getPath()
        print(self.projectPath.getPath())

    def getCode(self,block,II):
        comment="Inner element"
        temp = Generator()
        if (block.Type == "variable"):
            genType = "var"
            items = FindSrc(channelStack, blocks, block.Name,block.ID)
            arg1 = block.Name
            if (channelStack and items):
                arg2 = str(items[0].Name)
            else:
                arg2 = str(block.Value)
       	    args = [block.Name, arg1, arg2]
        if (block.Type == "method"):
            genType = block.Name
            genType = genType[:-1]
            argNum = getArgNum(genType)
            args = [block.Name]
            if argNum == 1:
                items = FindSrc(channelStack, blocks, block.Name,block.ID)
                args.append(str(items[0].Name))
            if argNum > 1:
                for i in range(1, argNum + 1):
                    items = FindSrc(channelStack, blocks, block.Name,block.ID, argN=i)
                    if len(items) > 0:
                        if ((genType == "while" or genType == "if") and i > 1):
                            args.append(self.getCode(items[0],II+1))
                        elif ((genType == "for") and i > 2):
                            args.append(self.getCode(items[0],II+1))
                        elif (genType == "output"):
                        	args.append(self.getCode(items[0],II+1))
                        else:
                            args.append(str(items[0].Value))
        if (block.Type == "class"):
            genType = "class"
            args = [block.Name]
        if (block.Type == "output"):
            genType = "print"
            items = FindSrc(channelStack, blocks, block.Name,block.ID)
            if len(items) > 0:
	        arg1 = str(items[0].Name)
	    else:
	        arg1=""
            args = [block.Name, arg1]
        temp.addBlock(genType, II, args,comment)
        return temp.spaghetti

    def extract(self,isLayer=False):
        # Parsing blocks:
        tmpblocks = []
        for i in blocks:
            from copy import deepcopy
            tmp = deepcopy(i)
            tmpblocks.append(tmp)
        orderedBlock = []
        counter = len(tmpblocks)
        while (counter > 0):
            for ord in tmpblocks:
                print("-> at:" + ord.Name)
                item = FindSrc(channelStack, tmpblocks, ord.Name,ord.ID)
                if len(item) == 0:
                    from copy import deepcopy
                    if ord.Name != "processed":
                        orderedBlock += [deepcopy(ord)]
                    	ord.Name = "processed"
                    	counter -= 1
                    	print("-> parsed: " + ord.Name)
                    print("len:" + str(len(item)))
                    print(counter)
        for i in orderedBlock:
            print(i.Name)
        # Generating
        print("EXTRACT: Status:");
        temp = Generator(first=True)
        II = 0
        for i in orderedBlock:
            print(i.Name + ", " + i.Type + ", " + i.Caption + ", " + str(i.ID) + ".")
            comment = "Code for " + i.Name + " block; " + i.Caption + ":"
            if (i.Type == "variable"):
                genType = "var"
                arg1 = i.Name
                items = FindSrc(channelStack, blocks, i.Name,i.ID)
                dst = FindDst(channelStack, blocks, i.Name,i.ID)
                if (channelStack and items):
                    if items[0].Type=="method" and (items[0].Name[0:2] == "if" or items[0].Name[0:3] == "for" or items[0].Name[0:5] == "while"):
	                    arg2 = str(i.Value)
	            else:
	            	    arg2 = str(items[0].Name)
                else:
                    arg2 = str(i.Value)
                if(len(dst)>0):
                    if(dst[0].Type == "method" and dst[0].Name[0] != 't'):
                	comment = arg1=arg2=""
                	genType = "empty"
                args = [i.Name, arg1, arg2]
            if (i.Type == "method"):
                genType = i.Name
                genType = genType[:-1]
                argNum = getArgNum(genType)
                args = [i.Name]
                if argNum == 1:
                    items = FindSrc(channelStack, blocks, i.Name,i.ID)
                    if len(items)>0:
	                    args.append(str(items[0].Name))
                if argNum > 1:
                    for j in range(1, argNum + 1):
                        items = FindSrc(channelStack, blocks, i.Name,i.ID, argN=j)
                        if len(items) > 0:
                            if ((genType == "while" or genType == "if") and j > 1):
                                args.append(self.getCode(items[0],II+1))
                            elif ((genType == "for") and j > 2):
                                args.append(self.getCode(items[0],II+1))
                            elif (genType == "output"):
                            	args.append(self.getCode(items[0],II+1))
                            else:
                                args.append(str(items[0].Value))
                pass
            if (i.Type == "class"):
                genType = "class"
                args = [i.Name]
                pass
            if (i.Type == "output"):
                genType = "print"
                items = FindSrc(channelStack, blocks, i.Name,i.ID)
                if len(items)>0:
                    print("******-> "+str(items[0].Type))
                    arg1 = str(items[0].Name)
                else:
                    arg1 = ""
                args = [i.Name, arg1]
            temp.addBlock(genType, II, args,comment)
        print(temp.spaghetti)
        if isLayer:
        	global layerCount
        	temp.release(path=(PATH[:-9]+"layer"+str(layerCount)+".py"))
        else:
        	temp.release(path=PATH)
        if isLayer:
        	myHandler = errorHandler((PATH[:-9]+"layer"+str(layerCount)+".py"))
        else:
        	myHandler = errorHandler(PATH)
        myHandler.Monitor()
        myHandler.makeReport()
        global debugText
        debugText = "Error: \n" + myHandler.err + "\n"

    def make_layer(self):
        self.extract(isLayer=True)
        


class DocumentOptions(BoxLayout):
    pass

class SampGridLayout(GridLayout):
    buildSpaceRef = BuildSpace
    pass

class WYSIWYGApp(App):
    def build(self):
        return SampGridLayout()

if __name__=="__main__":
    sample_app = WYSIWYGApp()
    sample_app.run()

#    def channelRedraw():
#        for i in lineStack:
#            with build.canvas:
