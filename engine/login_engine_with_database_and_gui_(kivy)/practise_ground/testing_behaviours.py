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
from kivy.uix.behaviors import TouchRippleBehavior

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


class Widgy(TouchRippleBehavior,Button):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.text='riddling'
        self.size_hint=(.2,.2)
        self.pos_hint={'center_x':.5,'center_y':.5}
        self.background_color=(0,0,0,0)
        #self.background_normal=''
        with self.canvas:
            Color(rgba=(.5,.5,.5,1))
            self.r=RoundedRectangle(pos=self.pos,size=self.size)
    def on_size(self,*args):
        self.r.pos=self.pos
        self.r.size=self.size
    def on_touch_down(self, touch):
        collide_point = self.collide_point(touch.x, touch.y)
        #print(collide_point)
        if collide_point:
            touch.grab(self)
            self.ripple_show(touch)
            return True
        return False
    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self.ripple_fade()
            return True
        return False
class Runner(App):
    def build(self):
        return Widgy()

if __name__=='__main__':
    Runner().run()
