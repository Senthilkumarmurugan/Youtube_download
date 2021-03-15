import streamlit as st 
from pytube import YouTube
import streamfunc


st.markdown("<h1 style='text-align: center; color: red;'>Youtube Downloader</h1>", unsafe_allow_html=True)

youtube_url=st.text_input("Paste the URL")

if youtube_url!="":
    #I/P-->Youtube URL O/P-->Streams
    streams=streamfunc.stream(url=youtube_url)
    
    #I/P-->Streams O/P-->Video/Audio Resolutions
    Videos,Audios=streamfunc.video_audio(streams)
    
    #Asking the user to choose Video or Audio of the File
    Download_type=st.selectbox('Select the Download Type',['Video','Audio'])
    
    #I/P-->Download_type,Resolution O/P-->Resolution of the video to be downloaded
    resolution,file_size=streamfunc.find_resolution(d_type=Download_type,streams=streams,videos=Videos,audios=Audios) 
    
    #Asking the user to enter the filename
    Filename=st.text_input("Enter the Filename:")
    
    #Checking the filename empty or not
    if Filename !="":
        if st.button("Download"):
            #downloading the file
            streamfunc.download(file=Filename,res=resolution)
    else:
        st.error("Please enter the file name")
else:
        st.error("Please paste the Url and hit enter")
    
