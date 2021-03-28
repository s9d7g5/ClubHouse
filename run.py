# ClubHouse Running
import requests
import sys
from clubhouse_skeleton import clubhouse

def main():
    DEBUG = True 

    print("CLUBHOUSE")
    client = clubhouse.ClubHouse()
    
    init_header = client.User_First_Access()
    
    if init_header.status_code != 200:
        print("Could you check your Request Header?")
        sys.exit(0)

    cloudflare_cookie = client.Get_User_Header(init_header)['Set-Cookie'].split(";")[0].split("__cfduid=")[1]
    print(cloudflare_cookie) # set Cookie

    if not DEBUG:
        phone_number = input("[+] Please enter your phone number  > ")
    else:
        phone_number = "+6598712847"
    
        if (client.Authentication(cloudflare_cookie, phone_number)):
            verify_code = input("[+] Please enter your verification code  > ")
        
            if(client.Send_Verification_Code(phone_number, verify_code)):
                client.Comming_Lobby() # PopUp bypass
            # get_online_friend API : up to you
                client.Get_ME()
                client.Show_Channel_List()

if __name__ == '__main__':
    main()
