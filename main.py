import tkinter
import customtkinter
from pytube import YouTube

def startDownload (): 
    try:
       ytLink=link.get() 
       ytObject= YouTube(ytLink, on_progress_callback=on_progress)
       video= ytObject.streams.get_highest_resolution() 
       video.download() 

       title.configure(text=ytObject.title,text_color="black")  
       finsishLabel.configure("") 
       finsishLabel.configure(text="Download Completed!!")
    except :
        finsishLabel.configure(text="Link is invalid",text_color="red") 


def on_progress(stream,chunk,bytes_remaining):
    total_size=stream.filesize 
    byes_downloaded= total_size- bytes_remaining
    percent_of_completion= byes_downloaded/ total_size*100
    per = str(int(percent_of_completion)) 
    pPercentage.configure(text= per+ " %")
    pPercentage.update() 

    #update the progress bar
    progressBar.set(float(percent_of_completion/100)) #because we need  float value between 0 and 1  
        
#system settings 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue") 

#app frame
app= customtkinter.CTk() #initialisation
app.geometry("720x480") #dimensions
app.title("Youtube Downloader by supro") 

#adding ui 
title=customtkinter.CTkLabel(app, text=" Insert a Youtube Link ")
title.pack(padx=10, pady=10) 

#link input
url_var= tkinter.StringVar()
link=customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack() 

#finished downloading 
finsishLabel= customtkinter.CTkLabel(app, text="")
finsishLabel.pack()

#progress percentage 
pPercentage= customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar= customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0) # progress bar goes from 0-1
progressBar.pack(padx=10, pady=10)

#download button 
download =customtkinter.CTkButton(app,text="Download", command=startDownload)
download.pack(padx=10,pady=10) 

#run app
app.mainloop() 