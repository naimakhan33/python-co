from moviepy.editor import VideoFileClip

video = VideoFileClip(r"C:\Users\Samiullah\Videos\Vaaste_Song_Dhvani_Bhanushali,_Tanishk_Bagchi_Nikhil_D_Bhushan_Kumar_Radhika_Rao,_Vinay_Sapru(360p).mp4")

video.audio.write_audiofile(r"demo.txt.mp3")

print("Audio extracted successfully!")

