from pytube import *

link=input("Enter youtube link here: ")

vd = YouTube(link)

video= vd.streams.all()

print("Title: ", vd.streams.first().title)

save="C:\\Users\\Extrs\\Desktop"

ques=input("Want to download : Y/N")
ques=ques.upper()

if "Y":
        a=vd.streams.first()
        a.download(save)
        print("Video Downloaded")
        print("Video saved in your Desktop")
        print("Thank You")
elif "N":
        print("Downloading Cancelled")
        
elif:
        print("Wrong input")
