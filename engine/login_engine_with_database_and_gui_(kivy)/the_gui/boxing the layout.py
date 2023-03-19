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

from kivy.graphics.vertex_instructions import Rectangle,Line,Ellipse,RoundedRectangle,Triangle

from kivy.graphics.context_instructions import Color
from kivy.graphics.instructions import Canvas # canvas
from kivy.uix.image import Image
from kivy.properties import Clock


class MyBox(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lab1=Button(text="1",size_hint=(None,1), width=120)
        lab2=Button(text="2",size_hint=(None,None),height=120, width=120, pos_hint={"top":.5,"right":.5})
        self.add_widget(lab1)
        self.add_widget(lab2)

class MyAnchor(AnchorLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lab1=Button(text="1",size_hint=(None,1), width=120)
        lab2=Button(text="2",size_hint=(None,None),height=120, width=120, pos_hint={"top":.5,"right":.5})
        self.anchor_x="right"
        self.add_widget(lab1)
        self.anchor_x="left"
        self.add_widget(lab2)

class MyRelative(RelativeLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lab1=Button(text="1",size_hint=(None,1), width=120)
        lab2=Button(text="2",size_hint=(None,1),height=120, width=120, pos_hint={"right":1})
        self.anchor_x="right"
        self.add_widget(lab1)
        self.anchor_x="left"
        self.add_widget(lab2)
class Boxing(App):
    def build(self):
        return MyRelative()


if __name__=="__main__":
    Boxing().run()
