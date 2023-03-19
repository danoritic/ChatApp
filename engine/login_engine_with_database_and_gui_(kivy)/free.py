from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.textinput import TextInput

Builder.load_string('''
<Test>:
    canvas:       # no rectangle this way
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
    background_color: 1, 1, 1, 0
''')

class Test(TextInput):
    pass

runTouchApp(Test())

'''
                
'''


from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.textinput import TextInput
Builder.load_string('''
<Test>:
    canvas.before:
        Color:
            rgba: 1, 0, 0, .5
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: root.foreground_color
    background_color: 1,1,1,0
''')
class Test(TextInput): pass
runTouchApp(Test())
