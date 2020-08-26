import time,datetime

aa=['这突如其来的难过差点要了我半条命', '玫瑰花腐烂的味道比野草还难闻它盛开的时候你可不是这样说的', '有谁知道我多难心碎心碎', '这世界这么多人哪来两个人一模一样的情感感同身受安慰人罢了', '我恨我的五官我的四肢我的青春痘我的囊肿我的黑头我还恨我的性格不合时宜的暴躁常态化的软弱毫无用处的无能狂怒伤害所爱的人时的肆无忌惮我恨我的作息规律我恨我的饮食习惯我恨我的穿衣打扮我恨我的言行举止我恨我所存在的世界我恨我所存在的时间我恨你喜欢她', '我有对象了高二谈的不是随便玩玩很认真认真到这辈子就他了他叫贺朝', '不要复制粘贴别人的情绪', '根本就没有感同身受', '感同身受什么的都是温柔的谎言吧', '别哭没有感同身受谁又会为你抹掉眼泪', '如果歌词滚动了记住里面有我的1积分', '要了你半条命的那句话是什么', '这世上没有感同身受的人你讲的是心事别人听的是故事', '小建议不能感同身受就保持沉默', '兄弟萌把好听打在公屏上']



strTime = '00:00:00.000'  
startTime = datetime.datetime.strptime(strTime, "%H:%M:%S.%f")
abb=0
t=0

def clean():
    f = open('process/zimu.srt','w+',encoding='utf-8')
    f.close()

def bud_srt(word):
    f = open('process/zimu.srt','a+',encoding='utf-8')
    global startTime,abb,t
    l=len(word)
    t1=t
    t2=t+l*timee
    startTime1 = (startTime + datetime.timedelta(seconds=t1)).strftime("%H:%M:%S.%f")[:-3]
    startTime2 = (startTime + datetime.timedelta(seconds=t2)).strftime("%H:%M:%S.%f")[:-3]
    msg='\n\n'+str(abb)+'\n'+str(startTime1)+' --> '+str(startTime2)+'\n'+str(word)
    abb=abb+1
    t=t2
    f.write(msg)
    f.close()

def encoding_text(aa,aa_txt,t11):
    clean()
    zishu=len(aa_txt)
    global timee
    timee=float(t11)/float(zishu)
    print(timee)
    for i in range(len(aa)):
        word=aa[i]
        l1=len(word)
        list1=[]    
        if l1 >=10 :
            yu=l1%10
            l2=l1//10
            if yu==1 or yu==2:
                xx=l2-1
                if xx<=0:
                    pass
                else:
                    for i in range(xx):
                            op=i*10
                            ed=op+10
                            data=word[op:ed] 
                            list1.append(data)
                op=(xx)*10
                ed=l1
                data=word[op:ed] 
                list1.append(data)                
            else:
                for i in range(l2+1):
                        op=i*10
                        ed=op+10
                        data=word[op:ed] 
                        list1.append(data)
        else:
            list1.append(word)

        # print(list1)
        l4=len(list1)
        for i in range (l4):
            bud_srt(list1[i])



# encoding_text(aa)