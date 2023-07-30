import numpy
import math
from turtle import *
from pyAudioAnalysis import *
#from pyAudioAnalysis.audioFeatureExtraction import *
#from pyAudioAnalysis import *
#from pyAudioAnalysis.audioFeatureExtraction import beat_detector


## BPM Finder Function
# This function takes the input of a song and returns its tempo (BPM). It uses Python's
# built-in MIDI module to read information about each note played by an instrument or group of notes
# on a piano keyboard while playing that piece of music. The program then analyzes this data
# using mathematical functions such as sine waves and cosines to determine what frequency is being produced at
def bpmspeed(song_file):
    #Importing songs from specified folder
    path = ("/Users/brerdormido/Desktop/School/pythoncode/portfolio/hysleria/music")
    beat_detect = beat_detector(path)
    song = AudioSegment.from_file(path)
    beats = beat_detect.detect_beats(song)
    bpm = 60 / numpy.mean(numpy.diff(beats))
    return bpm
    

##Heart Function
def hearta(k):
    return 15*math.sin(k)**3

def heartb(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)
        
speed(bpmspeed())
bgcolor("white")

for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#FAA0A0")
    goto(0,0)
done()