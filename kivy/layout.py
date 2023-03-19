from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty,BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image

from kivy.graphics.vertex_instructions import Rectangle,Line,Ellipse
from kivy.graphics.context_instructions import Color
from kivy.graphics.instructions import Canvas # canvas


from kivy.properties import Clock

class ButtonList(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.supe=[]
        self.orientation='vertical'
        self.b=None
        self.rects=[]
        height=dp(120)
        for i in range(30):
            substance=Button(text=str(i),size_hint_y=None,height=height,pos=self.pos)
            #blanket=BoxLayout()
            #blanket.add_widget(substance)
            self.supe.append(substance )
            
            self.add_widget(substance)
        '''
        for i in range(len(self.supe)):
            with self.supe[i].canvas:
                Color(rgba=(i%2,(i+2)%2,(i+7)%2,.9))
                r=Rectangle(pos=self.supe[i].pos,size=(self.supe[i].size[0]-i*10,self.supe[i].size[1]))
                self.rects.append(r)
            print(self.supe[i].size)
        '''
        self.rects
class Laid(App):
    pass

Laid().run()
