from moviepy.editor import  VideoFileClip

video = VideoFileClip(r"C:\Users\Samiullah\Videos\Vaaste_Song_Dhvani_Bhanushali,_Tanishk_Bagchi_Nikhil_D_Bhushan_Kumar_Radhika_Rao,_Vinay_Sapru(360p).mp4").subclip(00,10)

video.write_gif("ayz.gif")

