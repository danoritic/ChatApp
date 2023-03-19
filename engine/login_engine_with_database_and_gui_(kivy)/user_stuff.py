from chat_history_and_page import Chat
import time

class User:
    def __init__(self,username,database):
        self.friend_list=[]
        self.username=username
        self.database=database
        self.chat=Chat(database,username)
    def add_friend (self,friend_name):
        self.database.create_new_friend_db(self.username,friend_name)
    def select_friend(self):
        print('please select a friend you want to chat with')
        friend_list=self.database.get_friend_list(self.username)
        print('')
        cnt=0
        while cnt<len(friend_list):
            print(cnt,'>>',friend_list[cnt])
            print('')
            cnt+=1
        self.friend_name=friend_list[int(input('>> '))]

        return self.friend_name

    def start_chat_with_friend(self):
        self.select_friend()
        self.chat.show_chat(self.friend_name['friend'])
        print('')
        print(self.username)
        print('')
        message=self.input=str(input())
        date=time.strftime('%H:%M:%S')
        sn=self.chat.sn
        owner=self.username
        params={'sn':sn,'date':date,"message":message,'owner':owner}
        #params=(sn, date, message, owner)
        print('')
        self.chat.store_chat(params)
        
        while self.input!='terminate**':
            print(self.username)
            print('')
            message=self.input=str(input())
            date=time.strftime('%H:%M:%S')
            sn=self.chat.sn
            owner=self.username
            params={'sn':sn,'date':date,"message":message,'owner':owner}
            #params=(sn, date, message, owner)
            print('')
            if self.input!='terminate**':
                self.chat.store_chat(params)
            print('')
    def search_friends(self):
        pass
