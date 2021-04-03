# Q : How can I handle user session easily?
# A : Parse XML 

from xml.etree.ElementTree import parse
from xml.etree.ElementTree import Element, SubElement, ElementTree
import datetime as pydatetime


class Session():
    USERID = 0
    NAME = 1
    USERNAME = 2
    AUTH_TOKEN = 3
    REFRESH_TOKEN = 4
    ACCESS_TOKEN  = 5
    
    user_id = ''
    auth_token = ''
    device_id = ''
    filename = 'user_session.xml'

    def get_now(self):
        return pydatetime.datetime.now()

    def get_now_timestamp(self):
        return self.get_now().timestamp()

    def get_session(self):
        tree = parse(f'{self.filename}')
        root = tree.getroot()
        phone = root.findtext('PhoneNumber')
        sid = root.findtext('user_sid')
        name = root.findtext('name')
        nickname = root.findtext('username')
        auth_token = root.findtext('auth_token')
        cloudflare_cookie = root.findtext('cloudflare_cookie')
        
        print(f"phone = {phone}")
        print(f"sid = {sid}")
        return phone,sid,name,nickname,auth_token,cloudflare_cookie

        #tree = parse(f'test.xml')

        

    '''
    <?xml version="1.0" encoding="UTF-8"?>
    '''
    def create_session(self, phone_number,VALID_USER_INFO,cloudflare_cookie):
        #print(f"session check = {auth_token}")
        root = Element('ClubHouse')
        SubElement(root,'Author').text = 'Sangsoo Jeong'
        SubElement(root,'TimeStamp').text = str(self.get_now_timestamp())
        SubElement(root,'PhoneNumber').text = str(phone_number)
        SubElement(root,'user_sid').text = str(VALID_USER_INFO[self.USERID])
        SubElement(root,'name').text = str(VALID_USER_INFO[self.NAME])
        SubElement(root,'username').text = str(VALID_USER_INFO[self.USERNAME])
        SubElement(root,'auth_token').text = str(VALID_USER_INFO[self.AUTH_TOKEN])
        SubElement(root,'cloudflare_cookie').text = str(cloudflare_cookie)
        tree = ElementTree(root)
        tree.write('./' + self.filename)


    def check_session(self):
        test = ''

    