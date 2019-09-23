#module for single video download
from pytube import YouTube
import os
class Single_vid_download():
	def __init__(self,url,downloadfolder="Downloads/",on_progress_callback=None,on_complete_callback=None,isaudio=False):
		self.youtube = YouTube(url,on_progress_callback=on_progress_callback,on_complete_callback=on_complete_callback)
		self.title=self.youtube.title
		self.downloadfolder=downloadfolder
		self.isaudio=isaudio


	def download(self):
		if not os.path.exists(self.downloadfolder):
			os.mkdir(self.downloadfolder)
		self.youtube.streams.filter(only_audio=self.isaudio).first().download(self.downloadfolder)

if __name__ == "__main__":
	pass
	#on_complete