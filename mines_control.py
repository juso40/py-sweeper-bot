import pyautogui
import enum
import random


class GAME_STATES(enum.IntEnum):
    START = enum.auto()
    RUNNING = enum.auto()
    GAME_OVER = enum.auto()


def restart() -> None:
    pyautogui.press("F2")


def click_pos(x: int, y: int) -> None:
    pyautogui.leftClick(x=x, y=y)


def flag_pos(x: int, y: int) -> None:
    pyautogui.rightClick(x=x, y=y)


def get_game_state(img) -> GAME_STATES:
    return GAME_STATES.GAME_OVER


def start_random(x1: int, y1: int, x2: int, y2: int) -> None:
    click_pos(random.randint(x1, x2), random.randint(y1, y2))
