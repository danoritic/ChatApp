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
from kivy.uix.popup import Popup

class TheMain(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for i in range(10):
            l=Button(text=str(i))
            self.add_widget(l)
        Clock.schedule_once(self.funcy,10)
    def funcy(self,*args):
        popup = Popup(title='Test popup',
            content=BoxLayout(orientation="vertical"),
                      size_hint=(None, None), size=(400, 300))
        disp_lbl=Label(text='Hello world')
            
        close_btn=Button(text='close',on_press=popup.dismiss,size_hint=(.8,.9),
                         pos_hint={"center_x":.5})
        popup.content.add_widget(disp_lbl)
        popup.content.add_widget(close_btn)
        popup.open()

class appy(App):
    def build(self):
        m=TheMain()
        return m

if __name__=="__main__":
    appy().run()

