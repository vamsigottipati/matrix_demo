import curses
from curses import textpad
import time
import random

def getRandomChar(pos_string):
    return pos_string[random.randint(0, len(pos_string)-1)]


def main(stdscr):
    pos_string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Ͱ', 'ͱ', 'Ͳ', 'ͳ', 'Ͷ', 'ͻ', 'ͼ', 'ͽ', 'Ά', 'Έ', 'Ή', 'Ύ', 'Ώ', 'ΐ', 'Δ', 'Θ', 'Ξ', 'Π', 'Σ', 'Φ', 'Ψ', 'ά', 'ή', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'λ', 'μ', 'π', 'ξ', 'ρ', 'φ', 'χ', 'ϐ', 'Ϗ', 'ϒ', 'ϖ', 'ϗ', 'Ϙ', 'Ϝ', 'ϟ', 'Ϡ', 'Ϣ', 'ϧ', 'Ϫ', 'ϴ', 'ϯ', '϶', 'ϼ']
    sh, sw = stdscr.getmaxyx()
    curses.curs_set(0)
    curses.init_pair(1, 2, 0)
    curses.init_pair(2, curses.COLOR_WHITE, 0)
    move = False

    rain_cont = []

    for i in range(sw-1):
        if i%2 == 0:
            rain_cont_inner = []
            rain_height = random.randint(0, int(2*sh/3)-1)
            margin_top = random.randint(0, int(sh/3))
            for j in range(rain_height):
                rain_cont_inner.append([j+margin_top, i, getRandomChar(pos_string), rain_height-j])
            rain_cont.append(rain_cont_inner)



    # print(rain_cont[5])
        
    inc = 0
    while True:
        for sr in rain_cont:
            base_y = sr[0][0]
            base_x = sr[0][1]
            count = 0
            if count%2 == 0:
                for y,x,d,r in sr:
                    if y+inc < sh:
                        stdscr.addstr(y+inc,x,getRandomChar(pos_string))
                        stdscr.refresh()
            count += 1
            if inc > 0 and base_y+inc-1 < sh:
                stdscr.addstr(base_y+inc-1, base_x, ' ')
        time.sleep(0.1)
        inc += 1


curses.wrapper(main)