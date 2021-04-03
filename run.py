# ClubHouse Running
import requests
import sys
import os

from clubhouse_skeleton import clubhouse
from clubhouse_skeleton import session
from clubhouse_skeleton import rtc as rtc_class
from xml.etree.ElementTree import parse


sid = ""
name = ""
auth_token = ""

def main():
    DEBUG = True 
    
    USERID = 0
    NAME = 1
    USERNAME = 2
    AUTH_TOKEN = 3
    REFRESH_TOKEN = 4
    ACCESS_TOKEN  = 5

    client = clubhouse.ClubHouse()
    voice_service = rtc_class.RTC()

    voice_authentication = False
    # If you have a session, you do not need to login again. 
    # Requirement : user_id, auth_token, CH-DeviceId
    check_session = session.Session()

    
    # test
    #check_session.get_session()    
    

    # test
    #sys.exit(0)


    if (os.path.isfile('./user_session.xml') == True):
        print("User is online")
        # The logic add user session directy 
        phone, sid, name, nickname, auth_token, cloudflare_cookie = check_session.get_session()
        client.VALID_USER_INFO.append(sid)
        client.VALID_USER_INFO.append(name)
        client.VALID_USER_INFO.append(nickname)
        client.VALID_USER_INFO.append(auth_token)
        client.cloudflare['__cfduid'] = cloudflare_cookie
        client.HEADER['Authorization'] = f"Token {client.VALID_USER_INFO[AUTH_TOKEN]}"
        #client.
        client.Show_Channel_List()
        client.Join_Channel("M83A0nKL")
        voice_authentication = True 

    if (os.path.isfile('./user_session.xml') == False):
        init_header = client.User_First_Access()
    
        if init_header.status_code != 200:
            print("Could you check your Request Header?")
            sys.exit(0)

    #cloudflare_cookie = client.Get_User_Header(init_header)['Set-Cookie'].split(";")[0].split("__cfduid=")[1]
    #print(f"Cloud Flare Cookie = {cloudflare_cookie}") # set Cookie
        else:
            client.Get_User_Header(init_header)

        if not DEBUG:
            phone_number = input("[+] Please enter your phone number  > ")
            client.phone = phone_number

        else:
            phone_number = "+6598712847"
            client.phone = phone_number
            if (client.Authentication()):
                verify_code = input("[+] Please enter your verification code  > ")
                VALID_USER_INFO = []
                VALID_USER_INFO = client.Send_Verification_Code(phone_number, verify_code) 
                print(f"VALID_USER_INFO = {VALID_USER_INFO}")
                #if(auth_token != NULL):
                check_session.create_session(phone_number,VALID_USER_INFO,client.cloudflare['__cfduid'])
                client.Comming_Lobby() # PopUp bypass -> Reponse 401 ? 
                # get_online_friend API : up to you
                client.Get_ME()
                client.Join_Channel("M83A0nKL")
                #client.Show_Channel_List() # running

                


    if voice_authentication == True:
        # Set the voice from RTC
        try:
            import agorartc
            voice_authentication = True
            print(dir(agorartc))

            rtc = agorartc.createRtcEngineBridge()
            eventHandler = agorartc.RtcEngineEventHandlerBase()
            ret = rtc.initEventHandler(eventHandler)

            if ret == 0:
                rtc.initialize(rtc_class.AGORA_KEY, None, agorartc.AREA_CODE_GLOB & 0xFFFFFFFF)
                rtc.joinChannel("", "channel-name", "", 0)
            '''
            Suspicious module list : createRtcEngineBridge,registerAudioFrameObserver,registerVideoFrameObserver

            ref. https://github.com/AgoraIO-Community/Agora-Python-QuickStart
            '''


        except ModuleNotFoundError as f:
            print("If you want to listen an audio, you should be install agorartc")

if __name__ == '__main__':
    main()