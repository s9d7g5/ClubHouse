'''
Author : Sangsoo Jeong 
Date : 28 Mar 2021
'''

'''
Methodology

1. To get API function name -> Decrypted ios encrypt logic
2. To packet analysis -> Through Disable SSL Pinning 
'''
import requests
import urllib3
import random
import json
import sys

urllib3.disable_warnings()

class ClubHouse():
    # Header
    MAIN_URL = "https://www.clubhouseapi.com/api/"
    COPY_URL = MAIN_URL
    VALID_USER_INFO = [] 
    # When you make a header, If you don't have a cookie the cookie will set on the response through the set-cookie
    HEADER = {
        "CH-UserID": "null",
        "CH-Languages": "en-SG",
        "CH-Locale": "en_SG",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-SG;q=1",
        "CH-AppBuild": "331",
        "CH-AppVersion": "0.1.31",
        "Accept": "application/json; charset=utf-8",
        "CH-DeviceId": "621BDF2D-1C4D-4C18-B2FE-9E355B2E0600",
        "User-Agent": "clubhouse/331 (iPhone; iOS 13.6.1; Scale/3.00)"
    }
    
    def HTTP_Protocol(self,http,json_data,parameter):
        if(http == "post"):
            response_post = requests.post(  self.MAIN_URL, 
                            #PHONE, ##### => Note. Although the Clubhouse Request is post, but do not use real POST data
                            json = f"{json_data}",
                            headers=self.HEADER,
                            verify = False
                        )
            _response = response_post
                
        else: # get
            response_get = requests.get(
            self.MAIN_URL,
            headers=self.HEADER,
            params=parameter,
            verify=False
            )
            _response = response_get
        return _response

    def User_First_Access(self):
        '''
        WRONG DATA 
                GET /api/check_for_update?is_testflight=0 HTTP/1.1
                Host: www.clubhouseapi.com
                User-Agent: python-requests/2.25.1
                Accept-Encoding: gzip, deflate
                Accept: */*
                Connection: close
        '''
        parameter = {
            'is_testflight':f'{random.randint(1,100)}'
        }
        self.MAIN_URL += "check_for_update?"
        print(self.MAIN_URL)
        response_get = requests.get(
            self.MAIN_URL,
            headers=self.HEADER,
            params=parameter,
            verify=False)
        
        self.MAIN_URL = ""   # Important
        return response_get

    def Get_User_Header(self,response_data):
        return response_data.headers



    def Authentication(self, set_cookie, phone_number):
        self.MAIN_URL = self.COPY_URL
        self.MAIN_URL += "start_phone_number_auth"
        print(self.MAIN_URL)
        # append json data (__cfduid)
        cloudflare = {
            "__cfduid" : f"{set_cookie}"
        }

        # WRONG
        #self.HEADER['__cfduid'] = f"{set_cookie}"

        PHONE = {
            "phone_number" : f"{phone_number}"
        }

        
        response_post = requests.post(  self.MAIN_URL, 
                        #PHONE, ##### => Note. Although the Clubhouse Request is post, but do not use real POST data
                        json = PHONE,
                        cookies=cloudflare, # correct
                        headers=self.HEADER,
                        verify = False
                    )
        
        self.MAIN_URL = ""   # Important

        if(response_post.status_code == 200):
            print(f"Welcome {phone_number}")
            return 1
        else:
            print("Could you check your Phone number again?")
            sys.exit(0)

    def Send_Verification_Code(self, phone_number, verify_code):
        self.MAIN_URL = self.COPY_URL
        self.MAIN_URL += "complete_phone_number_auth"
        print(self.MAIN_URL)
        PHONE =  {
            "verification_code":f"{verify_code}",
            "phone_number":f"{phone_number}",
            "device_token": "AAAA" # dummy 
        }
        
        response_post = requests.post(  self.MAIN_URL, 
                        #PHONE, ##### => Note. Although the Clubhouse Request is post, but do not use real POST data
                        json = PHONE,
                        headers=self.HEADER,
                        verify = False
                    )
        
        self.MAIN_URL = ""   # Important
        if(response_post.status_code == 200):
            #uesrname = response_post["username"]
            _json_data = response_post.json()
            print(_json_data) # Debug
            try:
                name = _json_data['user_profile']['name']
                username = _json_data['user_profile']['username']
                auth_token = _json_data['auth_token']
                refresh_token = _json_data['refresh_token']
                access_token = _json_data['access_token']
                
                self.VALID_USER_INFO.append(name)
                self.VALID_USER_INFO.append(username)
                self.VALID_USER_INFO.append(auth_token)
                self.VALID_USER_INFO.append(refresh_token)
                self.VALID_USER_INFO.append(access_token)
                
                print(self.VALID_USER_INFO)
                return True
            except KeyError as f:
                print(f"This key json type is error {f} ! ! !")

    def Comming_Lobby(self):
        self.MAIN_URL = self.COPY_URL
        self.MAIN_URL += "update_notifications"
        print(self.MAIN_URL)
        # DEFAULT
        UPDATE_NOTIFICATION =  {
            "enable_trending":-1,
            "pause_till":-1,
            "is_sandbox":False,
            #"apn_token":"297711469a8359410ca2f76947e451fedda480bd3f70092f33b95c2896c45192",
            "system_enabled":1,
            "frequency":-1
        }
        
        response_post = requests.post(  self.MAIN_URL, 
                        #PHONE, ##### => Note. Although the Clubhouse Request is post, but do not use real POST data
                        json = UPDATE_NOTIFICATION,
                        headers=self.HEADER,
                        verify = False
                    )
        
        self.MAIN_URL = ""   # Important


    def Get_Online_Friend(self):
        test = ""

    def Get_ME(self):
        self.MAIN_URL = self.COPY_URL
        self.MAIN_URL += "me"
        print(self.MAIN_URL)
        MY_AREA = {
            "return_blocked_ids":True,
            "timezone_identifier":"Asia\/Singapore",
            "return_following_ids":True
        }
        
        
        response_post = requests.post(  self.MAIN_URL, 
                    #PHONE, ##### => Note. Although the Clubhouse Request is post, but do not use real POST data
                    json = MY_AREA,
                    headers=self.HEADER,
                    verify = False
                )
        self.MAIN_URL = ""

        _json_data = response_post.json()

        if response_get.status_code == 401:
            print(f"401 ===> {response_get.text}")
        

    def Show_Channel_List(self):
        self.MAIN_URL = self.COPY_URL
        self.MAIN_URL += "get_channels"       

        response_get = requests.get(
            self.MAIN_URL,
            headers=self.HEADER,
            #params=parameter,
            verify=False)
        
        if response_get.status_code == 200:
            print(response_get.text)
        if response_get.status_code == 401:
            print(f"401 ===> {response_get.text}")
