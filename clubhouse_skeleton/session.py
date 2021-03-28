# Q : How can I handle user session easily?
# A : Parse XML 

from xml.etree.ElementTree import Element, SubElement, ElementTree
from lxml import etree
import datetime as pydatetime


class Session():
    user_id = ''
    auth_token = ''
    device_id = ''
    filename = 'user_session.xml'

    def get_now(self):
        return pydatetime.datetime.now()

    def get_now_timestamp(self):
        return self.get_now().timestamp()

    '''
    <?xml version="1.0" encoding="UTF-8"?>
    '''
    def create_session(self):
        root = Element('ClubHouse')
        SubElement(root,'Author').text = 'Sangsoo Jeong'
        SubElement(root,'Time Stamp').text = str(self.get_now_timestamp())
        SubElement(root,'')
        tree = ElementTree(root)
        tree.write('./' + self.filename, pretty_print=True )


    def check_session(self):
        test = ''

    