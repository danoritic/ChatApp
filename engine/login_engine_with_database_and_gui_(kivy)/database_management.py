import time
import sqlite3
import os

class Database:
    def __init__(self):
        self.create_database()
        self.username_list=[]
        self.user_detail={}
        ## for testing purpose
        self.username_list.append('danoritic')
        for i in self.username_list:
            self.user_detail.update({i:{"surname":None,'first name':None,'password':None}})
        self.user_detail.update({'danoritic':{"surname":'olasiyan','first name':'Daniel','password':'daniel1234'}})
        
        # 
    def interact_with_database(self,instruction,params='',name='users_login_database.db'):
            
            self.db_file=sqlite3.connect('db/'+name)
            self.cursor=self.db_file.cursor()
            self.cursor.execute(instruction,params)
            self.db_file.commit()
            self.db_file.close()
            
    def create_database(self,name='users_login_database.db',
                        table_creation_instruction='CREATE TABLE users(username TEXT,surname TEXT,first_name TEXT,password TEXT)'):
        if name not in os.listdir(os.path.abspath(os.path.dirname(__file__))+'/db/'):
            self.interact_with_database(table_creation_instruction)
            self.register_user_database('danoritic',{"surname":'olasiyan','first name':'Daniel','password':'daniel1234'})
            self.register_user_database('shadow',{"surname":'ajele','first name':'oreoluwa','password':'danlove'})
            self.register_user_database('frix',{"surname":'ajele','first name':'oreoluwa','password':'danlove'})
            
            
        else:
            pass
    def register_user_database(self,username,pair):
        surname=pair['surname']
        first_name=pair['first name']
        password=pair['password']
        add_user_to_table=' INSERT INTO users(username,surname,first_name,password) VALUES (?,?,?,?) '
        params=(username,surname,first_name,password)
        self.interact_with_database(add_user_to_table,params)
        self.create_user_friends_table(username)
    def select_from_database(self,instruction,name='users_login_database.db',params=''):
        print('naming>>> ',type(name))
        self.db_file=sqlite3.connect('db/'+name)
        
        self.cursor=self.db_file.cursor()
        self.cursor.row_factory=sqlite3.Row
        self.cursor.execute(instruction,params)
        result=[dict(row) for row in self.cursor.fetchall()]
        self.db_file.commit()
        self.db_file.close()
        return result
   
    def get_all_users (self):
        instr='SELECT * FROM users '
        #print(self.select_from_database(instr))
        return self.select_from_database(instr)
    def check_if_match (self,username,pair):
        #self.get_all_user()
        instr='SELECT password FROM users WHERE username = ? '
        password=self.select_from_database(instr,'users_login_database.db',(username,))
        print('password[0]',password[0])
        print("pair['password']",pair['password'])
        print(pair['password'] == password[0]['password'])
        if pair['password'] == password[0]['password']:
            return True
        return False
    def check_if_exist(self,username):
        instr='SELECT username FROM users'
        username_=self.select_from_database(instr) #['username']
        print('Acting>> ',self.select_from_database(instr))
        for i in username_:
            if i['username']==username:
                return True
        return False
    def store(self,username,pair):
        surname=pair['surname']
        first_name=pair['first name']
        password=pair['password']
        instr='INSERT INTO users(surname,first_name,password) VALUES (?,?,?)'
        params=(surname,first_name,password)
        
        self.user_detail.update({username:{"surname":None,'first name':None,'password':None}})
        _dict=self.user_detail[username]
        changed_data_keys=list(pair.keys()) # Logic
        for i in changed_data_keys:
            _dict[i]=pair[i]
        return True
    def alter_stored_data(self,):
        pass

   # the chat history part
   def create_user_friends_table(self,username):
       #self.check_table_created(username)
        self.db_file=sqlite3.connect('db/'+username+'.db')
        self.cursor=self.db_file.cursor()
        
        instr2='CREATE TABLE friend_list(friend text)'
        
        self.cursor.execute(instr2)
        self.db_file.commit()
        self.db_file.close()
    def create_new_friend_db(self,username,friend_name):
        '''
        #print(self.get_friend_list(username))
        if username+'.db' not in os.listdir(os.path.abspath(os.path.dirname(__file__))+'/db/'):
            self.check_table_created(username)
            self.db_file=sqlite3.connect('db/'+username+'.db')
            self.cursor=self.db_file.cursor()
            
            instr='CREATE TABLE '+username+'_'+friend_name+'_chat (sn text,date text,message text,owner text)'
            instr3='INSERT INTO friend_list(friend) VALUES(?)'
            param3=(friend_name,)
            
            self.cursor.execute(instr)
            self.cursor.execute(instr3,param3)
            self.db_file.commit()
            self.db_file.close()
        else:
            '''
        _list=self.get_friend_list(username)
        friend_list=[]
        for i in _list:
            friend_list.append(i['friend'])
        print('friend_list',friend_list)
        if friend_name not in friend_list:
            self.db_file=sqlite3.connect('db/'+username+'.db')
            self.cursor=self.db_file.cursor()
            instr='CREATE TABLE '+username+'_'+friend_name+'_chat(sn text,date text,message text,owner text)'
            
            instr3='INSERT INTO friend_list(friend) VALUES(?)'
            param3=(friend_name,)
            self.cursor.execute(instr3,param3)
            self.cursor.execute(instr,)
            self.db_file.commit()
            self.db_file.close()
        #self.create_database
    def check_table_created(self,username):
        table_extract_instr = """SELECT name FROM sqlite_master WHERE type='table';"""
        
        self.db_file=sqlite3.connect('db/'+username+'.db')
        #instr='SELECT friend FROM friend_list'
        self.cursor=self.db_file.cursor()
        self.cursor.row_factory=sqlite3.Row
        self.cursor.execute(table_extract_instr)
        result=[dict(row) for row in self.cursor.fetchall()] # dict(row) for row in 
        self.db_file.commit()
        self.db_file.close()
        print('crankshaft>>>',result)
        return result
        
    def get_user_chat_history(self,username,friend_name):
        # table name is in this format username+'_'+friend_name+'_chat'
        # user db format is username+'.db'
        instr='SELECT * FROM '+username+'_'+friend_name+'_chat'
        result=self.select_from_database(instr,name=username+'.db')
        
        return result
    def store_user_chat(self,username,friend_name,details):
        # details should be a tuple of things to be recorded
        instr='INSERT INTO '+username+'_'+friend_name+'_chat(sn,date,message,owner) VALUES(?,?,?,?)'
        self.interact_with_database(instr,details,name=username+'.db')
        
        instr='INSERT INTO '+friend_name+'_'+username+'_chat(sn,date,message,owner) VALUES(?,?,?,?)'
        self.interact_with_database(instr,details,name=friend_name+'.db')
        
        return 'pass'
    '''
    def chat_sn(self,username,friend_name):
        instr='SELECT sn from'+username+'_'+friend_name+'_chat
        result=self.select_from_database(instr,name=username+'.db')

    '''
    def get_friend_list(self,username):
        self.db_file=sqlite3.connect('db/'+username+'.db')
        instr='SELECT friend FROM friend_list'
        self.cursor=self.db_file.cursor()
        self.cursor.row_factory=sqlite3.Row
        self.cursor.execute(instr)
        result=[dict(row) for row in self.cursor.fetchall()] # dict(row) for row in 
        self.db_file.commit()
        self.db_file.close()
        #print('crank>>>',result)
        return result
        
        #self.create_database
