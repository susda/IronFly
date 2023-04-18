import pygame
from files.pyvidplayer import Video

pygame.init()
win = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()

# provide video class with the path to your video
vid = Video("Assets/introironfly1.mp4")

vid.restart()
while True:
    key = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)

    # your program frame rate does not affect video playback
    clock.tick(60)

    if key == "r":
        vid.restart()  # rewind video to beginning
    elif key == "p":
        vid.toggle_pause()  # pause/plays video
    elif key == "right":
        vid.seek(10)  # skip 15 seconds in video
    elif key == "left":
        vid.seek(-15)  # rewind 15 seconds in video
    elif key == "up":
        vid.set_volume(1.0)  # max volume
    elif key == "down":
        vid.set_volume(0.0)  # min volume

    # draws the video to the given surface, at the given position
    vid.draw(win, (0, 0), force_draw=False)

    pygame.display.update()
