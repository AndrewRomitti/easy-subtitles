import whisper
from moviepy import TextClip

def get_transcribed_text(filename):
    audio = whisper.load_audio(filename)
    model = whisper.load_model('small', device='cpu')
    result = whisper.transcribe(model, audio, language="en", word_timestamps=True)

    return result

def get_text_clips(text, clip, font_path, delay=0):
    text_clip_array = []

    segments = text["segments"]
    for segment in segments:
        for word in segment["words"]:
            if word["start"] < delay:
                continue

            start = word["start"]
            end = word["end"]
            text_clip_array.append(
                TextClip(
                    text=word["word"],
                    font_size=70,
                    stroke_color="black",
                    stroke_width=5,
                    color="white",
                    font=font_path,
                    method="caption",
                    size=(clip.w, clip.h),
                ).with_start(start)
                .with_end(end)
                .with_position("center")
            )

    return text_clip_array