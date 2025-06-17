from utils import *
from moviepy import CompositeVideoClip, VideoFileClip

def create_subtitles(audio, video, output="main.mp4"):
    video = VideoFileClip(video).subclipped(0, audio.duration)

    transcribed_text = get_transcribed_text(audio)
    text_clips = get_text_clips(transcribed_text, video)


    main_clip = CompositeVideoClip([video] + text_clips)
    main_clip.write_videofile(output)

if __name__ == "__main__":
    create_subtitles(audio="C:\\Users\\15732\\Desktop\\Projects\\reel-maker\\audioGen\\audios\\genTextExaggerated.wav", video="C:\\Users\\15732\\Desktop\\Projects\\reel-maker\\MinecraftVids.mp4")