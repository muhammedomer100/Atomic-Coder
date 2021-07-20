from wavefile import WaveReader

with WaveReader("/Users/IrfanAhmad/audio.wav") as r:
    for data in r.read_iter(size=512):
        left_channel = data[0]
        volume = np.linalg.norm(left_channel)
        print (volume)


import sounddevice as sd

duration = 200 #seconds

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print( "") * int(volume_norm)

with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)
