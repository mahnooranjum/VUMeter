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

for i in range(int(10*44100/1024)): #go for a few seconds
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    bars="#"*int(50*peak/2**12)
    print("%04d %05d %s"%(i,peak,bars))

stream.stop_stream()
stream.close()
p.terminate()