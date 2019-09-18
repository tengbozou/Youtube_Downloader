from pytube import YouTube
class Single_vid_download():
	def __init__(self,url,downloadfolder="../Downloads/",on_progress_callback=None):
		self.url=url
		self.title=YouTube(self.url).title
		self.downloadfolder=downloadfolder
		self.on_progress_callback=on_progress_callback

	def download(self):
		baseurl = self.url
		youtube = YouTube(baseurl,on_progress_callback=self.on_progress_callback)
		youtube.streams.first().download(self.downloadfolder)

if __name__ == "__main__":
	pass