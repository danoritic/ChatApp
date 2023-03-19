from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatterlayout import ScatterLayout


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

class Boxings(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.count=0
        box=BoxLayout()
        self.add_widget(box)
        self.boxify(box)
        strings=['vertical','horizontal']
    def boxify(self,layout):
        layoutlet=BoxLayout()
        if layout.orientation=='vertical':
            layoutlet.orientation='horizontal'
        else:
            layoutlet.orientation='vertical'
        butns=Button(text='.')
        layout.add_widget(butns)
        layout.add_widget(layoutlet)
        if self.count==2:
            layout.add_widget(MyFloat())
        
        if self.count!=7:
            self.count+=1
            self.boxify(layoutlet)
            
            
class MyFloat(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        btn_list=[]
        self.size_hint=(0,1)#Float
        for i in range(12):
            btn_list.append(Button(text='num '+str(i),size_hint=(.2,.2),pos=(self.size[0]*.2*i,0))) # pos_hint=(None,None),
            self.add_widget(btn_list[i])

class The(App):
    def build(self):
        return Boxings()
if __name__=='__main__':
    The().run()
