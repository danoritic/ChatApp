from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput


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


class Alabel(Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.text='''
crankshaft filter

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

from kivy.uix.behaviors import ButtonBehavior

from kivy.uix.label import Label

from kivy.app import App

from kivy.uix.stacklayout import StackLayout

from kivy.uix.anchorlayout import AnchorLayout

from kivy.uix.relativelayout import RelativeLayout


---------------------------------------------------------------------
'''
        self.halign="center"
        self.valign='center'

    def on_size(self,*args):
        #self.text_size=self.size
        print(self.text_size==self.size)
        print("self.size>> ", self.size)
        print("self.text_size >>", self.text_size)
        self.font_size=.02*  ((self.height)**2+(self.width)**2)**.5
        
class MyTextInput(TextInput):
     pass
class MyLayout(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for i in range(3):
            a=Alabel( padding=[2,2], pos_hint={"center_y":.5} ) # , size=[dp(350),dp(380)] ,size_hint=[None,None]
            self.add_widget(a)
class LabelApp(App):
    def build(self):
        a=Alabel()
        t=MyTextInput()
        for i in dir(t):
            if "__" not in i:
                print(i)
            pass
        print("----",a.uid)
        m=MyLayout()
        print(">>>>>> ",m.children[0].text_size)
        return MyLayout()
if __name__=="__main__":
    LabelApp().run()
