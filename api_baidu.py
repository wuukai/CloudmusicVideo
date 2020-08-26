import requests
from download import download
import time
import os



def api_to_access_token(api_key,api_secret):
        url='https://aip.baidubce.com/oauth/2.0/token'
        data={'grant_type':'client_credentials','client_id':api_key,'client_secret':api_secret}
        global access_token
        access_token=requests.post(url,data=data).json()['access_token']
        return access_token


def baidu_voice_speaker(word,stu):
    api_key='##############'
    api_secret='##############‘
    api_to_access_token(api_key,api_secret) 
    tex = word
    cuid='0000'
    ctp='1'
    lan='zh'
    spd='3'
    per='3'
    pit='4'
    vol='10'
    url='http://tsn.baidu.com/text2audio?tex={}&tok={}&cuid={}&ctp={}&lan={}&spd={}&aue={}&per={}&pit={}&vol={}'.format(tex,access_token,cuid,ctp,lan,spd,'6',per,pit,vol)
    download(url,'process/zimu.wav')
    if stu== 1 :
        pass
    else:
        pass


