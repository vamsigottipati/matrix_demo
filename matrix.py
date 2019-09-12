from string import printable
import collections
import random
import sys
import time
import curses

COLORS = {
    "BLACK" : curses.COLOR_BLACK,
    "BLUE" : curses.COLOR_BLUE,
    "CYAN" : curses.COLOR_CYAN,
    "GREEN" : curses.COLOR_GREEN,
    "MAGENTA" : curses.COLOR_MAGENTA,
    "RED" : curses.COLOR_RED,
    "WHITE" : curses.COLOR_WHITE,
    "YELLOW" : curses.COLOR_YELLOW,
}

def rand_string(character_set, length):
    return "".join(random.choice(character_set) for _ in range(length))

def main(stdscr):

    curses.curs_set(0)
    curses.init_pair(9, FG, BG)
    stdscr.bkgd(curses.color_pair(9))
    curses.start_color()
    size = stdscr.getmaxyx()

    background = rand_string(printable.strip(), size[0] * size[1])
    foreground = []
    dispense   = []

    delta = 0
    bg_refresh_counter = random.randint(3, 7)
    lt = time.time()

    while 1:

        if CLEAR:
            stdscr.clear()
        else:
            stdscr.erase()

        now = time.time()
        delta += (now - lt) * UPDATES_PER_SECOND
        lt = now

        while delta >= 1:

            if stdscr.getmaxyx() != size:
                return

            for _ in range(LETTERS_PER_UPDATE):
                dispense.append(random.randint(0, size[1] - 1))

            for i, c in enumerate(dispense):
                foreground.append([0, c])
                if not random.randint(0, PROBABILITY):
                    del dispense[i]

            for a, b in enumerate(foreground):
                if b[0] < size[0] - 1:
                    stdscr.addstr(b[0], b[1],
                                    background[b[0] * size[0] + b[1]],
                                    curses.color_pair(9))
                    b[0] += 1
                else:
                    del foreground[a]

            bg_refresh_counter -= 1
            if bg_refresh_counter <= 0:
                background = rand_string(printable.strip(), size[0] * size[1])
                bg_refresh_counter = random.randint(3, 7)

            delta -= 1
            stdscr.refresh()

def init():


    global BG, CLEAR, FG, LETTERS_PER_UPDATE, PROBABILITY, UPDATES_PER_SECOND
    CLEAR = True 
    FG = 2
    BG = 0
    LETTERS_PER_UPDATE = 3
    PROBABILITY = 6
    UPDATES_PER_SECOND = 18

    try:
        while 1:
            curses.wrapper(main)
    except (EOFError, KeyboardInterrupt):
        sys.exit(0)

if __name__ == "__main__":
    init()
