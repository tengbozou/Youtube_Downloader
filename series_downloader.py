from pytube import Playlist
import os

class Series_vid_download:
	def __init__(self, baseurl,downloadfolder="../Downloads/"):
		self.baseurl=baseurl
		self.title = format_filename(Playlist(self.baseurl).title())
		self.downloadfolder=downloadfolder

	def download(self):
		folder = self.downloadfolder+self.series_name
		if not os.path.exists(folder):
			os.mkdir(folder)
		playlist = Playlist(self.baseurl)
		playlist.download_all(folder)


def format_filename(s):

    invalid_chars = "\\/:*?\"<>|"
    filename = ''.join(c for c in s if c not in invalid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    if len(filename)>20:
    	filename = filename[0:20]
    return filename

if __name__ == "__main__":
	pass