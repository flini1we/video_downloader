from pytube import YouTube
link= input("https://www.youtube.com/watch?v=hkrmyIecHR0")
video= YouTube(link)
stream= video.streams.get_highest_resolution()
stream.download