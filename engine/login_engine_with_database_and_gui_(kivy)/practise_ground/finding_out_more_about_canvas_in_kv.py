from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.modalview import ModalView


from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty,BooleanProperty,NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics.vertex_instructions import Rectangle,Line,Ellipse,RoundedRectangle
from kivy.graphics.context_instructions import Color
from kivy.graphics.instructions import Canvas # canvas
from kivy.properties import Clock
from kivy.uix.screenmanager import ScreenManager,Screen

class Moddy(ModalView):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='Hello world'))
        self.open()

class MyBox(BoxLayout):
    pass
'''



    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.l=Label(text='and others')
        self.add_widget(self.l)
        size=(NumericProperty(self.l.size[0]),NumericProperty(self.l.size[1]))
        with self.l.canvas.before:
            Color(rgba=(0,0,1,1))
            self.r=Rectangle(pos=self.l.pos,size=self.size)
    def on_size(self,*args):
        print(args)
        print(self.l.size,self.children[1].size)
        self.r.pos=self.l.pos
        self.r.size=args[1]
'''
class Canvasing(App):
    def bulid(self):
        return Moddy()
if __name__=='__main__':
    Canvasing().run()
