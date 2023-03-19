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

import time
import sqlite3
import os
from database_management import Database #.the_gui
from user_stuff import User
#print(kivy.__version__)

# The other kivy files
from HomePage import *
from TheSignupPage import *

#------------------------------------------------------------------------------

# the imported class

class LoginMechanism:
    def __init__(self,):
        self.database=Database()
        self.friend_list={'danoritic':['shadow']}
        print("welcome to swift")
        time.sleep(1)
        var=str(input('''
Do you have an account or do you want to register one?
1) I have an account
2) I want to sign up
>>'''))
        proceed=False
        while not proceed:
            if int(var)==1:
                proceed=True
                self.login()                
            elif int(var)==2:
                #sign up
                proceed=True
                self.signup()
            else:
                Proceed=False
    def login(self):
        while not self.check_if_exist(self.username):
            self.delay()
            print('this username does not exist...')
            self.delay()
            self.username=str(input('please enter another one>>'))
        else:
            self.password=str(input('Enter your password'))
            while not self.check_if_match(self.username,{'password':self.password}):
                self.delay()
                print('this password is not correct...')
                self.delay()
                self.password=str(input('please enter another one'))
            else:
                print('LOGIN SUCCESSFULL')
        user=User(self.username,self.database)
        for i in self.database.get_all_users():
            if i['username']!=self.username:
                user.add_friend(i['username'])
        user.start_chat_with_friend()
    def signup(self):
        self.new_user_surname=str(input('Enter surname >>'))
        self.new_user_first_name=str(input('Enter first name >>'))
        self.username=str(input('Enter username'))
        while self.check_if_exist(self.username):
            print('username already exist')
            self.delay()
            self.username=str(input('Enter username'))
        else:
            self.password=str(input("Create a password >>"))
            self.confirm_password=str(input("Confirm your password >>"))
            while self.password!=self.confirm_password:
                print('password not the same')
                self.delay()
                print('please enter the same password')
                self.password=str(input("Create a password >>"))

                self.database.user_detail.update({'danoritic':{"surname":'olasiyan','first name':'Daniel','password':'daniel1234'}})
                
                self.confirm_password=str(input("Confirm your password >>"))
            else:
                stored_data={"surname":self.new_user_surname,'first name':self.new_user_first_name,'password':self.confirm_password}
                self.database.username_list.append(self.username)
                self.database.register_user_database(self.username,stored_data)
                print(self.database.get_all_users())
                self.login()
    def delay(self,t=1):
        time.sleep(t)
    def check_if_exist(self,username):
        return self.database.check_if_exist(username)
    def check_if_match(self,username,pair):
        return self.database.check_if_match(username,pair)


# ----------------------------------------------------------------------------
class Mainframe(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.friend_list={'danoritic':['shadow']}
        #self.login_mechanism=LoginMechanism()
        self.database=Database()
    def login(self,username,password):
        if self.database.check_if_exist(username) and self.database.check_if_match(username,{"password":password}):
            print("pass ",self.ids.username.__class__)
        else:
            print("blocked")
        
    def sign_up(self):
        pass
       
class ScreenHandler(ScreenManager):
    pass
class TheLoginPage(App):
    def build(self):
        stiff=ScreenHandler()
        return stiff

if __name__=='__main__':
    TheLoginPage().run()


