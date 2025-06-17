from utils import *
from moviepy import CompositeVideoClip

def create_subtitles(audio, video, output="main.mp4"):
    transcribed_text = get_transcribed_text(audio)
    text_clips = get_text_clips(transcribed_text)

    main_clip = CompositeVideoClip([video] + text_clips)
    main_clip.write_videofile(output)