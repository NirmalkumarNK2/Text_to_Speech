from gtts import gTTS
from moviepy.editor import *

text = "hi my name is artificial intelligence and how are you."
language = 'en'  

tts = gTTS(text=text, lang=language, slow=False)
audio_file = "audio.mp3"
tts.save(audio_file)

audio = AudioFileClip(audio_file)

duration = audio.duration  
video = ColorClip(size=(640, 480), color=(255, 255, 255), duration=duration)  
video = video.set_audio(audio)

text_clip = TextClip(text, fontsize=24, color='black', size=video.size)
text_clip = text_clip.set_position('center').set_duration(duration)
final_video = CompositeVideoClip([video, text_clip])

output_file = "text_to_video.mp4"
final_video.write_videofile(output_file, fps=24, codec="libx264")

print("Video created successfully!")
