from pytube import YouTube
class Single_vid_download():
	def __init__(self,url,downloadfolder="../Downloads/"):
		self.url=url
		self.title=YouTube(self.url).title
		self.downloadfolder=downloadfolder

	def download(self):
		baseurl = self.url
		youtube = YouTube(baseurl)
		youtube.streams.first().download(self.downloadfolder)

if __name__ == "__main__":
	pass