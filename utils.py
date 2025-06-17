import whisper
from moviepy import TextClip, ColorClip, CompositeVideoClip
from moviepy.video.fx import Margin

def get_transcribed_text(filename):
    audio = whisper.load_audio(filename)
    model = whisper.load_model('small', device='cpu')
    result = whisper.transcribe(model, audio, language="en", word_timestamps=True)

    return result

def get_text_clips(text, clip, font_path, align, delay=0):
    text_clip_array = []

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
                method="caption",
                size=(clip.w, 200)
            )

            padding_v, padding_h = 10, 20
            bg = ColorClip(
                size=(txt.w + 2 * padding_h, txt.h + 2 * padding_v),
                color=(0, 0, 0),
            ).with_opacity(0)

            padded = CompositeVideoClip([bg.with_duration(txt.duration), txt.with_position(("center", "center"))])
            padded = padded.with_start(start).with_end(end).with_position(("center", align))

            text_clip_array.append(padded)

    return text_clip_array