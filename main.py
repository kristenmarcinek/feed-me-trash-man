import pygame
import sys

def play_song(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(-1)
    
def play_sound_effect(sound_path):
    sound = pygame.mixer.Sound(sound_path)
    sound.play()

def main():
    pygame.init()
    pygame.mixer.init()
    
    playing = False

    while True:

        input_text = input("Throw out your trash here!: ")

        if input_text.strip() == "test":
            if not playing:
                play_song("scatman.mp3")
                playing = True
        elif input_text.strip() == "stop":
            if playing:
                pygame.mixer.music.stop()
                print("Thank you for the food!")
                play_sound_effect("monch.mp3")
                playing = False
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
