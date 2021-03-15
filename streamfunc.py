import streamlit as st 
from pytube import YouTube



def stream(url:str):
    try:
        yt=YouTube(url)
    except Exception as e:
        st.exception(e)
    streams=yt.streams.all()
    return streams
    
def video_audio(streams)->dict:
    Videos={}
    Audios={}
    for i,stream in enumerate(streams):
        if stream.type=="video":
            Videos[f'{stream.resolution} {stream.subtype}']=i
        elif stream.type=="audio":
            Audios[stream.subtype]=i
    return Videos,Audios
    
        
def find_resolution(d_type:str,streams,videos,audios):
    if d_type=="Video": 
        Videos_resolution=st.selectbox('Select the resolution', list(videos.keys()))
        resolution=streams[videos[Videos_resolution]]
    elif d_type=="Audio":
        Audio_resolution=st.selectbox('Select the resolution', list(audios.keys()))
        resolution=streams[audios[Audio_resolution]]
    return resolution,resolution.filesize
    
def download(file:str,res):
    progress=st.text("Video Downloading...")
    progress_bar = st.progress(0)
    try:
        d=res.download(filename=file)
        if d:
            st.success(f"Successfully Downloaded at Location: {d}")
            progress_bar.progress(100)
            progress.text("Downloaded")
    except:  
        st.error("Some Error happened while downloading the video !")