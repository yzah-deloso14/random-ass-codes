import time
import os
import subprocess
import sys


# Clear terminal screen
def clear_screen():
	"""Clears the terminal screen, if any"""
	os.system('cls' if os.name == 'nt' else 'clear')

def main():
	clear_screen()

	print("💘 I am the love guru. 💘")
	time.sleep(0.75)
	print("✨ Will you love? Will you not? ✨")
	time.sleep(0.75)
	k = input("✒️ What's your name? ")
	time.sleep(0.5)
	j = input("✒️ Who do you desire? ")
	time.sleep(0.5)

	_random()

	delu()

def _random():
	n = 0
	while n<3:
		print("Analyzing...")
		time.sleep(1)
		n+=1

def delu():
	n = 0
	while n<10:
		print("thangina mo delulUUUUUUUUUUUUU 😹😹😹😹 BAWHASHAHAHAHAHAH")
		time.sleep(0.25)
		n+=1

main()