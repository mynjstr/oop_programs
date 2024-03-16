# Write a program that will ask you to input your name and your dream job. Print them in a fancy way.
# I will create a program using modules pyfiglet and termcolor.
import pyfiglet
from termcolor import colored

name = input("Please enter your name: ")
dream_job = input("Please enter your dream job: ")

sentence_art = pyfiglet.figlet_format(f"Hi, my name is {name}, and being a {dream_job} is my dream job", font="roman", width=160)

print(colored(sentence_art, 'blue'))