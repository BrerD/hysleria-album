## Hysleria Album Visualizer
## by Brer D

## Library Imports
import random
import math
import turtle
from turtle import *
import pyAudioAnalysis
import pygame

# Initialize Pygame and turtle
turtle.setup(width=800,height=600)
pygame.init()



## Create a list of stars
stars = []

# Create a function to create a star
def create_star():
		# Create a random x and y coordinate for the star
		x = random.randint(-400, 400)
		y = random.randint(-300, 300)

		# Create a random size for the star
		sizing = random.randint(1, 10)

		# Create a turtle object for the star
		star = turtle.Turtle()
		star.shape("circle")
		star.color("white")
		star.penup()
		star.goto(x, y)
		star.pendown()

		# Add the star to the list of stars
		stars.append(star)
		
# Create a function to draw the stars
def draw_stars():
		# For each star in the list of stars
		for star in stars:
				# Draw the star
				star.forward(0.1)
				star.turtlesize(0.5)
				star.left(10)

# Create a function to shrink and grow the stars
def shrink_and_grow_stars():
		# For each star in the list of stars
		for star in stars:
				# Get the current size of the star
				sizes = star.turtlesize()

				# Shrink the star by 10%
				if sizes > 3:
					sizes -= 0.1

				# If the size of the star is less than 1, grow the star by 10%
				if sizes < 1:
						sizes += 0.1

				# Set the size of the star
				star.turtlesize(sizes)

# Create a function to listen to the music
def listen_to_music():
	create_star()
	draw_stars()
	shrink_and_grow_stars()
	



## Get BPM
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


## Read Current Song's BPM
bpm = int(get_bpm('music/04hysleria.mp3'))

## Play Audio Function
def play_music():
		# Set the Pygame mixer volume
		pygame.mixer.music.set_volume(0.5)

		# Load the music file
		pygame.mixer.music.load('music/04hysleria.mp3')

		# Play the music
		pygame.mixer.music.play(-1)

		# Wait for the music to finish
		while pygame.mixer.music.get_busy():
				pygame.time.Clock().tick(10)

		# Quit Pygame
		pygame.quit()


			
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



def main():
	# Play music
	play_music()
	
	# Call the liste_to_music function to listen to the music
	listen_to_music()
	
	# Create a canvas.
	canvas = turtle.Screen()
	# Randomize Screen Color
	ran = random_color()
	
	canvas.bgcolor("black")

	
	# Set canvas speed
	canvas.tracer(0)
	
	# Set canvas delay
	canvas.delay(0)
 
	speed(0)
	for i in range(6000):
		goto(hearta(i)*20,heartb(i)*20)
		for j in range(5):
				color(ran)
		goto(0,0)
	done()

if __name__ == "__main__":
	main()

main.mainloop()
pygame.quit()

