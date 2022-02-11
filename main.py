import time

import keyboard

import screen_reader
import mines_control
import webbrowser

HEIGHT = 16
WIDTH = 30
webbrowser.open(r"https://minesweeperonline.com/#200")

# wait for player to open the minesweeper game
time.sleep(2)
mines_control.restart()

# grab initial screenshot to find the playing field
screenshot = screen_reader.get_screen_gray()
contours = screen_reader.get_contours(screenshot)
rects = screen_reader.contours_to_rects(contours, HEIGHT * WIDTH)
ORIGIN = screen_reader.get_rect_origin(rects)

# the initial data gathering process is finished
# now its time for the main loop
while True:
    time.sleep(0.2)
    if keyboard.is_pressed("q"):
        break

    # get a new screenshot
    img = screen_reader.get_screen_gray()

    # depending on the new game condition continue playing
    # or quit this bot
    game_state = mines_control.get_game_state(img)
    if game_state == mines_control.GAME_STATES.GAME_OVER:
        break
    elif game_state == mines_control.GAME_STATES.START:
        mines_control.start_random()
