from __future__ import unicode_literals
from __future__ import print_function
import subprocess
import os
import time
from flask import Flask, render_template, Response, request, send_file,session,Markup,jsonify,url_for
from flask_jsglue import JSGlue
import youtube_dl
import itunes
import re
import logging

app = Flask(__name__)
jsglue = JSGlue(app)


ydl_opts = {
    'writethumbnail':True,
    'format': 'bestaudio/best',
    'outtmpl':'static/downloads/%(id)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    },
    {'key' : 'EmbedThumbnail'},
    {'key' : 'FFmpegMetadata'},
    
    ],
   }

@app.route('/')

def index():
    #link='https://is3-ssl.mzstatic.com/image/thumb/Music20/v4/a0/4a/95/a04a95a8-9c6a-7635-6b81-2b0286118d83/source/600x600bb.jpg'

    link=os.path.join('static','img/add.png')
    #img=Markup('<img src="'+link+'" width="250px" height="250px" class="rounded-circle"\>')
    return render_template('index.html',url=link)
def name():
    return "play.mp3"
     

@app.route('/ytdl')

def i():
 with youtube_dl.YoutubeDL(ydl_opts) as ydl:
     video="https://www.youtube.com/watch?v=MRLyREkZles"
     info_dict = ydl.extract_info(video,None)
     video_title =info_dict.get("title",None)
     video_id=info_dict.get("id",None)
     file_name=video_title+".mp3"
     #output = subprocess.check_output(filename.download([video]))
     #return send_file(file_name, attachment_filename=file_name)
     #ydl_opts["outtmpl"]= video_title
     ydl.download([video])
     
    
 return send_file(file_name,as_attachment= True)


@app.route('/process',methods=['POST'])

def test():

  yt_url=request.values.get("yt_url")
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    video=yt_url
    info_dict = ydl.extract_info(video,None)
    video_title =info_dict.get("title",None)
    video_id=info_dict.get("id",None)
    video_artist=info_dict.get("artist",None)
    #file_name=ydl_opts.outtmpl
    file_name=video_id+".mp3"
    #file_name=file_name.replace(" ", "")
    yt_thumb='https://i.ytimg.com/vi/'+video_id+'/sddefault.jpg'
    #output = subprocess.check_output(filename.download([video]))
    #return send_file(file_name, attachment_filename=file_name)
    #ydl_opts["outtmpl"]= video_title
    ydl.download([video])
 ##############################################################################$$$$
 ##########FILTERATION ALGORITM #################################################################
 #########################################################################@$%%%%%@%@%@%%@%@%@%
    search=re.sub(r'[^\w]',' ',video_title)
    search=re.sub(r'[^\u0000-\u007F]',' ',search)
    search=search.lower()     
    stopwords=['official','video','full','song','latest','hd','lyrical']       
    querywords=search.split()
    resultwords=[word for word in querywords if word.lower() not in stopwords]
    count =len(resultwords)
    i=count+1
    qre=' '.join(resultwords)
  flag=0
  art=""
  while(i!=0 or flag==0):
      i=i-1
      result=qre.split()[:i] 
      print(result)
      if not result:
        break
      qre=' '.join(result)
      videos = itunes.search(query=qre, media='music',limit='1')
      for video in videos:
          art=video.artwork['600']
          apple_artist=re.sub('<Song>: ','',str(video.artist))
          #print(apple_artist)
          apple_track=video.name
      if art!="":
          break    

  #return ('<img src='+art+'/><img src=\"'+yt_thumb+'\"/><br>'+video_id)
  return jsonify({'apple_art' :art,
                  'apple_track' :apple_track,
                  'apple_artist':apple_artist,
                  'yt_art':yt_thumb,
                  'yt_title':video_title,
                  'yt_id':video_id,
                  'yt_artist':video_artist,
                  'file_name':file_name})
  return render_template('index.html');
@app.route('/ajax',methods=['POST'])
  
def fun():
 yt_thumb = request.values.get("yt_url")
 return jsonify({'url' :yt_thumb})

if __name__ == "_main_":
     app.run(debug=True)
     