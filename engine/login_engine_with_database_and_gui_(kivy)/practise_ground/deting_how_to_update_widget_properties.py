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

class MyLabel: 
    pass 
class Mainframe(AnchorLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        self.count=1
        self.store_array={}
        self.spacing=12
        self.padding=12
        for i in range(2):
            self.l=Label(text="number "+str(i))  
            self.add_widget(self.l)
            with self.l.canvas.before:
                Color(rgba=(1,0,1,1))
                self.libel=RoundedRectangle(pos=self.l.pos,size=self.l.size,radius=(50,))
                
                self.store_array.update({i+1:{"Ls":self.l,"Libels":self.libel}})

        for k in self.store_array.keys():
            self.store_array[k]["Ls"].bind(pos=self.update_pos,size=self.update_size)
    def update_pos(self,instance,pos):
        for k in self.store_array.keys():
            if self.store_array[k]["Ls"]==instance:
                self.store_array[k]["Libels"].pos=pos
                
        self.count+=1
        return pos 
    def update_size(self,instance,size):
        for k in self.store_array.keys():
            if self.store_array[k]["Ls"]==instance:
                self.store_array[k]["Libels"].size=size
                self.store_array[k]["Libels"].radius=(.4*min(size[0],size[1]),)
        self.count+=1
        return size 
    def update(self):
        print("updating")


'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__events__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__le__', '__lt__', '__metaclass__', '__module__', '__ne__', '__new__', '__proxy_getter',
'__proxy_setter', '__pyx_vtable__', '__reduce__', '__reduce_ex__', '__repr__', '__self__',
'__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '_apply_transform',
'_context', '_disabled_count', '_disabled_value', '_find_index_in_motion_filter', '_iterate_layout',
'_kwargs_applied_init', '_proxy_ref', '_trigger_layout', '_update_motion_filter', '_walk',
'_walk_reverse', 'add_widget', 'apply_class_lang_rules', 'apply_property', 'bind', 'canvas',
'center', 'center_x', 'center_y', 'children', 'clear_widgets', 'cls', 'collide_point', 'collide_widget',
'count', 'create_property', 'dec_disabled', 'disabled', 'dispatch', 'dispatch_children',
'dispatch_generic', 'do_layout', 'events', 'export_as_image', 'export_to_png', 'fbind', 'funbind',
'get_center_x', 'get_center_y', 'get_disabled', 'get_parent_window', 'get_property_observers',
'get_right', 'get_root_window', 'get_top', 'get_window_matrix', 'getter', 'height', 'ids', 'inc_disabled',
'is_event_type', 'l', 'layout_hint_with_bounds', 'libel', 'minimum_height', 'minimum_size',
'minimum_width', 'motion_filter', 'on_kv_post', 'on_motion', 'on_opacity', 'on_touch_down',
'on_touch_move', 'on_touch_up', 'opacity', 'orientation', 'padding', 'parent', 'pos', 'pos_hint',
'properties', 'property', 'proxy_ref', 'register_event_type', 'register_for_motion_event',
'remove_widget', 'right', 'set_center_x', 'set_center_y', 'set_disabled', 'set_right', 'set_top',
'setter', 'size', 'size_hint', 'size_hint_max', 'size_hint_max_x', 'size_hint_max_y', 'size_hint_min',
'size_hint_min_x', 'size_hint_min_y', 'size_hint_x', 'size_hint_y', 'spacing', 'store_array',
'to_local', 'to_parent', 'to_widget', 'to_window', 'top', 'uid', 'unbind', 'unbind_uid',
'unregister_event_type', 'unregister_event_types', 'unregister_for_motion_event',
'update_pos', 'update_size', 'walk', 'walk_reverse', 'width', 'x', 'y']
'''
class Loader(App):
    def build(self):
        m=Mainframe()
        for i in dir(m.__getattribute__('l')):
            if "__" not in i:
                print(i)
        print(self.get_application_config())

        self.title="Ajananku"
        return m
    
'''for i,j in m.__dict__.items():
    print(i,">>>",j)
print("-"*120)
for i in dir(m.__getattribute__('l')):
    print(i)

'''

#print(dir(m))
#print(m.__getattribute__('l').get_property_observers([]))


if __name__=="__main__":
    Loader().run()
