## Hysleria Album Visualizer
## by Brer D

## Library Imports
import os
import random
import math
import turtle
from turtle import *
import pyAudioAnalysis

def get_bpm(audio_file):
  """
  This function uses pyAudioAnalysis to read a song's beats per minute.

  Args:
    audio_file: The path to the audio file.

  Returns:
    The song's beats per minute.
  """

  # Load the audio file.
  audio = pyAudioAnalysis.AudioSegment.from_file(audio_file)

  # Extract the beats per minute.
  bpm = pyAudioAnalysis.bpm(audio, sr=44100)

  # Return the beats per minute.
  return bpm


# Get a list of all the files in the folder.
files = os.listdir('/Users/brerdormido/Desktop/School/pythoncode/portfolio/hysleria/music')

# Shuffle the list of files.
random.shuffle(files)

# Load the files in the shuffled order.
for file in files:
    audio = pyAudioAnalysis.AudioSegment.from_file(files)
## Read Current Song's BPM
bpm = int(get_bpm(audio))


      
## Heart Function
def hearta(k):
    return 15*math.sin(k)**3

def heartb(k):
    return 12*math.cos(k)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)
        
## Randomize Color Function
def random_color():
  """Returns a random hex code."""
  # Generate a random number between 0 and 255.
  r = random.randint(0, 255)
  # Generate a random number between 0 and 255.
  g = random.randint(0, 255)
  # Generate a random number between 0 and 255.
  b = random.randint(0, 255)
  # Return the hex code as a string.
  return f"#{r:02x}{g:02x}{b:02x}"

## Visualizer Function
def visualizer(k):
  for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        ran_col = random_color()
        color(ran_col)
    goto(0,0)
  done()


## Main Function
def main():
  # Create a canvas.
  canvas = turtle.Screen()
  # Randomize Screen Color
  color = random_color()
  canvas.bgcolor(color)
  #Set canvas title to current song playing
  canvas.title(audio)
  # Set canvas size
  canvas.setup(width=1000, height=1000)
  # Set canvas speed
  canvas.tracer(0)
  # Set canvas delay
  canvas.delay(0)
  #Set speed as BPM
  speed(bpm)
  visualizer()
  
if __name__ == "__main__":
  main()
  


