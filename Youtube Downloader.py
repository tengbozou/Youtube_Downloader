#this app is based on module "pytube"
#however, pytube has been done some ajustment for this app.
import pytube
#import other modules
import series_downloader
import single_downloader
import tkinter as tk
from tkinter import filedialog
import json
import threading

# GUI design
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.setting()
        self.master = master
        self.pack()
        self.create_widgets()
        
        # the widget containing several frames
    def create_widgets(self):
        #this frame is to implement a margin of the gui
        self.border_frame=tk.Frame(self.master)
        self.border_frame.pack(padx=40,pady=40)
        #other frames inside border_frame
        self.input_entry_frame()
        self.radio_selection_frame()
        self.downloadfolder_frame()
        self.button_frame()
        self.download_status_frame()
        
        
        
        

    def input_entry_frame(self):
        #input entry
        self.input_frame = tk.Frame(self.border_frame)
        self.input_frame.pack()
        self.urllabel = tk.Label(self.input_frame,text="URL:")
        self.urllabel.pack(side=tk.LEFT)
        self.inputurl=tk.StringVar()
        self.input = tk.Entry(self.input_frame,textvariable=self.inputurl,width=40)
        self.input.pack(padx=10,pady=10)
        self.input.focus()

    def content_detail_frame(self):
        #content detail frame
        self.content_frame = tk.Frame(self.border_frame)
        self.content_frame.pack(side=tk.TOP,fill=tk.X)
        self.title_label = tk.Label(self.content_frame,text="title: ")
        self.title_label.pack(side=tk.LEFT,fill=tk.X)

    def radio_selection_frame(self):
        #radio selection_frame
        self.selection_frame = tk.Frame(self.border_frame)
        self.selection_frame.pack()
        self.radio1 = tk.Radiobutton(self.selection_frame,text="Single", variable=self.choice1, value="single")
        self.radio2 = tk.Radiobutton(self.selection_frame,text="List", variable=self.choice1, value="list")
        self.radio1.pack(side=tk.LEFT)
        self.radio2.pack(side=tk.LEFT)
        
        self.audioonly = tk.Checkbutton(self.selection_frame,text="Audio Only",variable=self.isaudio)
        self.audioonly.pack(side=tk.RIGHT,padx=30)

    def downloadfolder_frame(self):
        #download_path
        self.download_folder_choose = tk.Frame(self.border_frame)
        self.download_folder_choose.pack(fill=tk.X)
        self.label_download_folder = tk.Label(self.download_folder_choose,text=self.folder_name)
        self.label_download_folder.pack(side=tk.LEFT,fill=tk.X)
        #buttontoselect
        self.path_select_folder=tk.Button(self.download_folder_choose,text="Path",command=self.browse_path)
        self.path_select_folder.pack(side=tk.RIGHT)
    def button_frame(self):
        #button
        self.button_frame = tk.Frame(self.border_frame)
        self.button_frame.pack()
        self.download_button = tk.Button(self.button_frame,text="Download",command=self.download)
        self.download_button.pack(side=tk.LEFT)

    def download_status_frame(self):
        #download INFO
        self.download_status_frame = tk.Frame(self.border_frame)
        self.download_status_frame.pack(pady=10)


    def thread4download(self):
        #whenever press the download button, a thread is created
        self.url = self.input.get()
        self.create_task_info_frame()
        try:
            if self.choice1.get() == "single":
                single_downloader.Single_vid_download(self.url,self.folder_name,
                    on_progress_callback=self.on_progress_single,
                    on_complete_callback=self.on_complete_single,
                    isaudio=self.isaudio.get()).download()
            else:
                series_downloader.Series_vid_download(self.url,self.folder_name,
                    on_progress_callback=self.on_progress_list,
                    on_complete_callback=self.on_complete_list,
                    isaudio=self.isaudio.get()).download()        
        except Exception as e:
            self.downloadpercentage['text']="failed: " + str(e)
            self.downloadpercentage['fg']="red"
            raise

    def create_task_info_frame(self):
        #when a thread start, create a frame to show its info
        self.oneiteminfo=tk.Frame(self.download_status_frame)
        self.oneiteminfo.pack(side=tk.BOTTOM)
        self.file_title = tk.Label(self.oneiteminfo, text="")
        self.file_title.pack(side=tk.LEFT,padx=10)
        self.urllabelinfo = tk.Label(self.oneiteminfo,text=self.url)
        self.urllabelinfo.pack(side=tk.LEFT,padx=10)

        self.downloadpercentage = tk.Label(self.oneiteminfo,text="downloading",fg="blue")
        self.downloadpercentage.pack(side=tk.RIGHT,padx=10)        

#when a downloading task/thread is created, change the info of downloading status\
#by the following two functions, one for single, one for list
    def on_progress_single(self, stream, chunk, file_handler, bytes_remaining): 
        self.file_title["text"]=stream.player_config_args['title']
        self.downloadpercentage['text']="downloading {:.1f}%".format((100*(stream._filesize-bytes_remaining))/stream._filesize)

    def on_progress_list(self,progress_message):
        self.downloadpercentage['text']=progress_message

    def on_complete_single(self,stream,file_handle):
        self.downloadpercentage['text']="completed"
        self.downloadpercentage['fg']="green"

    def on_complete_list(self):
        self.downloadpercentage['text']="completed"
        self.downloadpercentage['fg']="green"
    



    def download(self):
        # button download's callback function
        self.savesetting()
        t = threading.Thread(target=self.thread4download)
        t.start()




    


    def browse_path(self):
        # callback function of button path, choose the destination download folder
        selected_folder = filedialog.askdirectory()
        if selected_folder!="":
            self.folder_name=selected_folder
            if len(self.folder_name)>30:
                self.label_download_folder['text']=self.folder_name[:15]+" ... "+self.folder_name[-15:]
            else:
                self.label_download_folder['text']=self.folder_name

    def setting(self):
        #function to get setting from setting.json
        s=open('setting.json','r')
        self.settings=json.loads(s.read())
        if self.settings=={}:
            self.settings={"choice": "single", "folder_name": "../Downloads", "isaudio": False}
        s.close()
        self.choice1 = tk.StringVar()
        self.choice1.set(self.settings['choice'])
        self.isaudio = tk.BooleanVar()
        self.isaudio.set(self.settings['isaudio'])
        self.folder_name=self.settings['folder_name']

    def savesetting(self):
        #function to store setting to setting.json
        self.settings={
            'choice': self.choice1.get(),
            'folder_name': self.folder_name,
            'isaudio': self.isaudio.get(),
        }
        s=open('setting.json','w')
        s.write(json.dumps(self.settings))
        s.close()



root = tk.Tk()
root.title('Youtube Downloader')
app = Application(master=root)

app.mainloop()