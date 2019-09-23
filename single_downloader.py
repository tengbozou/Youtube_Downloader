#module for single video download
from pytube import YouTube
import os
from series_downloader import format_filename
class Single_vid_download():
	def __init__(self,url,downloadfolder="Downloads/",on_progress_callback=None,on_complete_callback=None,isaudio=False):
		self.youtube = YouTube(url,on_progress_callback=on_progress_callback,on_complete_callback=on_complete_callback)
		self.title=self.youtube.title
		self.downloadfolder=downloadfolder
		self.isaudio=isaudio


	def download(self,withcaption=False):
		if not os.path.exists(self.downloadfolder):
			os.mkdir(self.downloadfolder)
		self.youtube.streams.filter(only_audio=self.isaudio).first().download(self.downloadfolder)
		if withcaption:
			caption = self.youtube.captions.get_by_language_code('en')
			srt = caption.generate_srt_captions()
			file = format_filename(self.title) + ".srt"
			f_name = os.path.join(self.downloadfolder,file)
			print(f_name)
			f = open(f_name,'w')
			f.write(srt)
			f.close()


if __name__ == "__main__":
	pass