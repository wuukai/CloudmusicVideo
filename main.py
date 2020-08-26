from api_baidu import baidu_voice_speaker
from api_music import Getcomment_read_text,Getcomment_json
from getstr import encoding_text
import ffmpeg
import os,time,subprocess


comment_id='1398663411'             #网易云评论ID
video_file='video1.mp4'             #视频路径
music_file='music2.mp3'             #音频路径
#1443022767



text=Getcomment_read_text(comment_id)
text_json=Getcomment_json(comment_id)
print("评论文本获取")
# print(text_json)
baidu_voice_speaker(text,0)
print("评论朗读已生成,process/zimu.wav")
result=os.popen("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 -i process/zimu.wav")
res = result.read()  
for line in res.splitlines():  
    tim=str(line)
encoding_text(text_json,text,tim)
print("评论字幕已生成,process/zimu.srt")

os.system('ffmpeg -i {} -vn -acodec copy -ss 0 -t {}  process/music_out.mp3'.format(music_file,tim))
os.system('ffmpeg -i process/zimu.wav -i process/music_out.mp3 -filter_complex amerge -ac 2 -c:a libmp3lame -q:a 4 process/yingping.mp3')
print('音频已生成')

os.system('ffmpeg -t {} -i {} -vcodec copy -acodec copy process/video_out.mp4'.format(tim,video_file))
os.system('ffmpeg -i process/video_out.mp4 -c:v copy -an process/no-audio.mp4')
os.system('ffmpeg  -i process/no-audio.mp4 -i process/yingping.mp3 -vf subtitles=process/zimu.srt -y output.mp4')



