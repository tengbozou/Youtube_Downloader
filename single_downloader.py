#module for single video download
from pytube import YouTube
class Single_vid_download():
	def __init__(self,url,downloadfolder="../Downloads/",on_progress_callback=None,isaudio=False):
		self.url=url
		self.title=YouTube(self.url).title
		self.downloadfolder=downloadfolder
		self.on_progress_callback=on_progress_callback
		self.isaudio = isaudio

	def download(self):
		baseurl = self.url
		youtube = YouTube(baseurl,on_progress_callback=self.on_progress_callback)
		if self.isaudio:
			youtube.streams.filter(only_audio=self.isaudio).first().download(self.downloadfolder)
		else:
			youtube.streams.first().download(self.downloadfolder)

if __name__ == "__main__":
	pass