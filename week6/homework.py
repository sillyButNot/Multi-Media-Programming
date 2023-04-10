from gtts import gTTS
import soundfile as sf
from scipy import signal
import playsound
import numpy as np
import pyaudio
from scipy.io import wavfile
import speech_recognition as sr
import keyboard

RATE = 16000
CHUNK = RATE * 5

playsound.playsound('start.wav')  # 말씀해주세요 듣고 있어요
print("말씀해주세요. 듣고 있어요.")
answer = False
r = sr.Recognizer()

while True:
    key_ = input("시작하려면 s를 눌러주세요 (종료를 원하면 q를 눌러주세요) : ")

    if key_ == 'q':
        print("종료합니다.")
        break
    if key_ == 's':
        answer = False
        print("Speak for 5 sec")
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK,
                        input_device_index=0)
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        wavfile.write('answer.wav', RATE, data.astype(np.int16))
        wavr = sr.AudioFile('answer.wav')
        answer = ''
        with wavr as source:
            try:
                audio = r.record(source)
                answer = r.recognize_google(audio, language='ko-KR')
                print(answer)
            except sr.UnknownValueError:
                # ignore the exception and do nothing
                pass

        if '안녕' in answer:
            playsound.playsound('nice_to_meet_you.wav')
            print("안녕하세요. 반가워요. 제가 도와드릴게 있을까요?")

        if '자동차' in answer and '영어' in answer:  # 자동차가 영어로 뭐야?
            playsound.playsound('answer2.wav')  # 자동차는 영어로
            playsound.playsound('answer2-1.wav')  # car
            playsound.playsound('answer2-2.wav')  # 입니다.
            print("자동차는 영어로 car 입니다.")

        if '자동차' in answer and '프랑스어' in answer:  # 자동차가 프랑스어로 뭐야?
            playsound.playsound('answer_fr_1.wav')
            playsound.playsound('answer_fr_2.wav')
            playsound.playsound('answer2-2.wav')
            print("자동차는 프랑스어로 voiture 입니다.")

        if '자동차' in answer and '독일어' in answer:  # 자동차가 독일어로 뭐야?
            playsound.playsound('answer_de_1.wav')
            playsound.playsound('answer_de_2.wav')
            playsound.playsound('answer2-2.wav')
            print("자동차는 독일어로 Automobil입니다.")

        if '날씨' in answer and '오늘' in answer:
            playsound.playsound('sunny.wav')
            print("오늘 하루는 날씨가 맑아요. 자외선이 쎄니 햇빛에 유의하세요")

        if '날씨' in answer and '내일' in answer:
            playsound.playsound('rain.wav')
            print("내일은 비가 많이 와요. 우산을 챙기세요")

        if '심심해' in answer:
            playsound.playsound('board.wav')
            print("영화나 만화책을 보시는 것을 추천해드릴게요")

        if answer == '':
            playsound.playsound('re_answer.wav')
            print("잘 이해하지 못했어요. 다시 말씀해주세요")
