
# https://pypi.org/project/speech-recognition-fork/ справка по распознованию голоса


import playsound #аудио
import gtts # google text to speech
import os #операционная система
import speech_recognition as sr #распознавание речи с микрофона


def user_input(): #ввод запроса
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source: #микрофон захвачен
        voice_recognizer.adjust_for_ambient_noise(source) # функция подстраивает чувствительность микрофона для корректного распознования речи без шумов
        audio = voice_recognizer.listen(source)
        #микрофон снова доступен другим программам

    voice_text = voice_recognizer.recognize_google(audio, language='ru')
    print ('— '+ voice_text)
    return voice_text


def reply(text): #ответ голосовой

    voice = gtts.gTTS(text, lang='ru') #гугл включился
    audio_file = 'audio.mp3'
    voice.save(audio_file)

    playsound.playsound(audio_file)
    os.remove('audio.mp3')
    print('— '+ text)


def handle_command(command): #отработка ответов
    command = command.lower()
    if command == 'привет':
        reply('Ну привет, дорогуша')
    elif command == 'пока':
        reply('приходи еще')
        exit()               #выход
    elif command == 'какая на улице погода':
        reply('сдувает, одевайся теплее')
    elif command == 'хочу на море':
        reply('Дак полетели в Турцию, уже смотрю билеты, дорогуша')       
    elif command == 'время обеда':
        reply('одевайся, тогда за шавермой пойдем')            
    else:
        reply('Что еще раз?')
        start()
       


def start():# вызов  функций
    while True:
        user_text = user_input()
        handle_command(user_text)


start() #запуск

# user_text=user_input()
# reply(user_text)


