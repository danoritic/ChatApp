import os
import time
import sqlite3



'''
The chat history is stored in this format:
    Each user has his own database
    Each user's friend has his own table with the name username_friend_name_chat
    Each of the user friend table has this fields: message, owner,sn,date

'''


class Chat:
    def __init__(self,database,username):
        self.database=database
        self.username=username
        self.friend_name=''
    def show_chat(self,friend_name):
        self.friend_name=friend_name
        result=self.database.get_user_chat_history(self.username,friend_name)
        count=0
        print("*"*20)
        print('result**>>',result)
        print("*"*20)
        print(len(result))
        while count<len(result):
            #print(count)
            if result[count]['owner']==self.username:
                print('Me')
            else:
                print(result[count]['owner'].upper())
            print(result[count]['message'])
            count+=1
        self.sn=len(result)
               
    def store_chat(self,chat_details):
        data=(chat_details['sn'],
        chat_details['date'],
        chat_details['message'],
        chat_details['owner'])
        
        self.database.store_user_chat(self.username,self.friend_name,data)
        

