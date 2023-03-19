from kivy.config import Config
Config.set("graphics","resizable",False)

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window



from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty,BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image

from kivy.graphics.vertex_instructions import Rectangle,Line,Ellipse,RoundedRectangle,Triangle

from kivy.graphics.context_instructions import Color
from kivy.graphics.instructions import Canvas # canvas
from kivy.uix.image import Image
from kivy.properties import Clock

# user defined modules
from Image_preparer import crop_to_circle

# importing other file
import os
import wx

apple="Fruit"



"""
canvas:
                            Color:
                                rgba:(0,1,0,1)
                            RoundedRectangle:
                                pos:self.pos
                                size:self.size

#what next is the interaction with the former build-up
# text widgets must be sensitive to change in window size

Having a minimum size and changing into a scrollable placade below this size

i think the text width should be fixed and should be the half of the display placade at the minimum
window.
"""

class MessageBox(AnchorLayout):
    def __init__(self,text='danoritic', **kwargs):
        #print("self.ids >>>",self.uid)
        super().__init__(**kwargs) # the kwargs must to contain the master, the owner  and the text        
        self.text=text
        self.text_label=Label(text=self.text,size_hint=(None,1),
                              width=758/2,height=120,padding_x=14,size_hint_max_x=400)  
        self.owner="danoriti"
        self.user="danoritic"
        self.spacing=1
        self.size_hint=(1,None)
        self.size_hint_max_x=400
        self.add_widget(self.text_label)
        #the determining the sides mechanism
        
         
        if self.owner=="danoritic":
            self.anchor_x="right"
        else:
            self.anchor_x="left"
        
        with self.text_label.canvas.before:
            Color(rgba=(0,168/255,89/255,1))
            self.board=RoundedRectangle(pos=(self.text_label.pos[0]+7,self.text_label.pos[1]),
                                        size=(self.text_label.size[0]-10,self.text_label.size[1]),)
            #Color(rgba=(0,0/255,89/255,1))
            p1=[self.text_label.pos[0],self.text_label.pos[1]+self.text_label.height]
            p2=[self.text_label.pos[0]+30,self.text_label.pos[1]+self.text_label.height]
            p3=[self.text_label.pos[0]+15,self.text_label.pos[1]+self.text_label.height-20]
            self.pointy=Triangle()
            self.pointy.points=(p1+p2+p3)
        self.text_label.bind(pos=self.update_pos,size=self.update_size)
        # adjusting th pointy triangle shape
        if self.owner==self.user:
            self.board.pos=(self.text_label.pos[0]-7,self.text_label.pos[1])

            p1=[self.text_label.pos[0],self.text_label.pos[1]+self.text_label.height]
            p2=[self.text_label.pos[0]+30,self.text_label.pos[1]+self.text_label.height]
            p3=[self.text_label.pos[0]+15,self.text_label.pos[1]+self.text_label.height-20]
            self.pointy.points=(p1+p2+p3)
            
        else:
            self.board.pos=(self.text_label.pos[0]+7,self.text_label.pos[1])
            p1=[self.text_label.pos[0]+self.text_label.size[0],self.text_label.pos[1]+self.text_label.height]
            p2=[self.text_label.pos[0]+self.text_label.size[0]-30,self.text_label.pos[1]+self.text_label.height]
            p3=[self.text_label.pos[0]+self.text_label.size[0]-15,self.text_label.pos[1]+self.text_label.height-20]
            self.pointy.points=(p1+p2+p3)
            
        
        #self.text_label.size[0]=1920/2
        
    def update_pos(self,instance,pos):
        if self.owner==self.user:
            self.board.pos=(pos[0]-7,pos[1])
            p1=[pos[0]+instance.size[0],pos[1]+instance.height]
            p2=[pos[0]+instance.size[0]-30,pos[1]+instance.height]
            p3=[pos[0]+instance.size[0]-15,pos[1]+instance.height-20]
            self.pointy.points=(p1+p2+p3) 
        else:
            self.board.pos=(pos[0]+7,pos[1])
            p1=[pos[0],pos[1]+instance.height]
            p2=[pos[0]+30,pos[1]+instance.height]
            p3=[pos[0]+15,pos[1]+instance.height-20]
            self.pointy.points=(p1+p2+p3) 
    def update_size(self,instance,size):
        self.board.size=size
        self.text_label.text_size=self.text_label.size
        p1=[instance.pos[0],instance.pos[1]+instance.height]
        p2=[instance.pos[0]+30,instance.pos[1]+instance.height]
        p3=[instance.pos[0]+15,instance.pos[1]+instance.height-20]
        self.pointy.points=(p1+p2+p3)
        if self.text_label.texture_size!=size:
            pass

            
        
        
class HomePageMainframe(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.gin=None
        self.cnt=0
    def do(self):
        print(self.children)
        print(self.ids)
    def create_text_label(self,text):
        self.ids.text_area.bind(height=self.equalize_label_and_text_input)
        self.ids.text_area.do_wrap=True
        m=MessageBox(text=text)
        
        self.m=m
        '''
        print("Important !!!!!!!!",self.ids.chat_board.size)
        print("Height ",self.ids.text_area.line_height)
        print("spacing ",self.ids.text_area.line_spacing)
        print("Other height",m.text_label.line_height)
        '''
        self.ids.text_area.line_height=20
        
        original_text_area_size=self.ids.text_area.width
        self.ids.text_area.width=m.text_label.width
        m.height=self.ids.text_area.minimum_height
        '''
        print(m.text_label.events())
        print(m.anchor_x)
        '''
        
        '''
        print(m.height==self.ids.text_area.height)
        print(m.height)
        print(self.ids.text_area.height)
        print(m.height==self.ids.text_area.height)
        '''
        #m.height=self.ids.text_area.height
        print(self.ids.text_area.padding)
        Clock.schedule_once(self.didi_TS,.0001)
        
        
    def equalize_label_and_text_input(self,*args):
        self.cnt+=1
        print("Impopo>>>>>>>>",self.cnt)
        #self.m.height=self.ids.text_area.height
        
        #if self.cnt==3:
            #self.ids.text_area.unbind(height=self.equalize_label_and_text_input)
        
    def didi_TS(self,*args):
        print(self.m.height==self.ids.text_area.height)
        self.m.height=self.ids.text_area.minimum_height
        self.ids.chat_board.add_widget(self.m)
        self.ids.text_area.text=""
class ButtonImage(ButtonBehavior,Image):
    def on_press(*args):
        pass #print(22)

class EnhancedImage(ButtonImage):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.size=(100,100)
        self.save_path=os.path.abspath(os.path.dirname(__file__))+'/temps/'
        print(self.ids)
        #self.=print(12)
    def on_press(self,*args):
        pass
    def on_source(self,*args):
        self.save_name=self.source.split('/').pop()
        if self.save_name in os.listdir(self.save_path):
            os.remove(self.save_path+'/'+self.save_name)
        im=crop_to_circle(self.source,self.size)
        new_path_and_name=self.save_path+self.save_name.split('.jpg')[0]+'.png'
        im.save(new_path_and_name)
        
        
class TheHomePage(App):
    pass
Window.size = (1100, 600)
x,y=Window._get_window_pos()[0]/2, Window._get_window_pos()[1]/2  #-500/2  -900/2
print(Window._get_window_pos())
Window._set_window_pos(x,y)
Window._set_shape(shape_image="C:/code/video player/resource/play_button.png")
for i in dir(Window):
    #if "__" not in i:
    if "set" in i:
        print(i)

if __name__=="__main__":
    TheHomePage().run()
