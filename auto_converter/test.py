from pydub import AudioSegment
import os

def speed_swifter(sound, speed=1.0):
    return sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})

in_path = 'your/path/of/input_file/hello.mp3'
ex_path = 'your/path/of/output_file/hello.mp3'
sound = AudioSegment.from_file(in_path)    

# generate a slower audio for example
slower_sound = speed_change(sound, 0.5)

slower_sound.export(os.path.join(ex_path, 'slower.mp3'), format="mp3")