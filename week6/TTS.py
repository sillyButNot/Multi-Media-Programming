from gtts import gTTS
import soundfile as sf
from scipy import signal
import playsound

s ="안녕하세요. 반가워요. 제가 도와드릴게 있을까요? "

tts = gTTS(text=s, lang='ko')
tts.save('nice_to_meet_you.wav')

d, fs = sf.read('nice_to_meet_you.wav')
ds = signal.resample(d, int(len(d) * 12 / 24))
sf.write('nice_to_meet_you.wav', ds, 16000)
playsound.playsound('nice_to_meet_you.wav')
