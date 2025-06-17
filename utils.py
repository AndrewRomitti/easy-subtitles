import whisper
from moviepy import TextClip
from moviepy.video.fx import Margin

def get_transcribed_text(filename):
    audio = whisper.load_audio(filename)
    model = whisper.load_model('small', device='cpu')
    result = whisper.transcribe(model, audio, language="en", word_timestamps=True)

    return result

def get_text_clips(text, clip, font_path, delay=0):
    text_clip_array = []

    margin = Margin(20)

    segments = text["segments"]
    for segment in segments:
        for word in segment["words"]:
            if word["start"] < delay:
                continue

            start, end, w = word["start"], word["end"], word["word"]

            txt = TextClip(
                text=w,
                font_size=70,
                stroke_color="black",
                stroke_width=5,
                color="white",
                font=font_path,
                method="label",
            )

            txt = Margin(left=20, right=20, top=20, bottom=20, color=(0, 0, 0), opacity=0).apply(txt)

            txt = (txt
                   .with_start(start)
                   .with_end(end)
                   .with_position(("center", "bottom"))
                  )

            text_clip_array.append(txt)

    return text_clip_array