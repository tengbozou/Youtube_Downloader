import series_downloader
import single_downloader
import tkinter as tk
from tkinter import filedialog
import json

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.setting()
        self.master = master
        self.pack()
        self.create_widgets()
        
    def setting(self):
        s=open('setting.json','r')
        self.settings=json.loads(s.read())
        s.close()
        self.choice1 = tk.StringVar()
        self.choice1.set(self.settings['choice'])
        self.folder_name=self.settings['folder_name']

    def create_widgets(self):
        self.border_frame=tk.Frame(self.master)
        self.border_frame.pack(padx=40,pady=40)
        self.input_entry_frame()
        self.radio_selection_frame()
        self.downloadfolder_frame()
        self.button_frame()
        
        
        
        

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
        self.radio1 = tk.Radiobutton(self.selection_frame,text="Single Video", variable=self.choice1, value="single")
        self.radio2 = tk.Radiobutton(self.selection_frame,text="List of Videos", variable=self.choice1, value="list")
        self.radio1.pack(side=tk.LEFT)
        self.radio2.pack(side=tk.LEFT)

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

    def input_entry(self):
        pass






    def download(self):
        url = self.input.get()
        self.settings={
            'choice': self.choice1.get(),
            'folder_name': self.folder_name
        }
        s=open('setting.json','w')
        s.write(json.dumps(self.settings))
        s.close()
        if self.choice1.get() == "single":
            single_downloader.Single_vid_download(url,self.folder_name).download()
        else:
            series_downloader.Series_vid_download(url,self.folder_name).download()
    
    # def change_titlelabel(self,event):

    #     url = self.inputurl.get()
    #     print(url)
    #     try:
    #         if self.choice.get() == "single":
    #             title = single_downloader.Single_vid_download(url).title
    #         else:
    #             title = series_downloader.Series_vid_download(url).title
            
    #     except:
    #         title = "Not Valid"
    #     finally:
    #         self.title_label["text"]="title: "+title

    def browse_path(self):
        selected_folder = filedialog.askdirectory()
        if selected_folder!="":
            self.folder_name=selected_folder
            if len(self.folder_name)>30:
                self.label_download_folder['text']=self.folder_name[:15]+" ... "+self.folder_name[-15:]
            else:
                self.label_download_folder['text']=self.folder_name


root = tk.Tk()
root.title('Youtube Downloader')
app = Application(master=root)

app.mainloop()