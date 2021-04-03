'''
Information

jeongsangsus-iPhone:/var/containers/Bundle/Application/3531FF21-B8A4-444C-A8A7-0CF6604A7719/clubhouse.app root# cat Info.plist | grep -n "KEY"
61:	<key>AMPLITUDE_KEY</key>
71:	<key>TWITTER_KEY</key>
126:	<key>PUBNUB_PUB_KEY</key>
130:	<key>AGORA_KEY</key>
148:	<key>PUBNUB_SUB_KEY</key>
191:	<key>INSTABUG_KEY</key>
'''
import agorartc # RTC

class RTC():
    # Initialization in clubhouse's Info.plist
    AGORA_KEY = "938de3e8055e42b281bb8c6f69c21f78"
    
    #def __init__(self):