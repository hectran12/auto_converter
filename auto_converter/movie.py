from moviepy.editor import concatenate_audioclips, AudioFileClip, VideoFileClip, CompositeAudioClip
class movie:
    @staticmethod 
    def cv_to_object_audio (audio_file, start=0, end=0):
        try:
            audio_clip = AudioFileClip(audio_file)
            if end == 0:
                end = audio_clip.end
            audio_clip = audio_clip.subclip(start, end)

            return audio_clip
        except:
            return False
    @staticmethod
    def add_audio_to_video (video_file, audio_list, outputPath):
        concatAudio = concatenate_audioclips(audio_list)
        concatAudio.write_audiofile('audio_temp.mp3')
        

        #add to video
        input_video_clip = VideoFileClip(video_file)
        input_audio_clip = AudioFileClip("audio_temp.mp3")
        final = input_video_clip.set_audio(input_audio_clip)
        final.write_videofile(outputPath,fps=60)
