from moviepy import VideoFileClip

def convert_mp4_to_mp3(mp4_path, mp3_path):
    video = VideoFileClip(mp4_path)
    audio = video.audio
    audio.write_audiofile(mp3_path)

mp4_file = "input.MP4"  # MP4 dosyanın adı
mp3_file = "output.mp3"  # Çıkacak MP3 dosyanın adı

convert_mp4_to_mp3(mp4_file, mp3_file)