import googletrans, json, export, voice, audio_process, datetime, time, movie
class Home:
    def __init__(self, languge='vi')->None:
        self.language = languge
        self.allText = {
            'welcome': 'Tool tự động chuyển subtitle sang giọng nói'
        }
        self.trans = googletrans.Translator()
    def bar (self, count)->None:
        for x in range(count):
            print('-', end='')
        print()

    def welcome (self)->None:
        self.bar(100)
        if self.language == 'vi':
            print(self.allText['welcome'])
        else:
            print(
                self.trans.translate(self.allText['welcome'], src='vi', dest=self.language).text
            )
        self.bar(100)
    
    def Menu (self)->None:
        menu = '''
        [1] Chuyển cơ bản (chỉ dành cho từ Tiếng Anh sang Tiếng Việt) [Thử Nghiệm]
        '''
        if self.language == 'vi':
            print(menu)
        else:
            print(
                self.trans.translate(menu, src='vi', dest=self.language).text
            )
        self.bar(100)
        
        #ask
        if self.language == 'vi':
            print('Chọn số', end=': ')
        else:
            print(
                self.trans.translate('Chọn số', src='vi', dest=self.language).text, end=': '
            )
        try:
            return int(input())
        except:
            if self.language == 'vi':
                print('Lỗi: Vui lòng nhập số')
            else:
                print(
                    self.trans.translate('Lỗi: Vui lòng nhập số', src='vi', dest=self.language).text
                )
            quit()
    def outMessage (self, message_success='', message_error='', error=False):
        if error == True:
            if self.language == 'vi':
                print(message_error, end='')
            else:
                print(
                    self.trans.translate(message_error, src='vi', dest=self.language).text,
                    end = ''
                )
            quit()
        else:
            if self.language == 'vi':
                print(message_success, end='')
            else:
                print(
                    self.trans.translate(message_success, src='vi', dest=self.language).text,
                    end = ''
                )
    def function1 (self):
        srt = '001.srt'
        video = '001.mp4'
        outpath = 'out.mp4'

        
        # if self.language == 'vi':
        #     print('Nhập vào file srt: ', end='')
        #     srt = input()
        #     print('Nhập vào file video: ', end='')
        #     video = input()
        #     print('Nhập vào đường dẫn xuất video: ')
        #     outpath = input()
          
        # else:
        #     print(
        #             self.trans.translate('Nhập vào file srt: ', src='vi', dest=self.language).text,
        #             end = ''
        #         )
        #     srt = input()
        #     print(
        #             self.trans.translate('Nhập vào file video: ', src='vi', dest=self.language).text,
        #             end = ''
        #         )
        #     video = input()
        #     print(
        #             self.trans.translate('Nhập vào đường dẫn xuất video: ', src='vi', dest=self.language).text,
        #             end = ''
        #         )
        #     outpath = input()
        
        # export srt
        exp = export.export()
        trans = exp.TranslateSrt(file=srt, src='en', dest='vi')
        
        if type(trans) == bool:
            if self.language == 'vi':
                print('Đã xảy ra lỗi trong quá trình dịch thuật', end='')
            else:
                print(
                    self.trans.translate('Đã xảy ra lỗi trong quá trình dịch thuật', src='vi', dest=self.language).text,
                    end = ''
                )
            quit()
        else:
            
            # voice object
            voices = voice.Voicerss()
            audio_ = audio_process.Audio_Hex()
            mv = movie.movie()
           
            count_obj = len(trans)
            audio_list = []
            # Browse all items
            checkFirst = False
            temp = None
            Audios = []
            seconds_limit = None
            for audio in trans:
                contentTime = audio['time'].split(' --> ')
                start = contentTime[0].split(',')
                milstarts = start[1]
                end = contentTime[1].split(',')
                milends = end[1]
                mildu = 0
                mildu += int(milstarts)
                mildu += int(milends)
                
                starts = datetime.datetime.strptime(start[0], "%H:%M:%S")
                ends   = datetime.datetime.strptime(end[0], "%H:%M:%S")
                if checkFirst == False:
                    temp = ends
                    checkFirst = True
                else:
                    x = time.strptime(str(starts-temp).split('.')[0],'%H:%M:%S')
                    
                    seconds = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()

                    print(seconds)

                    if seconds > 60:
                        print(True)
                        while seconds > 0:
                            obj = None
                            if seconds > 60:
                                obj = mv.cv_to_object_audio(
                                    audio_file='./audio_system/nosound.mp3',
                                    start=0,
                                    end=60
                                )
                                seconds -= 60
                            else:
                                obj = mv.cv_to_object_audio(
                                    audio_file='./audio_system/nosound.mp3',
                                    start=0,
                                    end=seconds
                                )
                                seconds -= seconds
                            if obj == False:
                             
                                self.outMessage(message_error='Đã xảy ra lỗi trong quá trình chuyển đổi âm thanh', error=True)
                            else:
                                audio_list.append(obj)
                    else:
                        if seconds > 1:
                            obj = mv.cv_to_object_audio(
                                        audio_file='./audio_system/nosound.mp3',
                                        start=0,
                                        end=seconds
                                    )

                            if obj == False: 
                           
                                self.outMessage(message_error='Đã xảy ra lỗi trong quá trình chuyển đổi âm thanh', error=True)
                            audio_list.append(obj)
                    
                    temp = ends
                # dt = datetime.timedelta(hours=tractime.tm_hour,minutes=tractime.tm_min,seconds=tractime.tm_sec).total_seconds()
                # print(dt)
                x = time.strptime(str(ends-starts).split('.')[0],'%H:%M:%S')
                    
                seconds_limit = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
                speed = '0'
                while True:
                    def addMiliSecondToList (mili):
                        if mili > 0:
                            seconds = mili / 1000
                            if seconds < 60:
                              
                                obj = mv.cv_to_object_audio(
                                            audio_file='./audio_system/nosound.mp3',
                                            start=0,
                                            end=seconds
                                        )
                                audio_list.append(obj)
                            else:
                                cv_str = str(seconds)
                                sp = cv_str.split('.')
                                sc = int(sp[0])
                                milis = int(sp[1])

                                if sc > 60:
                                    while sc > 0:
                                        obj = mv.cv_to_object_audio(
                                                audio_file='./audio_system/nosound.mp3',
                                                start=0,
                                                end=60
                                            )
                                        audio_list.append(obj)
                                        sc -= 60
                                if milis > 0:
                                    obj = mv.cv_to_object_audio(
                                                audio_file='./audio_system/nosound.mp3',
                                                start=0,
                                                end=milis/1000
                                            )
                                    audio_list.append(obj)

                    gen_audio = voices.generator(audio['content'], str(speed))
                    if 'ERROR' not in gen_audio:
                        if audio_.download_audio(gen_audio, audio['number']) == False:
                      
                            self.outMessage(message_error='Đã xảy ra lỗi trong quá trình chuyển đổi âm thanh', error=True)
                        else:
                            obj = mv.cv_to_object_audio(
                                        audio_file='./audio/{0}.mp3'.format(audio['number']),
                                    )
                            
                            
                            if obj == False: 
                              
                                self.outMessage(message_error='Đã xảy ra lỗi trong quá trình chuyển đổi âm thanh', error=True)
                            if int(seconds_limit) == 0:
                                audio_list.append(obj)
                                #addMiliSecondToList(mildu)
                                break
                            else:
                                
                                if int(round(obj.end)) <= int(seconds_limit):
                                  
                                    audio_list.append(obj)
                                    #addMiliSecondToList(mildu)
                                    break
                                if speed != '0':
                                    speed = int(speed) + 1
                                else:
                                    speed = round(obj.end / seconds_limit)
                            print('...{0}/{1}'.format(
                                audio['number'], str(count_obj)
                            ), end='\r')
                    else:
                       
                        self.outMessage(message_error='Đã xảy ra lỗi trong quá trình chuyển đổi âm thanh', error=True)
            try:
                mv.add_audio_to_video(video, audio_list, outpath)
                self.outMessage(message_success='Trích xuất video thành công, enter để quay lại menu!')
            except:
                self.outMessage(message_error='Đã xảy ra lỗi trong quá trình trích xuất video', error=True)

    def setting_menu_1 (self):
        menu = '''
            [1] Chỉnh sửa config (API Key text-to-speech...)
            [2] Tiến hành xử lý subtitle
        '''
        try:
            if self.language == 'vi':
                print(menu)
                print('Chọn số', end=': ')
            else:
                print(
                        self.trans.translate(menu, src='vi', dest=self.language).text
                    )
                print(
                        self.trans.translate('Chọn số', src='vi', dest=self.language).text, end=': '
                    )
            number = int(input())

            if number == 1:
                openfile = open('./config/func1.json', 'w+')
                if self.language == 'vi':
                    openfile.write(json.dumps({
                        'api-key': input('Nhập vào API Key lấy từ (https://www.voicerss.org//registration.aspx): ')
                    },))
                else:
                    openfile.write(json.dumps({
                        'api-key': input(self.trans.translate('Nhập vào API Key lấy từ (https://www.voicerss.org//registration.aspx): ', src='vi', dest=self.language).text)
                    }))
                openfile.close()
                return False
            else:
                return True
            
        except Exception as e:
            if self.language == 'vi':
                print(e)
                print('Lỗi: Vui lòng nhập số')
            else:
                print(
                    self.trans.translate('Lỗi: Vui lòng nhập số', src='vi', dest=self.language).text
                )
            quit()
        
