import os, Home, time
from helper import *
from os import system, name
# import voice, datetime,time, os
# from helper import *
# import googletrans, export, Home
# from pprint import pprint
# from moviepy.editor import concatenate_audioclips, AudioFileClip
# from os import system, name
# from time import sleep
 
def clear():
    if name == 'nt':
        _ = system('cls')
 
    else:
        _ = system('clear')

while True:
    clear()
    # Detect your ip to display content
    # helper = Helper()
    # langCode = helper.detect_language_code()
    # if langCode == None:
    #     langCode = 'en'

    # Home
    home = Home.Home(languge='vi')
    home.welcome()
    number = home.Menu()

    # func
    if number == 1:
        checkFunc = home.setting_menu_1()
        if checkFunc == False:
            print('....')
            time.sleep(2)  
        else:
            home.function1()

# Hex = Home.Home()
# Hex.welcome()
# #audio download
# exp = export.export()
# cv = exp.TranslateSrt()
# musics = []
# if type(cv) == bool:
#     print('Lỗi')
# else:

#     # speed proccess
#     rel = []
#     main = voice.Voicerss()
#     procc_num = 0
#     len_sub = len(cv)
#     status_proc_audio = False
#     lasTime = 0
#     listpro = []
#     for x in cv:
#         try:

#             # speed loader
#             contentTime = x['time'].split(' --> ')
#             start = contentTime[0].split(',')
#             milstarts = start[1]
#             end = contentTime[1].split(',')
#             milends = end[1]
#             starts = datetime.datetime.strptime(start[0], "%H:%M:%S") + datetime.timedelta(milliseconds=int(milstarts))
#             ends   = datetime.datetime.strptime(end[0], "%H:%M:%S") + datetime.timedelta(milliseconds=int(milends))
#             audio = main.generator(x['content'], '1')
#             if 'ERROR' in audio:
#                 pass
#             # count_character = len(x['content'].split(' ')) / 6
#             # if count_character > 6:
#             #     count_character = 6
#             # sp = int(str(count_character).split('.')[1][0])
        
#             # if sp < 5:
#             #     count_character = float('{0}.5'.format(str(count_character).split('.')[0]))
#             # else:
#             #     count_character = int(str(count_character).split('.')[0]) + 1
#             # count_character -= 2.5
            
#             # # create no sound time
#             # if lasTime == 0:
#             #     lasTime = ends
#             # else:
#             #     delay = 0
#             #     while True:
                    
#             #         if lasTime >= starts:
#             #             break
#             #         else:
#             #             delay += 1
#             #             lasTime += datetime.timedelta(seconds=1)
#             #     lasTime = ends
#             #     if delay > 1:
                    
#             #         i = 0
#             #         while i <= int(round(delay)):
#             #             listpro.append(AudioFileClip('./audio_system/nosound.mp3'))
#             #             i += 1
#             # # while True:
#             # #     currentTest += datetime.timedelta(milliseconds=1000000)
#             # #     print(currentTest)
#             # #     if currentTest > tractTime:
#             # #         break
#             # #     else:
#             # #         timeTest += 1
#             # # print(timeTest)
#             # cvToAudio = main.generator(x['content'], str(count_character))
        
#             # if cvToAudio:
#             #     if audio.download_audio(cvToAudio, 'music{0}'.format(str(procc_num))):
#             #         print('[+] Audio processing progress:{0}/{1}'.format(
#             #             str(procc_num), str(len_sub)
                        
#             #         ), end='\r')
#             #         listpro.append(AudioFileClip('./audio/music{0}.mp3'.format(
#             #             str(procc_num)
#             #         )))
#             #         procc_num += 1
#             #         status_proc_audio = True
                    
#             #     else:
#             #         print('[+] Convert to audio error. dddddddd')
#             #         quit()
#             # else:
               
#             #     status_proc_audio = False
#             #     print('[+] Convert to audio error. gfdgdfgdfgfdg')
#             #     quit()
           


    

#         except Exception as e:
#             print(e)
#             print('[+] Time separation error')
#             quit()

#     final_audio = concatenate_audioclips(listpro)
#     final_audio.write_audiofile("output.mp3")
#     input_video_clip = VideoFileClip("video.mp4")
#     input_audio_clip = AudioFileClip("output.mp3")

#     duration = input_video_clip.duration
#     temp_audio_clip = input_audio_clip.set_duration(duration)
#     final_audio_clip = CompositeAudioClip([temp_audio_clip])

#     final = input_video_clip.set_audio(final_audio_clip)
#     final.write_videofile("output.mp4",fps=60)