#module for list of videos download
from pytube import Playlist
import os

class Series_vid_download:
	def __init__(self, baseurl,downloadfolder="../Downloads/",on_progress_callback=None,on_complete_callback=None,isaudio=False):
		self.baseurl=baseurl
		self.playlist = Playlist(self.baseurl,on_progress_callback=on_progress_callback,on_complete_callback=on_complete_callback,isaudio=isaudio)
		if self.playlist.title():
			self.title = format_filename(self.playlist.title())
		else:
			self.title = format_filename(self.baseurl)
		self.downloadfolder=downloadfolder


	def download(self):
		folder = self.downloadfolder+self.title
		if not os.path.exists(folder):
			os.mkdir(folder)
		
		self.playlist.download_all(folder)


def format_filename(s):

    invalid_chars = "\\/:*?\"<>|"
    filename = ''.join(c for c in s if c not in invalid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    if len(filename)>20:
    	filename = filename[0:20]
    return filename

if __name__ == "__main__":
	a=Series_vid_download("https://www.youtube.com/watch?v=M8Uur3OyJD8&list=RDYqeW9_5kURI")
	a.download()