from kivy.lang import Builder
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
from kivy.uix.screenmanager import ScreenManager,Screen

Builder.load_file('ui.kv')
class Screen_1(Screen):
    name='Screen_1'
    pass

class Screen_2(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class TheScreen(App):
    def build(self):


        sm=ScreenManager()
        #Screen_1().name='Screen_1'
        #Screen_1().name='Screen_2'
        sm.add_widget(Screen_1(name='Screen_1'))
        sm.add_widget(Screen_2(name='Screen_2'))

        return sm

if __name__=='__main__':
    TheScreen().run()
