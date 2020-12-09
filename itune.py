from __future__ import print_function
import itunes
import re


# Search album artItunes and Meta Data
# videos = itunes.search(query='eminem lose yourself', media='music',limit='1')
# for video in videos:
    #print video.get_name(), video.get_preview_url(), video.get_artwork()
    #print(videos[0])
    #print(video.artwork)
    # print(video.artwork['600'],video.name,video.duration,video.artist,video.url)

# Search band U2
# artist = itunes.search_artist('u2')[0]
# for album in artist.get_albums():
#     for track in album.get_tracks():
#         print(album.name, album.url, track.name, track.duration, track.preview_url)

video_title="'Tu Hai Ki Nahi' FULL VIDEO Song | Roy | Ankit Tiwari | Ranbir Kapoor, Jacqueline Fernandez, Tseries"
print(video_title)
search=re.sub(r'[^\w]',' ',video_title) 
print(search)    
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
    qre=' '.join(result) 
    q=' '.join(result) 
    videos = itunes.search(query=qre, media='music',limit='1')
    for video in videos:
        art=video.artwork['600'] 
        #print(video)
    if art!="":
        print(art)
        break    

    
        

