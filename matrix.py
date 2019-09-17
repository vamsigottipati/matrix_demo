import curses
from curses import textpad
import time
import random

def getRandomChar(pos_string):
    return pos_string[random.randint(0, len(pos_string)-1)]


# def main(stdscr):
#     pos_string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Ͱ', 'ͱ', 'Ͳ', 'ͳ', 'Ͷ', 'ͻ', 'ͼ', 'ͽ', 'Ά', 'Έ', 'Ή', 'Ύ', 'Ώ', 'ΐ', 'Δ', 'Θ', 'Ξ', 'Π', 'Σ', 'Φ', 'Ψ', 'ά', 'ή', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'λ', 'μ', 'π', 'ξ', 'ρ', 'φ', 'χ', 'ϐ', 'Ϗ', 'ϒ', 'ϖ', 'ϗ', 'Ϙ', 'Ϝ', 'ϟ', 'Ϡ', 'Ϣ', 'ϧ', 'Ϫ', 'ϴ', 'ϯ', '϶', 'ϼ']
#     sh, sw = stdscr.getmaxyx()
#     curses.curs_set(0)
#     curses.init_pair(1, 2, 0)
#     curses.init_pair(2, curses.COLOR_WHITE, 0)
#     move = False

#     rain_cont = []

#     for i in range(sw-1):
#         if i%2 == 0:
#             rain_cont_inner = []
#             rain_height = random.randint(0, int(2*sh/3)-1)
#             margin_top = random.randint(0, int(sh/3))
#             for j in range(rain_height):
#                 rain_cont_inner.append([j+margin_top, i, getRandomChar(pos_string), rain_height-j])
#             rain_cont.append(rain_cont_inner)



#     # print(rain_cont[5])
        
#     inc = 0
#     while True:
#         for sr in rain_cont:
#             base_y = sr[0][0]
#             base_x = sr[0][1]
#             count = 0
#             if count%2 == 0:
#                 for y,x,d,r in sr:
#                     if y+inc < sh:
#                         stdscr.addstr(y+inc,x,getRandomChar(pos_string))
#                         stdscr.refresh()
#             count += 1
#             if inc > 0 and base_y+inc-1 < sh:
#                 stdscr.addstr(base_y+inc-1, base_x, ' ')
#         time.sleep(0.1)

            # counter_empty = 0 

            # for j in range(len(rain_cont[i])-1):
            #     if rain_cont[i][j] != ' ':
            #         counter_empty += 1

            # if counter_empty > rain_cont_pos[i][0]:
            #     if inserted_data[i] < rain_cont_pos[i][1]:
            #         rain_cont[i][0] = getRandomChar(pos_string)
            #         inserted_data[i] += 1


#         inc += 1




# def main(stdscr):
#     sh, sw = stdscr.getmaxyx()
#     ush = sh -1
#     usw = sw - 1
#     curses.curs_set(0)
#     curses.init_pair(1, 2, 0)
#     curses.init_pair(2, curses.COLOR_WHITE, 0)
#     pos_string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Ͱ', 'ͱ', 'Ͳ', 'ͳ', 'Ͷ', 'ͻ', 'ͼ', 'ͽ', 'Ά', 'Έ', 'Ή', 'Ύ', 'Ώ', 'ΐ', 'Δ', 'Θ', 'Ξ', 'Π', 'Σ', 'Φ', 'Ψ', 'ά', 'ή', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'λ', 'μ', 'π', 'ξ', 'ρ', 'φ', 'χ', 'ϐ', 'Ϗ', 'ϒ', 'ϖ', 'ϗ', 'Ϙ', 'Ϝ', 'ϟ', 'Ϡ', 'Ϣ', 'ϧ', 'Ϫ', 'ϴ', 'ϯ', '϶', 'ϼ']
#     rain_cont = []
#     rain_cont_pos = []

#     for i in range(usw):
#         rain_str = []
#         rand_length = random.randint(0, ush)
#         rand_margin = random.randint(0, int(ush - rand_length))
#         rain_cont_pos.append([rand_margin, rand_length])

#         for j in range(ush):
#             if j > int(rand_margin/2) and j < int(int(rand_margin/2)+rand_length):
#                 rain_str.append(getRandomChar(pos_string))
#             else:
#                 rain_str.append(' ')
#         rain_cont.append(rain_str)
    
#     while True:
#         for i in range(len(rain_cont)-1):
#             count = 0
#             if 5*i%3 == 0:
#                 for j in range(len(rain_cont[i])-1):
#                     stdscr.addstr(j,i,rain_cont[i][j], curses.color_pair(1))
#                     stdscr.refresh()

#         # code for changing rain_cont list

#         inserted_data = []

#         for i in range(len(rain_cont)-1):
#             inserted_data.append(0)

#         for i in range(len(rain_cont)-1):
#             rain_cont[i].pop()
#             rain_cont[i].insert(0, ' ')

#             counter_empty = 0
#             for j in range(len(rain_cont[i])-1):
#                 if rain_cont[i][j] == ' ':
#                     counter_empty += 1
#                 else:
#                     break

#             if counter_empty >= rain_cont_pos[i][0]:
#                 rain_cont[i][0] = getRandomChar(pos_string)

#         time.sleep(0.1)



















def rand_string(character_set, length):
    return "".join(random.choice(character_set) for _ in range(length))


def main(stdscr):
    curses.curs_set(0)
    clr_scr = True
    curses.init_pair(1, 2, 0)
    stdscr.bkgd(curses.color_pair(1))
    curses.init_pair(2, curses.COLOR_WHITE, 0)
    curses.start_color()
    sh, sw = stdscr.getmaxyx()
    pos_string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Ͱ', 'ͱ', 'Ͳ', 'ͳ', 'Ͷ', 'ͻ', 'ͼ', 'ͽ', 'Ά', 'Έ', 'Ή', 'Ύ', 'Ώ', 'ΐ', 'Δ', 'Θ', 'Ξ', 'Π', 'Σ', 'Φ', 'Ψ', 'ά', 'ή', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'λ', 'μ', 'π', 'ξ', 'ρ', 'φ', 'χ', 'ϐ', 'Ϗ', 'ϒ', 'ϖ', 'ϗ', 'Ϙ', 'Ϝ', 'ϟ', 'Ϡ', 'Ϣ', 'ϧ', 'Ϫ', 'ϴ', 'ϯ', '϶', 'ϼ']

    background = rand_string(pos_string, sh * sw)
    foreground = []
    char_set   = []


    d = 0
    refresh_rate = random.randint(5, 10)
    prev_time = time.time()

    while 1:
        if clr_scr:
            stdscr.clear()
        else:
            stdscr.erase()

        cur_time = time.time()
        d += (cur_time - prev_time) * 18
        prev_time = cur_time

        while d >= 1:

            for _ in range(2):
                char_set.append(random.randint(0, sw - 1))

            for i, c in enumerate(char_set):
                foreground.append([0, c])
                if not random.randint(0, 3):
                    del char_set[i]

            for a, b in enumerate(foreground):
                if b[0] < sh - 1:
                    if not 5*b[1]%5:
                        stdscr.addstr(b[0], b[1], background[b[0] * sh + b[1]], curses.color_pair(1))
                        b[0] += 1
                else:
                    del foreground[a]

            refresh_rate -= 1

            if refresh_rate <= 0:
                background = rand_string(pos_string, sh * sw)
                refresh_rate = random.randint(5, 10)

            d -= 1
            stdscr.refresh()






curses.wrapper(main)