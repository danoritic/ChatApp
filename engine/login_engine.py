import time

class User:
    def __init__(self):
        self.surname=None
        self.name=None
        self.username=None
        self.friend_list=[]
        

    def add_friend (self,username):
        self.friend_list.append(username)

class Database:
    def __init__(self):
        self.username_list=[]
        self.user_detail={}
        ## for testing purpose
        self.username_list.append('danoritic')
        for i in self.username_list:
            self.user_detail.update({i:{"surname":None,'first name':None,'password':None}})
        self.user_detail.update({'danoritic':{"surname":'olasiyan','first name':'Daniel','password':'daniel1234'}})
        # 
        
        
    def check_if_match (self,username,pair):
        if pair['password'] == self.user_detail[username]['password']:
            return True
        return False
    def check_if_exist(self,username):
        if username in self.username_list:
            return True
        return False
    def store(self,username,pair):
        self.user_detail.update({username:{"surname":None,'first name':None,'password':None}})
        _dict=self.user_detail[username]
        changed_data_keys=list(pair.keys()) # Logic
        for i in changed_data_keys:
            _dict[i]=pair[i]
        return True
   
        
class LoginMechanism:
    def __init__(self,):
        self.database=Database()
        print("welcome to swift")
        time.sleep(1)
        var=str(input('''Do you have an account or do you want to register one?
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
                self.database.store(self.username,stored_data)
                self.login()
    def delay(self,t=1):
        time.sleep(t)
    def check_if_exist(self,username):
        return self.database.check_if_exist(username)
    def check_if_match(self,username,pair):
        return self.database.check_if_match(username,pair)
LoginMechanism()
        
                       
