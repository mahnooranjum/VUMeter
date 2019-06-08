#==============================================================================
#   AUTHOR: MAHNOOR ANJUM
#   EMAIL: manomaq@gmail.com
#   DATE: 17/12/2018
#   CODE REFERENCE: https://www.swharden.com
#   DESCRIPTION: Live Volume Meter in Python
#==============================================================================
import pyaudio
import numpy as np

CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)
peak = 0
i = 0
while(peak<10000): #go for a few seconds
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))
    print("%04d %d"%(i,peak))
    i = i+1

stream.stop_stream()
stream.close()
p.terminate()