from __future__ import unicode_literals
import subprocess
import os
import time
from flask import Flask, render_template, Response, request, send_file,session
import youtube_dl
app = Flask(__name__)


ydl_opts = {
    'writethumbnail':True,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    },
    {'key' : 'EmbedThumbnail'},
    {'key' : 'FFmpegMetadata'},
    
    ],
   }

def kill():
    session.clear()




@app.route('/')

def index():
 with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     video="https://www.youtube.com/watch?v=VPRjCeoBqrI"
     info_dict = ydl.extract_info(video,None)
     video_title =info_dict.get("title",None)
     video_id=info_dict.get("id",None)
     file_name=video_title+"-"+video_id+".mp3"
     #output = subprocess.check_output(filename.download([video]))
     #return send_file(file_name, attachment_filename=file_name)
     #ydl_opts["outtmpl"]= video_title
     ydl.download([video])
     
    
 return send_file(file_name,as_attachment= True)

     