from pytube import YouTube   # install pytube library before using: in cmd run command "pip install pytube"
from sys import argv

vid_link = argv[1]  # gets the vid link from the terminal, argv being the array containing all the strings in the command, argv[1] being the link to the video
yt = YouTube(vid_link)  # creates a YouTube object with the passed link
vid = yt.streams.get_highest_resolution()   # gets the highest possible reolution for the video, could be changed
vid.download('C:\\Users\\Ali Ammar\\Videos\\Youtube Downloads') # downloads the video to the specifeid path, change it to the desired location