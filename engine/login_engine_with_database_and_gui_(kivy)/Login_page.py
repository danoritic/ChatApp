from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
#from kivy.graphics.boxshadow import BoxShadow

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
from kivy.uix.screenmanager import ScreenManager,Screen
import kivy.graphics as vict


#print(kivy.__version__)

class Mainframe(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
    def switch(self):
        
        print(self.ids.username.__class__)
       
class ScreenHandler(ScreenManager):
    pass
class TheLoginPage(App):
    def build(self):
        stiff=ScreenHandler()
        return stiff

if __name__=='__main__':
    TheLoginPage().run()


