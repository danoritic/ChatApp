from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout

from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty,BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics.vertex_instructions import Rectangle,Line,Ellipse,RoundedRectangle
from kivy.graphics.context_instructions import Color
from kivy.graphics.instructions import Canvas # canvas
from kivy.uix.image import Image
from kivy.properties import Clock

# user defined modules
from Image_preparer import crop_to_circle

# importing other file
import os



#what next is the interaction with the former build-up

"""
    def update_pos(self,instance,pos):
        for k in self.store_array.keys():
            if self.store_array[k]["Ls"]==instance:
                self.store_array[k]["Libels"].pos=pos
                
        self.count+=1
        return pos 
    def update_size(self,instance,size):
        for k in self.store_array.keys():
            if self.store_array[k]["Ls"]==instance:
                self.store_array[k]["Libels"].size=size
                self.store_array[k]["Libels"].radius=(.4*min(size[0],size[1]),)
        self.count+=1
        return size 
"""
class MessageBox(AnchorLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs) # the kwargs must to contain the master, the owner  and the text
        #self.owner=kwargs['owner']
        self.text="danoritic"
        self.text_label=Label(text=self.text,size_hint=(1,None),height=120)
        self.owner="danoriti"
        #self.master.message_list={}      #this is a dictionary of text_label and board
        self.size_hint=(None,None)
        self.height=120
        self.width= 120
         # kwargs["text"]
        self.add_widget(self.text_label)
        if self.owner=="danoritic":
            self.anchor_x="right"
        else:
            self.anchor_x="left"
        with self.text_label.canvas.before:
            Color(rgba=(0,168/255,89/255,1))
            self.board=RoundedRectangle(pos=self.text_label.pos,size=(self.text_label.size[0]-10,self.text_label.size[1]))
        self.text_label.bind(pos=self.update_pos)
        self.text_label.bind(size=self.update_size)
    '''    
    def on_text(self,*args):
        self.text_label.text=self.text
        print(self.text)
    '''
    def update_pos(self,instance,pos):
        self.board.pos=pos
        return pos 
    def update_size(self,instance,size):
        self.board.size=size
        return size 
class Mainframe(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def do(self):
        print(self.children)
        print(self.ids)
    def create_text_label(self):
        MessageBox(anchor_x="right",size_hint=(None,None),
                            height=120,text="frail",owner="danoritic",
                           width=120,
                           )
        print("crankshaft")
class ButtonImage(ButtonBehavior,Image):
    def on_press(*args):
        print(22)

class EnhancedImage(ButtonImage):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.size=(100,100)
        self.save_path=os.path.abspath(os.path.dirname(__file__))+'/temps/'
        print(self.ids)
        #self.=print(12)
    '''def on_press(self,*args):
        print(self.ids)'''
    def on_source(self,*args):
        self.save_name=self.source.split('/').pop()
        if self.save_name in os.listdir(self.save_path):
            os.remove(self.save_path+'/'+self.save_name)
        im=crop_to_circle(self.source,self.size)
        new_path_and_name=self.save_path+self.save_name.split('.jpg')[0]+'.png'
        im.save(new_path_and_name)
        
        
class TheHomePage(App):
    pass


if __name__=="__main__":
    TheHomePage().run()
'''
    AnchorLayout:
                            anchor_x:"right"
                            size_hint:(1,None)
                            height:120
                                
                            MessageBox:
                                text:"Frail"
                                size_hint:(None,1)
                                width:120
                        AnchorLayout:
                            anchor_x:"right"
                            size_hint:(1,None)
                            height:120
                                
                            MessageBox:
                                text:"Frail"
                                size_hint:(None,1)
                                width:120
                        AnchorLayout:
                            anchor_x:"right"
                            size_hint:(1,None)
                            height:120
                                
                            MessageBox:
                                text:"Frail"
                                size_hint:(None,1)
                                width:120
                        AnchorLayout:
                            anchor_x:"right"
                            size_hint:(1,None)
                            height:120
                                
                            MessageBox:
                                text:"Frail"
                                size_hint:(None,1)
                                width:120
                        AnchorLayout:
                            anchor_x:"left"
                            size_hint:(1,None)
                            height:120
                                
                            MessageBox:
                                text:"Frail"
                                size_hint:(None,1)
                                width:120
                        AnchorLayout:
                            anchor_x:"left"
                            size_hint:(1,None)
                            height:120
                                
                            MessageBox:
                                text:"Frail"
                                size_hint:(None,1)
                                width:120
                        AnchorLayout:
                            anchor_x:"left"
                            size_hint:(1,None)
                            height:120
                                
                            MessageBox:
                                text:"Frail"
                                size_hint:(None,1)
                                width:120
                        AnchorLayout:
                            anchor_x:"right"
                            size_hint:(1,None)
                            height:120
                            
                            MessageBox:
                                text:"Frail"
                                size_hint:(None,1)
                                width:120
                        
                
'''
