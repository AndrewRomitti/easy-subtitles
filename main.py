from utils import *
from moviepy import CompositeVideoClip, VideoFileClip, AudioFileClip

def create_subtitles(audio_path, video, font_path, output="output/main.mp4"):
    audio = AudioFileClip(audio_path)
    video = VideoFileClip(video).subclipped(0, audio.duration)

    transcribed_text = get_transcribed_text(audio_path)
    text_clips = get_text_clips(transcribed_text, video, font_path)


    main_clip = CompositeVideoClip([video] + text_clips).with_audio(audio)
    main_clip.write_videofile(output)

if __name__ == "__main__":
    create_subtitles(audio_path="C:\\Users\\15732\\Desktop\\Projects\\reel-maker\\audioGen\\audios\\genTextExaggerated.wav", video="C:\\Users\\15732\\Desktop\\Projects\\reel-maker\\MinecraftVids.mp4", font_path="C:\\Users\\15732\\Desktop\\Projects\\reel-maker\\font\\static\\Montserrat-ExtraBold.ttf")