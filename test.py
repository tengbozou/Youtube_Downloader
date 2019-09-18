from pytube import YouTube
from inspect import getsource as gs

url="https://www.youtube.com/watch?v=YTvaiBLkw0U"

def showprogress(stream, chunk, file_handler, bytes_remaining):
	percent = (100*(stream._filesize-bytes_remaining))/stream._filesize

a=YouTube(url,on_progress_callback=showprogress,on_complete_callback=None)
a.streams.first().download()
