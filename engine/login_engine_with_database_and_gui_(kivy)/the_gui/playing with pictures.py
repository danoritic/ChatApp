from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
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
from kivy.properties import Clock

class CustomWidget(RelativeLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.B=Button(text='free')
        #self.size=(100,100)
        with self.canvas:
            Color(rgba=(0,1,0,1))
            #self.r=Rectangle(pos=self.pos,size=self.size)
            self.image=Image(source='C:/code/chat app v1/engine/login_engine_with_database_and_gui_(kivy)/the_gui/res/MainFrame.png',keep_ratio=True,pos=self.pos)
            #self.l1=Line(points=(0,self.height/2,self.width,self.height/2))
            #print(self.image.size,self.image.pos)
    def on_size(self,*args):
        #self.r.size=self.size
        print('*'*12)
        print(self.image.size,self.image.pos)
        print(self.size,self.pos)
        print('*'*12)
        #self.image.pos=(i/2 for i in self.center)   #(self.center_x-self.size[0]/2,self.center_y-self.size[1]/2)    # 
        #self.image.size=(i-20 for i in self.size)
        self.image.pos=self.pos
        self.image.size=self.size
        #self.l1.points=(0,self.height/2,self.width,self.height/2)
class Plane (Label):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(rgba=(0,.5,.5,1))
            self.ori_plane=RoundedRectangle(radius=[30,])
    def on_size(self, *args):
        self.ori_plane.size=self.size
        self.ori_plane.pos=self.pos
        
        
class MyAnchor(AnchorLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.anchor_x='right'
        #self.anchor_y='top'
        self.plane=Plane(size_hint=(.8,.8))
        #b=Button(text='France',size=(100,100),size_hint=(None,None))
       # self.widgy=CustomWidget()
        #print('self.widgy.size',self.widgy.size)
        #self.add_widget(self.widgy)
        self.add_widget(self.plane)
        
        
        #self.B=Button(text='free',size_hint=(None,None),size=(100,100))
        #self.add_widget(self.B)

class TheFirApp(App):
    def build(self):
        return MyAnchor()


if __name__=='__main__':
    TheFirApp().run()
