import time
import sqlite3
import os
from database_management import Database
from user_stuff import User

'''
I will have a general database and a specific user database
'''

        
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
        self.username=str(input('please enter username :'))
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
        #user.add_friend('shadow')
        #user.add_friend('frix')
        
        for i in self.database.get_all_users():
            if i['username']!=self.username:
                print('*'*10)
                print(i['username'],self.username)
                print('*'*10)
                
                user.add_friend(i['username'])
        user.start_chat_with_friend()
        '''
        print('who do you want to chat with...')
        cnt=0
        listings=self.friend_list[self.username]
        while cnt<len(listings):
            print(' {n}>>{o}\n'.format(n=cnt+1,o=listings[cnt]))
            cnt+=1
        self.current_friend=listings[int(input())-1]
        print(self.current_friend)
        '''
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

LoginMechanism()
        
                       
