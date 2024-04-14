import pygame
import sys

def play_song(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(-1)

def stop_song():
    pygame.mixer.music.stop()

def play_sound_effect(sound_path):
    sound = pygame.mixer.Sound(sound_path)
    sound.play()

def main():
    pygame.init()
    pygame.mixer.init()

    print("Pygame initialized")

    screen = pygame.display.set_mode((400, 300))
    if not screen:
        print("Unable to create Pygame window")
        sys.exit()

    pygame.display.set_caption('Music Player')

    print("Window created")

    clock = pygame.time.Clock()

    playing = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if not playing:
                play_song("trashman.mp3")
                playing = True
        elif keys[pygame.K_a]:
            if playing:
                stop_song()
                print("Thank you for the food!")
                play_sound_effect("monch.mp3")
                playing = False

        screen.fill((255, 255, 255))

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()

    # while True:

    #     input_text = input("Throw out your trash here!: ")

    #     if input_text.strip() == "w":
    #         if not playing:
    #             play_song("trashman.mp3")
    #             playing = True
    #     elif input_text.strip() == "a":
    #         if playing:
    #             pygame.mixer.music.stop()
    #             print("Thank you for the food!")
    #             play_sound_effect("monch.mp3")
    #             playing = False
    #     else:
    #         print("Invalid command.")
