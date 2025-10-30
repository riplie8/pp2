import pygame

pygame.init()
pygame.mixer.init()

playlist = ["supervillain.mp3", "timeless.mp3", "batman.mp3"]
current_index = 0
is_paused = False

screen = pygame.display.set_mode((400, 600))

white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font(None, 30)

def status():
    screen.fill(black)

    song_name = playlist[current_index]
    if is_paused:
        status_text = "Pause"
    elif pygame.mixer.music.get_busy():
        status_text = "Playing"
    else:
        status_text = "Stopped"

    text_song = font.render("Song: " + song_name, True, white)
    text_status = font.render("Status: " + status_text, True, white)
    text_controls1 = font.render("P: Play/Pause | S: Stop", True, white)
    text_controls2 = font.render("N: Next | B: Previous", True, white)

    screen.blit(text_song, (10, 10))
    screen.blit(text_status, (10, 50))
    screen.blit(text_controls1, (10, 100))
    screen.blit(text_controls2, (10, 150))

def play(index):
    global is_paused

    new_index = index % len(playlist)
    load = playlist[new_index]
    pygame.mixer.music.load(load)
    pygame.mixer.music.play(loops=0)
    is_paused = False

    return new_index

pygame.mixer.music.load(playlist[current_index])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    is_paused = True
                elif is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                else:
                    pygame.mixer.music.play(loops=0)

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                is_paused = False

            elif event.key == pygame.K_n:
                current_index = (current_index+1) % len(playlist)
                current_index = play(current_index)

            elif event.key == pygame.K_b:
                current_index = (current_index-1) % len(playlist)
                current_index = play(current_index)

    status()
    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()
