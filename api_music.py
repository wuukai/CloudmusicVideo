import requests,json,re

def Getid(name):
    djson={}
    url="http://musicapi.leanapp.cn/search?keywords={}".format(name)
    res=requests.get(url).json()['result']['songs']
    l=len(res)
    for i in range(l):
        djson[i] ={'名称':str(res[i]['name']),'作者:': str(res[i]['artists'][0]['name']), 'id:': str(res[i]['id'])}
    return djson
    


# s=Getid('可乐')
# for i in range(len(s)):
#     print(s[i])

def Getcomment_json(id):
    clist=[]
    url="http://musicapi.leanapp.cn/comment/music?id={}&limit=1".format(id)
    res=requests.get(url).json()['hotComments']
    l=len(res)
    for i in range(l):
        str2=str(res[i]['content'])
        res2 = ''.join(re.findall('[0-9\u4e00-\u9fa5]',str2))
        clist.append(res2)
    return clist



def Getcomment_read_text(id):
    str1=''
    a=Getcomment_json(id)
    l=len(a)
    for i in range (l):
        str1=str1+a[i]
    return str1

a=Getcomment_read_text('1443022767')
# print(a)
# print(Getid('丢了你'))
#print(Getcomment_json('1443022767'))