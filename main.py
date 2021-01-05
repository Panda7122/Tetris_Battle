from tkinter import*
from random import*
import pygame
#基本設定
SHAPES = ([[(0, 0), (1, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (0, 1), (1, 1)]],     # Square
          [[(1, 1), (0, 1), (2, 1), (3, 1)], [(2, 1), (2, 0), (2, 2), (2, 3)], [(1, 2), (0, 2), (2, 2), (3, 2)], [(1, 1), (1, 0), (1, 2), (1, 3)]],     # Line 
          [[(0, 1), (1, 1), (2, 1), (2, 0)], [(2, 2), (1, 1), (1, 0), (1, 2)], [(0, 1), (1, 1), (2, 1), (0, 2)], [(0, 0), (1, 0), (1, 1), (1, 2)]],     # L shape
          [[(0, 0), (0, 1), (1, 1), (2, 1)], [(2, 0), (1, 1), (1, 0), (1, 2)], [(0, 1), (1, 1), (2, 1), (2, 2)], [(0, 2), (1, 0), (1, 1), (1, 2)]],     # J shape
          [[(1, 0), (1, 1), (2, 0), (0, 1)], [(1, 0), (1, 1), (2, 1), (2, 2)], [(1, 1), (2, 1), (1, 2), (0, 2)], [(0, 0), (0, 1), (1, 1), (1, 2)]],     # S shape
          [[(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 1), (2, 1), (2, 0), (1, 2)], [(1, 1), (2, 2), (1, 2), (0, 1)], [(1, 1), (0, 1), (1, 0), (0, 2)]],     # Z shape
          [[(1, 1), (0, 1), (1, 0), (2, 1)], [(1, 1), (1, 2), (1, 0), (2, 1)], [(1, 1), (0, 1), (1, 2), (2, 1)], [(1, 1), (0, 1), (1, 0), (1, 2)]])     # T shape
COLOR = ('#f0f000',
         '#00f0f0',
         '#f0a000',
         '#0000f0',
         '#00f000',
         '#f00000',
         '#a000f0')
colorfile = (
         '.\\piece\\O.png',
         '.\\piece\\I.png',
         '.\\piece\\L.png',
         '.\\piece\\J.png',
         '.\\piece\\S.png',
         '.\\piece\\Z.png',
         '.\\piece\\T.png')
BOX_SIZE = 20
GAME_WIDTH = 240
GAME_HEIGHT = 400
GAME_START_POINT = (GAME_WIDTH / 2 / BOX_SIZE) * BOX_SIZE - BOX_SIZE
level = 0
levelup = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 100, 100, 100, 100, 100, 110, 120, 130, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
levelspeed = [800, 716, 633, 550, 466, 383, 300, 216, 133, 100, 83, 83, 83, 66, 66, 66, 50, 50, 50, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 16, 16, 16, 16, 16, 16, 16]
lc = 0
score = 0
linecount = 0
fast = 1
tmp = 0

#PVP
pvp = 0
turn = 0
turn2 = 0
combo = 0
combo2 = 0
fast2 = 1
harddrop2 = 0
boxes2 = []
hold2 = None
holdtype2 = -1
holdstr2 = None
hold_block2 = None
use_hold2 = 0
gamewindows2 = None
nextstr2 = None
next_block2 = []
damage = []
damage2 = []
attackbar = None
attackbar2 = None
gamewindows = constr_var = nextstr = next_block = img = imgfile = holdstr = hold_block = None
play_again_btn = None
quit_btn = None
contest_btn = None
double_btn = None
hi_text = None
content = None
check = None
end_b = False
img = None
boxes = []
wait = None
last = [-1, 0]
last2 = [-1, 0]
tutn = 0
#讀檔案
file  = open('.\\highscore.txt')
text = []
for line in file:
    text.append(line)
highscore=int(text[0])
person=text[1]
person = person.replace('\n','')
prohigh=int(text[2])
properson = text[3]
file.close()
predictable = True
pressdown = False
hold = None
holdtype = -1
use_hold = 0
mode = 0
past = 0
past2 = 0
totaltime = 0
#視窗
root = Tk()
status = Label(root)
end = Label(root)
hiname = StringVar()
status_var = StringVar()
constr_var = StringVar()
end_word = StringVar()
textplayer1 = StringVar()
textplayer2 = StringVar()
imgfile = ['.\\pretend_weak.png','.\\orz.png', '.\\tetris.png', '']
nowtype = -1
nowtype2 = -1
#遊戲控制
def timer():
    global level, levelspeed, levelup, past, fast, fast2, past2, totaltime
    past += 1
    past2 += 1
    totaltime += 1
    if (past >= levelspeed[level]//fast):
        past = 0
        drop_double(0)
    if (past2 >= levelspeed[level]//fast2):
        past2 = 0
        drop_double(1)
    if totaltime >= 30000:
        level += 1
        levelupsound = '.\\music\\pvp\\levelup.wav'
        lu = pygame.mixer.Sound(levelupsound)
        lu.play()
        totaltime = 0
    if not end_b:
        timecount = root.after(1, timer)
def offset_double(who):
    global nowpiece
    if not who:
        return (min(int(gamewindows.coords(box)[0]) // BOX_SIZE for box in boxes),
            min(int(gamewindows.coords(box)[1]) // BOX_SIZE for box in boxes))
    else:
        return (min(int(gamewindows2.coords(box)[0]) // BOX_SIZE for box in boxes2),
            min(int(gamewindows2.coords(box)[1]) // BOX_SIZE for box in boxes2))
def offset():
    global nowpiece
    return (min(int(gamewindows.coords(box)[0]) // BOX_SIZE for box in boxes),
        min(int(gamewindows.coords(box)[1]) // BOX_SIZE for box in boxes))
def can_move_double(box_coords, new_pos, who):
        x, y = new_pos
        x = x * BOX_SIZE
        y = y * BOX_SIZE
        x_left, y_up, x_right, y_down = box_coords
        if not who:
            overlap = set(gamewindows.find_overlapping((x_left + x_right) / 2 + x, 
                                                       (y_up + y_down) / 2 + y, 
                                                       (x_left + x_right) / 2 + x,
                                                       (y_up + y_down) / 2 + y))
            other_items = set(gamewindows.find_withtag('game')) - set(boxes)
        else:
            overlap = set(gamewindows2.find_overlapping((x_left + x_right) / 2 + x, 
                                                       (y_up + y_down) / 2 + y, 
                                                       (x_left + x_right) / 2 + x,
                                                       (y_up + y_down) / 2 + y))
            other_items = set(gamewindows2.find_withtag('game')) - set(boxes2)
        if y_down + y > GAME_HEIGHT+4*BOX_SIZE or x_left + x < 20 or x_right + x > GAME_WIDTH-20 or overlap & other_items:
            return False
        return True
def can_move(box_coords, new_pos):
        x, y = new_pos
        x = x * BOX_SIZE
        y = y * BOX_SIZE
        x_left, y_up, x_right, y_down = box_coords
        
        overlap = set(gamewindows.find_overlapping((x_left + x_right) / 2 + x, 
                                                   (y_up + y_down) / 2 + y, 
                                                   (x_left + x_right) / 2 + x,
                                                   (y_up + y_down) / 2 + y))
        other_items = set(gamewindows.find_withtag('game')) - set(boxes)

        if y_down + y > GAME_HEIGHT+4*BOX_SIZE or x_left + x < 20 or x_right + x > GAME_WIDTH-20 or overlap & other_items:
            return False
        return True
def move_double(direction, who):
    if all(can_move_double((gamewindows.coords(box)if (not who) else gamewindows2.coords(box)), direction, who) for box in (boxes if not who else boxes2)):
        x, y = direction
        for box in (boxes if not who else boxes2):
            if not who:
                gamewindows.move(box,
                                 x * BOX_SIZE,
                                 y * BOX_SIZE)
            else:
                gamewindows2.move(box,
                                 x * BOX_SIZE,
                                 y * BOX_SIZE)
        return True
    return False
def move(direction):
    if all(can_move(gamewindows.coords(box), direction) for box in boxes):
        x, y = direction
        for box in boxes:
            gamewindows.move(box,
                             x * BOX_SIZE,
                             y * BOX_SIZE)
        return True
    return False
def predict_movement_double(who):
    global turn, nowtype
    if not who:
        level = shape_drop_double(offset_double, who)
        min_y = min([gamewindows.coords(box)[1] for box in boxes])
        return (0, level - (min_y // BOX_SIZE)+min(nowpiece, key = lambda x:x[1])[1])
    else:
        level = shape_drop_double(offset_double, who)
        min_y = min([gamewindows2.coords(box)[1] for box in boxes2])
        return (0, level - (min_y // BOX_SIZE)+min(nowpiece2, key = lambda x:x[1])[1])
def predict_movement():
    global turn, nowtype
    level = shape_drop(offset)
    min_y = min([gamewindows.coords(box)[1] for box in boxes])
    return (0, level - (min_y // BOX_SIZE)+min(nowpiece, key = lambda x:x[1])[1])
def rotate_count_double(t, who):
    global nowpiece, nowtype, SHAPES, turn, turn2, index1, index2, nowtype2
    if not who:
        rotated = SHAPES[nowtype][turn]
    else:
        rotated = SHAPES[nowtype2][turn2]
    return rotated
def rotate_count(t):
    global nowpiece, nowtype, SHAPES, turn
    rotated = SHAPES[nowtype][turn]
    return rotated
def test_double(deltax, deltay, who):
    global gamebox, boxes
    if not who:
        for box in boxes:
            x, y, _, _ = gamewindows.coords(box)
            x-=20
            x //= BOX_SIZE
            y //= BOX_SIZE
            x+=deltax
            y+=deltay
            if x >= 10 or x < 0:
                return False
            if y >= 24 or y < 0:
                return False
            if gamebox[int(y)][int(x)]:
                return False
    else:
        for box in boxes2:
            x, y, _, _ = gamewindows2.coords(box)
            x-=20
            x //= BOX_SIZE
            y //= BOX_SIZE
            x+=deltax
            y+=deltay
            if x >= 10 or x < 0:
                return False
            if y >= 24 or y < 0:
                return False
            if gamebox2[int(y)][int(x)]:
                return False
    return True
def test(deltax, deltay):
    global gamebox, boxes
    for box in boxes:
        x, y, _, _ = gamewindows.coords(box)
        x-=20
        x //= BOX_SIZE
        y //= BOX_SIZE
        x+=deltax
        y+=deltay
        if x >= 10 or x < 0:
            return False
        if y >= 24 or y < 0:
            return False
        if gamebox[int(y)][int(x)]:
            return False
    return True
kickdata = [[(0,0),(-1,0),(-1,-1),(0,+2),(-1,+2)],
            [(0,0),(+1,0),(+1,+1),(0,-2),(+1,-2)],
            [(0,0),(+1,0),(+1,+1),(0,-2),(+1,-2)],
            [(0,0),(-1,0),(-1,-1),(0,+2),(-1,+2)],
            [(0,0),(+1,0),(+1,-1),(0,+2),(+1,+2)],
            [(0,0),(-1,0),(-1,+1),(0,-2),(-1,-2)],
            [(0,0),(-1,0),(-1,+1),(0,-2),(-1,-2)],
            [(0,0),(+1,0),(+1,-1),(0,+2),(+1,+2)]]

linedata = [[(0,0),(-2,0),(+1,0),(-2,+1),(+1,-2)],
            [(0,0),(+2,0),(-1,0),(+2,-1),(-1,+2)],
            [(0,0),(-1,0),(+2,0),(-1,-2),(+2,+1)],
            [(0,0),(+1,0),(-2,0),(+1,+2),(-2,-1)],
            [(0,0),(+2,0),(-1,0),(+2,-1),(-1,+2)],
            [(0,0),(-2,0),(+1,0),(-2,+1),(+1,-2)],
            [(0,0),(+1,0),(-2,0),(+1,+2),(-2,-1)],
            [(0,0),(-1,0),(+2,0),(-1,-2),(+2,+1)]]
kickindex = [1, 4, 6, 9, 11, 14, 12, 3]
kickmove = False
kickmove2 = False
def rotate_double(t, who):
    global nowpiece, turn, nowtype, SHAPES, turn2, nowpiece2, kickmove, kickmove2
    #ro_sound = '.\\music\\pvp\\rotate.wav'
    stuck = False
    rotate_sound = '.\\music\\pvp\\rotate.wav'
    rotateS = pygame.mixer.Sound(rotate_sound)
    if t:
        
        if not who:
            lastturn = turn*4
            turn += 1
        else:
            lastturn = turn2*4
            turn2 += 1
    else:
        
        if not who:
            lastturn = turn*4
            turn += 3
        else:
            lastturn = turn2*4
            turn2 += 3
    #turn += 4
    turn %= 4
    turn2 %= 4
    if not who:
        lastturn += turn
        nowpiece = rotate_count_double(t, who)
    else:
        lastturn += turn2
        nowpiece2 = rotate_count_double(t, who)
    lx = 20
    rx = 220
    by = 480
    index = 0
    for i in range(8):
        if lastturn == kickindex[i]:
            index = i
            break
    if not who:
        kickmove = False
        for i in range(len(boxes)):
            x = nowpiece[i][0] - SHAPES[nowtype][((turn-(1 if t else 3))+4)%4][i][0]
            y = nowpiece[i][1] - SHAPES[nowtype][((turn-(1 if t else 3))+4)%4][i][1]
            gamewindows.move(boxes[i],
                             x * BOX_SIZE,
                             y * BOX_SIZE)
        for box in boxes:
            coord = gamewindows.coords(box)
            x, y, _, _ = coord
            
            x //= BOX_SIZE
            y //= BOX_SIZE
            if y >= 24 or x <= 0 or x > 10:
                stuck = True
                break
            if gamebox[int(y)][int(x-1)]==1:
                stuck = True
        if stuck:
            for i in (kickdata[index] if nowtype > 1 else linedata[index]):
                if(test_double(i[0], i[1], who)):
                    for box in boxes:
                        gamewindows.move(box, i[0]*BOX_SIZE, i[1]*BOX_SIZE)
                    kickmove = True
                    break
            if not kickmove:
                if t:
                    turn += 3
                else:
                    turn += 1
                turn %= 4
                nowpiece = rotate_count_double(not t, who)
                for i in range(len(boxes)):
                    x = nowpiece[i][0] - SHAPES[nowtype][((turn-(3 if t else 1))+4)%4][i][0]
                    y = nowpiece[i][1] - SHAPES[nowtype][((turn-(3 if t else 1))+4)%4][i][1]
                    gamewindows.move(boxes[i],
                                     x * BOX_SIZE,
                                     y * BOX_SIZE)
            else:
                rotateS.play()
        else:
            rotateS.play()
    else:
        kickmove2 = False
        for i in range(len(boxes2)):
            x = nowpiece2[i][0] - SHAPES[nowtype2][((turn2-(1 if t else 3))+4)%4][i][0]
            y = nowpiece2[i][1] - SHAPES[nowtype2][((turn2-(1 if t else 3))+4)%4][i][1]
            gamewindows2.move(boxes2[i],
                             x * BOX_SIZE,
                             y * BOX_SIZE)
        for box in boxes2:
            coord = gamewindows2.coords(box)
            x, y, _, _ = coord
            x //= BOX_SIZE
            y //= BOX_SIZE
            if y >= 24 or x <= 0 or x > 10:
                stuck = True
                break
            if gamebox2[int(y)][int(x-1)]==1:
                stuck = True
        if stuck:
                for i in (kickdata[index] if nowtype > 1 else linedata[index]):
                    if(test_double(i[0], i[1], who)):
                        print(i)
                        for box in boxes2:
                            gamewindows2.move(box, i[0]*BOX_SIZE, i[1]*BOX_SIZE)
                        kickmove2 = True
                        break
                if not kickmove2:
                    print('nope')
                    if t:
                        turn2 += 3
                    else:
                        turn2 += 1
                    turn2 %= 4
                    nowpiece2 = rotate_count_double(not t, who)
                    for i in range(len(boxes2)):
                        x = nowpiece2[i][0] - SHAPES[nowtype2][((turn2-(3 if t else 1))+4)%4][i][0]
                        y = nowpiece2[i][1] - SHAPES[nowtype2][((turn2-(3 if t else 1))+4)%4][i][1]
                        gamewindows2.move(boxes2[i],
                                         x * BOX_SIZE,
                                         y * BOX_SIZE)
                else:
                    rotateS.play()
        else:
            rotateS.play()
def rotate(t):
    global nowpiece, turn, nowtype, SHAPES, kickmove
    
    ro_sound = '.\\music\\original\\rotate.wav'
    rotateS = pygame.mixer.Sound(ro_sound)
    stuck = False
    kickmove = False
    lastturn = turn*4
    if t:
        turn += 1
    else:
        turn += 3
    turn %= 4
    lastturn += turn
    nowpiece = rotate_count(t)
    lx = 20
    rx = 220
    by = 480
    index = 0
    for i in range(8):
        if lastturn == kickindex[i]:
            index = i
            break
    for i in range(len(boxes)):
        x = nowpiece[i][0] - SHAPES[nowtype][((turn-(1 if t else 3))+4)%4][i][0]
        y = nowpiece[i][1] - SHAPES[nowtype][((turn-(1 if t else 3))+4)%4][i][1]
        gamewindows.move(boxes[i],
                         x * BOX_SIZE,
                         y * BOX_SIZE)
    for box in boxes:
        coord = gamewindows.coords(box)
        x, y, _, _ = coord
        
        x //= BOX_SIZE
        y //= BOX_SIZE
        if y >= 24 or x <= 0 or x > 10:
            stuck = True
            break
        if gamebox[int(y)][int(x-1)]==1:
            stuck = True
    if stuck:
        for i in (kickdata[index] if nowtype > 1 else linedata[index]):
            if(test(i[0], i[1])):
                for box in boxes:
                    gamewindows.move(box, i[0]*BOX_SIZE, i[1]*BOX_SIZE)
                kickmove = True
                break
        if not kickmove:
            if t:
                turn -= 3
            else:
                turn -= 1
            turn += 4
            turn %= 4
            nowpiece = rotate_count(not t)
            if t:
                tmp = (turn + 3)%4
            else:
                tmp = (turn + 1)%4
            for i in range(len(boxes)):
                x = nowpiece[i][0] - SHAPES[nowtype][(turn+(3 if t else 1))%4][i][0]
                y = nowpiece[i][1] - SHAPES[nowtype][(turn+(3 if t else 1))%4][i][1]
                gamewindows.move(boxes[i],
                                 x * BOX_SIZE,
                                 y * BOX_SIZE)
        else:
            rotateS.play()
    else:
        rotateS.play()
harddrop = 0
def hard_drop2(who):    
    move_double(predict_movement_double(who), who)
def hard_drop():    
    move(predict_movement())
def switch_hold_double(who):
    global turn, nowpiece, hold, boxes, nowtype, holdtype, index1, index2, holdtype2, boxes2, nowtype2, turn2, nowpiece2
    holdsound = '.\\music\\pvp\\hold.wav'
    holdS = pygame.mixer.Sound(holdsound)
    holdS.play()
    if not who:
        for box in boxes:
            gamewindows.delete(box)
        nowtype, holdtype = holdtype, nowtype
        turn = 0
        if nowtype != -1:
            nowpiece = SHAPES[nowtype][0]
            boxes = draw_now_double(0)
        else:
            index1 += 1
            update_piece_double(0)
        draw_hold_double(0)
        gamewindows.tag_raise('line')
    else:
        for box in boxes2:
            gamewindows2.delete(box)
        nowtype2, holdtype2 = holdtype2, nowtype2
        turn2 = 0
        if nowtype2 != -1:
            nowpiece2 = SHAPES[nowtype2][0]
            boxes2 = draw_now_double(1)
        else:
            index2 += 1
            update_piece_double(1)
        draw_hold_double(1)
        gamewindows.tag_raise('line')
def switch_hold():
    global turn, nowpiece, hold, boxes, nowtype, holdtype
    root.after_cancel(wait)
    for box in boxes:
        gamewindows.delete(box)    
    nowtype, holdtype = holdtype, nowtype
    turn = 0
    if nowtype != -1:
        nowpiece = SHAPES[nowtype][0]
        boxes = draw_now()
    else:
        update_piece()
    draw_hold()
    gamewindows.tag_raise('line')
    drop()
def release(event):
    global fast, pressdown, harddrop, fast2
    if event.char == 's' or event.keysym == 'Down':
        if pvp:
            if event.char == 's':
                
                fast = 1
            else:
                fast2 = 1
        else:
            fast = 1   
def game_control(event):
    global end_b, harddrop, nowpiece, hold, harddrop2, kickmove, kickmove2
    global fast, wait, pressdown, use_hold, use_hold2, fast2
    if not end_b:
        if event.keycode in [65, 37]:#左、A 往左
            if pvp:
                if event.keycode == 37:
                    if not harddrop2:
                        move_double((-1,0), 1)
                        kickmove2 = False
                else:
                    if not harddrop:
                        move_double((-1, 0), 0)
                        kickmove = False
            else:
                if not harddrop:
                    move((-1, 0))
                    kickmove = False
        elif event.keycode in [68, 39]:#右、D 往右
            if pvp:
                if event.keycode == 39:
                    if not harddrop2:
                        move_double((1,0), 1)
                        kickmove2 = False
                else:
                    if not harddrop:
                        move_double((1,0), 0)
                        kickmove = False
            else:
                if not harddrop:
                    move((1, 0))
                    kickmove = False
        #快壓
        elif event.keycode in [32] and not harddrop:#空格 快壓
            harddrop = 1
            if not pvp:
                hard_drop()
            else:
                hard_drop2(0)
        elif event.keycode == 99:
            if pvp:
                harddrop2 = 1
                hard_drop2(1)
        #正旋轉
        elif event.keycode in [87, 38]:#W、上 正旋轉
            if pvp:
                if event.keycode == 38:
                    if not harddrop2:
                        rotate_double(1, 1)
                else:
                    if not harddrop:
                        rotate_double(1, 0)
            else:
                if not harddrop:
                    rotate(1)#旋轉
        #逆旋轉
        elif event.keycode in [16]:#shift 逆旋轉
            if not harddrop:
                if not pvp:
                    rotate(0)
                else:
                    rotate_double(0, 0)
        elif event.keycode == 97:
            if pvp:
                if not harddrop2:
                    rotate_double(0, 1)
        elif event.keycode in [40, 83]:#下、s 加速下降
            if pvp:
                if event.keysym == 'Down':
                    fast2 = 10
                else:
                    fast = 10
            else:
                fast = 10
                if not pressdown:
                    root.after_cancel(wait)
                    drop()
                pressdown = True
        #C交換
        elif event.keycode == 67 and not use_hold and not mode:
            use_hold = 1
            if not pvp:
                clear_holdcanvas()
                switch_hold()
            else:
                clear_holdcanvas_double(0)
                switch_hold_double(0)
        elif event.keycode == 98 and not use_hold2:
            if pvp:
                use_hold2 = 1
                clear_holdcanvas_double(1)
                switch_hold_double(1)
        if not pvp:
            update_predict()
        else:
            update_predict_double(0)
            update_predict_double(1)
def draw_hold_double(who):
    off_x, off_y = (20,20)
    global hold_block, colorfile, holdtype
    if not who:
        hold = SHAPES[holdtype][0]
        for piece in hold:
            x, y = piece
            box = hold_block.create_rectangle(x * BOX_SIZE + off_x,
                                               y * BOX_SIZE + off_y,
                                               x * BOX_SIZE + BOX_SIZE + off_x,
                                               y * BOX_SIZE + BOX_SIZE + off_y,
                                              fill=COLOR[holdtype],
                                              tags="game")
    else:
        file = PhotoImage(file=colorfile[nowtype2])
        hold2 = SHAPES[holdtype2][0]
        for piece in hold2:
            x, y = piece
            box = hold_block2.create_rectangle(x * BOX_SIZE + off_x,
                                               y * BOX_SIZE + off_y,
                                               x * BOX_SIZE + BOX_SIZE + off_x,
                                               y * BOX_SIZE + BOX_SIZE + off_y,
                                               fill=COLOR[holdtype2],
                                               tags="game")
def draw_hold():
    off_x, off_y = (20,20)
    hold = SHAPES[holdtype][0]
    for piece in hold:
        x, y = piece
        box = hold_block.create_rectangle(x * BOX_SIZE + off_x,
                                           y * BOX_SIZE + off_y,
                                           x * BOX_SIZE + BOX_SIZE + off_x,
                                           y * BOX_SIZE + BOX_SIZE + off_y,
                                           fill=COLOR[holdtype],
                                           tags="game")
#畫下一個方塊
nextcolort = [0,0,0,0,0]
nextcolort2 = [0,0,0,0,0]
def draw_next_double(who):
    global next_double, index1, index2
    off_x, off_y = (20,20)
    clear_nextcanvas_double(who)
    for i in range(index1-5, index1):
        for piece in SHAPES[next_double[i]][0]:
                x, y = piece
                box = next_block[i-index1+5].create_rectangle(x * BOX_SIZE + off_x,
                                                   y * BOX_SIZE + off_y,
                                                   x * BOX_SIZE + BOX_SIZE + off_x,
                                                   y * BOX_SIZE + BOX_SIZE + off_y,
                                                   fill=COLOR[next_double[i]],
                                                   tags="game")
    for i in range(index2-5, index2):
        for piece in SHAPES[next_double[i]][0]:
                x, y = piece
                box = next_block2[i-index2+5].create_rectangle(x * BOX_SIZE + off_x,
                                                   y * BOX_SIZE + off_y,
                                                   x * BOX_SIZE + BOX_SIZE + off_x,
                                                   y * BOX_SIZE + BOX_SIZE + off_y,
                                                   fill=COLOR[next_double[i]],
                                                   tags="game")
def draw_next(nexttype):
    off_x, off_y = (20,20)
    for piece in nextpiece:
        x, y = piece
        box = next_block.create_rectangle(x * BOX_SIZE + off_x,
                                           y * BOX_SIZE + off_y,
                                           x * BOX_SIZE + BOX_SIZE + off_x,
                                           y * BOX_SIZE + BOX_SIZE + off_y,
                                           fill=COLOR[nexttype],
                                           tags="game")
#畫當前方塊
def draw_now_double(who):
    global nowpiece, nowpiece2
    boxes = []
    off_x, off_y = (GAME_START_POINT,0)
    if not who:
        nowpiece = SHAPES[nowtype][0]
        for piece in nowpiece:
            x, y = piece
            box = gamewindows.create_rectangle(x * BOX_SIZE + off_x,
                                               y * BOX_SIZE + off_y + 2 * BOX_SIZE,
                                               x * BOX_SIZE + BOX_SIZE + off_x,
                                               y * BOX_SIZE + BOX_SIZE + off_y + 2 * BOX_SIZE,
                                               fill=COLOR[nowtype],
                                               tags="game")
            boxes += [box]
    else:
        nowpiece2 = SHAPES[nowtype2][0]
        for piece in nowpiece2:
            x, y = piece
            box2 = gamewindows2.create_rectangle(x * BOX_SIZE + off_x,
                                               y * BOX_SIZE + off_y + 2 * BOX_SIZE,
                                               x * BOX_SIZE + BOX_SIZE + off_x,
                                               y * BOX_SIZE + BOX_SIZE + off_y + 2 * BOX_SIZE,
                                               fill=COLOR[nowtype2],
                                               tags="game")
            boxes += [box2]
    return boxes
def draw_now():
    global nowpiece
    boxes = []
    off_x, off_y = (GAME_START_POINT,0)
    for piece in nowpiece:
        x, y = piece
        box = gamewindows.create_rectangle(x * BOX_SIZE + off_x,
                                           y * BOX_SIZE + off_y + 2 * BOX_SIZE,
                                           x * BOX_SIZE + BOX_SIZE + off_x,
                                           y * BOX_SIZE + BOX_SIZE + off_y + 2 * BOX_SIZE,
                                           fill=COLOR[nowtype],
                                           tags="game")
        boxes += [box]
    return boxes
#預測位置
def matrix_double(who):
    if not who:
        return [[1 if ((j+min(nowpiece, key=lambda x:x[0])[0]), i) in nowpiece else 0 \
             for j in range(max(nowpiece, key=lambda x: x[0])[0] + 1)] \
             for i in range(max(nowpiece, key=lambda x: x[1])[1] + 1)]
    else:
        return [[1 if ((j+min(nowpiece2, key=lambda x:x[0])[0]), i) in nowpiece2 else 0 \
             for j in range(max(nowpiece2, key=lambda x: x[0])[0] + 1)] \
             for i in range(max(nowpiece2, key=lambda x: x[1])[1] + 1)]
def matrix():
    return [[1 if ((j+min(nowpiece, key=lambda x:x[0])[0]), i) in nowpiece else 0 \
             for j in range(max(nowpiece, key=lambda x: x[0])[0] + 1)] \
             for i in range(max(nowpiece, key=lambda x: x[1])[1] + 1)]
def shape_drop_double(offset_double, who):
    global nowtype, turn
    off_x, off_y = offset_double(who)
    mat = matrix_double(who)
    t = 0
    if not who:
        last_level = len(gamebox) - len(mat) + 1
        for level in range(off_y, last_level):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if gamebox[level+i][off_x+j-1+((10-(off_x+j) if (off_x+j) > 10 else 0))] == 1 and mat[i][j] == 1:
                        return level-1
        return last_level-1
    else:
        last_level = len(gamebox2) - len(mat) + 1
        for level in range(off_y, last_level):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if gamebox2[level+i][off_x+j-1+((10-(off_x+j) if (off_x+j) > 10 else 0))] == 1 and mat[i][j] == 1:
                        return level-1
        return last_level-1
def shape_drop(offset):
    global nowtype, turn
    off_x, off_y = offset()
    mat = matrix()
    t = 0
    last_level = len(gamebox) - len(mat) + 1
    for level in range(off_y, last_level):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if gamebox[level+i][off_x+j-1+((10-(off_x+j) if (off_x+j) > 10 else 0))] == 1 and mat[i][j] == 1:
                    return level-1
    return last_level-1
def remove_predicts_double(who):
    if not who:
        for i in gamewindows.find_withtag('predict'):
            gamewindows.delete(i) 
        gamewindows.update()
    else:
        for i in gamewindows2.find_withtag('predict'):
            gamewindows2.delete(i) 
        gamewindows2.update()
def remove_predicts():
    for i in gamewindows.find_withtag('predict'):
        gamewindows.delete(i) 
    gamewindows.update()
def predict_drop_double(who):
    global nowtype, turn, mode, nowpiece, index1, index2
    level = shape_drop_double(offset_double, who)
    remove_predicts_double(who)
    
    if not who:
        minx = min(nowpiece, key = lambda x:x[0])[0]
        miny = min(nowpiece, key = lambda x:x[1])[1]
        min_y = min([gamewindows.coords(box)[1] for box in boxes])
        for box in boxes:
            x1, y1, x2, y2 = gamewindows.coords(box)
            box = gamewindows.create_rectangle(x1,
                                               (level+miny) * BOX_SIZE + (y1 - min_y),
                                               x2,
                                               (level + 1+miny) * BOX_SIZE + (y1 - min_y),
                                               outline=(COLOR[nowtype]),
                                               tags = "predict")
    else:
        minx = min(nowpiece2, key = lambda x:x[0])[0]
        miny = min(nowpiece2, key = lambda x:x[1])[1]
        min_y = min([gamewindows2.coords(box)[1] for box in boxes2])
        for box in boxes2:
            
            x1, y1, x2, y2 = gamewindows2.coords(box)
            
            box = gamewindows2.create_rectangle(x1,
                                               (level+miny) * BOX_SIZE + (y1 - min_y),
                                               x2,
                                               (level+1+miny) * BOX_SIZE + (y1 - min_y),
                                               outline=(COLOR[nowtype2]),
                                               tags = "predict")
def predict_drop():
    global nowtype, turn, mode, nowpiece, boxes
    level = shape_drop(offset)
    remove_predicts()
    minx = min(nowpiece, key = lambda x:x[0])[0]
    miny = min(nowpiece, key = lambda x:x[1])[1]
    min_y = min([gamewindows.coords(box)[1] for box in boxes])
    print(boxes)
    for box in boxes:
        x1, y1, x2, y2 = gamewindows.coords(box)
        
        box = gamewindows.create_rectangle(x1,
                                           (level+miny) * BOX_SIZE + (y1 - min_y),
                                           x2,
                                           (level + 1+miny) * BOX_SIZE + (y1 - min_y),
                                           outline=(COLOR[nowtype] if (not mode) else "#000000"),
                                           tags = "predict")
def update_predict_double(who):
    predict_drop_double(who)
def update_predict():
    predict_drop()
#方塊掉落確認
def drop_boxes_double(boxes_to_drop, who):
    if not who:
        for box in boxes_to_drop:
            gamewindows.move(box, 0, BOX_SIZE)
        gamewindows.update()
    else:
        for box in boxes_to_drop:
            gamewindows2.move(box, 0, BOX_SIZE)
        gamewindows2.update()
def drop_boxes(boxes_to_drop):
    for box in boxes_to_drop:
        gamewindows.move(box, 0, BOX_SIZE)
    gamewindows.update()
def clean_line_double(boxes_to_delete, who):
    if not who:
        for box in boxes_to_delete:
            gamewindows.delete(box)
        gamewindows.update()
    else:
        for box in boxes_to_delete:
            gamewindows2.delete(box)
        gamewindows.update()
def clean_line(boxes_to_delete):
    for box in boxes_to_delete:
        gamewindows.delete(box)
    gamewindows.update()
def completed_lines_cnt_double(y_coords, who):
    cleaned_lines = 0
    y_coords = sorted(y_coords)
    if not who:
        for y in y_coords:
            if sum(1 for box in gamewindows.find_withtag('game') if gamewindows.coords(box)[3] == y) == ((GAME_WIDTH - 40) // BOX_SIZE):
                clean_line_double([box for box in gamewindows.find_withtag('game') if gamewindows.coords(box)[3] == y], who)
    
                drop_boxes_double([box for box in gamewindows.find_withtag('game') if gamewindows.coords(box)[3] < y], who)
                cleaned_lines += 1
    else:
        for y in y_coords:
            if sum(1 for box in gamewindows2.find_withtag('game') if gamewindows2.coords(box)[3] == y) == ((GAME_WIDTH - 40) // BOX_SIZE):
                clean_line_double([box for box in gamewindows2.find_withtag('game') if gamewindows2.coords(box)[3] == y], who)
    
                drop_boxes_double([box for box in gamewindows2.find_withtag('game') if gamewindows2.coords(box)[3] < y], who)
                cleaned_lines += 1
    return cleaned_lines
def completed_lines_cnt(y_coords):
    cleaned_lines = 0
    y_coords = sorted(y_coords)
    for y in y_coords:
        if sum(1 for box in gamewindows.find_withtag('game') if gamewindows.coords(box)[3] == y) == ((GAME_WIDTH - 40) // BOX_SIZE):
            clean_line([box for box in gamewindows.find_withtag('game') if gamewindows.coords(box)[3] == y])

            drop_boxes([box for box in gamewindows.find_withtag('game') if gamewindows.coords(box)[3] < y])
            cleaned_lines += 1
    return cleaned_lines
attackbox = []
attackbox2 = []
def update_attack():#not done
    global damage, damage2, attackbox, attackbox2, attackbar, attackbar2
    attackbar2.delete('all')
    for i in range (min(20, sum(damage2))):
        if i < damage2[0]:
            bar = attackbar2.create_rectangle(0,
                                               (19-i) * 15,
                                               15,
                                               (20-i) * 15,
                                               fill="#FA0000",
                                               tags="game")
        else:
            bar = attackbar2.create_rectangle(0,
                                       (19-i) * 15,
                                       15,
                                       (20-i) * 15,
                                       fill="#ffffff",
                                       tags="game")
        attackbox2 += [bar]
    attackbar.delete('all')
    for i in range (min(20, sum(damage))):
        if i < damage[0]:
            bar2 = attackbar.create_rectangle(0,
                                           (19-i) * 15,
                                           15,
                                           (20-i) * 15,
                                           fill="#FA0000",
                                           tags="game")
        else:
            bar2 = attackbar.create_rectangle(0,
                                           (19-i) * 15,
                                           15,
                                           (20-i) * 15,
                                           fill="#ffffff",
                                           tags="game")
        attackbox += [bar2]
def attack(who):
    global damage, damage2, gamebox, gamebox2
    garbage = '.\\music\\pvp\\garbage.wav'
    gs = pygame.mixer.Sound(garbage)
    gs.play()
    c = randint(0, 9)
    if not who:
        for i in range(damage[0]):
            for box in gamewindows.find_withtag('game'):
                gamewindows.move(box,
                                 0,
                                 -BOX_SIZE)
            for j in range(10):
                if j != c:
                    gamebox[23-i][j] = 1
                    box = gamewindows.create_rectangle(j * BOX_SIZE + 20,
                                               22 * BOX_SIZE + 20,
                                               j * BOX_SIZE + BOX_SIZE + 20,
                                               22 * BOX_SIZE + BOX_SIZE + 20,
                                               fill="#404040",
                                               tags="game")
    else:
        for i in range(damage2[0]):
            for box in gamewindows2.find_withtag('game'):
                gamewindows2.move(box,
                                 0,
                                 -BOX_SIZE)
            for j in range(10):
                if j != c:
                    gamebox2[23-i][j] = 1
                    box = gamewindows2.create_rectangle(j * BOX_SIZE + 20,
                                               22 * BOX_SIZE + 20,
                                               j * BOX_SIZE + BOX_SIZE + 20,
                                               22 * BOX_SIZE + BOX_SIZE + 20,
                                               fill="#404040",
                                               tags="game")
b2b = 0
b2b2 = 0
def completed_lines_double(who):
        global combo, combo2, damage, damage2, attackbar, attackbar2, kickmove, kickmove2
        global lastcomplete, lastcomplete2, b2b, b2b2
        tspin = False
        if not all (can_move_double(gamewindows.coords(box)if not who else gamewindows2.coords(box), (1,0), who) for box in (boxes if not who else boxes2)):
            if not all (can_move_double(gamewindows.coords(box)if not who else gamewindows2.coords(box), (0,1), who) for box in (boxes if not who else boxes2)):
                if not all (can_move_double(gamewindows.coords(box)if not who else gamewindows2.coords(box), (-1,0), who) for box in (boxes if not who else boxes2)):
                    if not all (can_move_double(gamewindows.coords(box)if not who else gamewindows2.coords(box), (0,-1), who) for box in (boxes if not who else boxes2)):
                        if not who:
                            if nowtype == 6:
                                tspin = True
                        else:
                            if nowtype2 == 6:
                                tspin = True
        y_coords = [(gamewindows.coords(box)[3]if not who else gamewindows2.coords(box)[3]) for box in (boxes if not who else boxes2)]
        completed_line = completed_lines_cnt_double(y_coords, who)
        damagecnt = 0
        damage2cnt = 0
        if completed_line != 0:
            if tspin:
                tspin_sound = '.\\music\\pvp\\tspin.wav'
                tspinS = pygame.mixer.Sound(tspin_sound)
                tspinS.play()
            else:
                clear = ['.\\music\\pvp\\single.wav', '.\\music\\pvp\\double.wav', '.\\music\\pvp\\triple.wav', '.\\music\\pvp\\tetris.wav']
                completed = pygame.mixer.Sound(clear[completed_line-1])
                completed.play()
            if not who:
                if not tspin:
                    damagecnt = completed_line
                else:
                    damagecnt = completed_line*2
                if b2b and (completed_line == 4 or tspin == True):
                    damagecnt = int(damagecnt * 1.5)
                if combo >= 7:
                    damagecnt += 4
                elif combo > 0:
                    damagecnt += ((combo-1)//2)+1
                pc=0
                gamebox = game_board_double(who)
                for i in range(len(gamebox)):
                    print(gamebox[i])
                    pc += sum(gamebox[i])
                if pc == 0:
                    damagecnt += 10
                combo += 1
                if completed_line == 4 or tspin == True:
                    b2b = 1
                else:
                    b2b = 0
                while len(damage) != 0 and damagecnt != 0:
                    if damage[0] > damagecnt:
                        damage[0] -= damagecnt
                        damagecnt = 0
                    else:
                        del damage[0]
                if damagecnt > 0:
                    damage2.append(damagecnt)
            else:
                if not tspin:
                    damage2cnt = completed_line
                else:
                    damage2cnt = completed_line*2
                if b2b2:
                    damage2cnt *= 1.5
                if combo2 >= 7:
                    damage2cnt += 4
                elif combo2 > 0:
                    damage2cnt += ((combo2-1)//2)+1
                pc=0
                gamebox2 = game_board_double(who)
                for i in range(len(gamebox2)):
                    print(gamebox2[i])
                    pc += sum(gamebox2[i])
                if pc == 0:
                    damage2cnt = 10
                while len(damage2) != 0 and damage2cnt != 0:
                    if damage2[0] > damage2cnt:
                        damage2[0] -= damage2cnt
                        damage2cnt = 0
                    else:
                        del damage2[0]
                combo2 += 1
                if completed_line == 4 or tspin == True:
                    b2b2 = 1
                else:
                    b2b2 = 0
                
                if damage2cnt > 0:
                    damage.append(damage2cnt)
        else:
            if not who:
                combo = 0
                if sum(damage) > 0:
                    attack(0)
                    del damage[0]
            else:
                
                combo2 = 0
                if sum(damage2) > 0:
                    attack(1)
                    del damage2[0]
        conbovar.set(f"combo:{combo}")
        conbovar2.set(f"combo:{combo2}")
        update_attack()
def completed_lines():
        global score, linecount, lc, level
        tspin = 0
        if not all (can_move(gamewindows.coords(box), (1,0)) for box in boxes):
            if not all (can_move(gamewindows.coords(box), (0,1)) for box in boxes):
                if not all (can_move(gamewindows.coords(box), (-1,0)) for box in boxes):
                    if not all (can_move(gamewindows.coords(box), (0,-1)) for box in boxes):
                        if nowtype == 6:
                            print('T-SPIN')
                            tspin = 1
        y_coords = [gamewindows.coords(box)[3] for box in boxes]
        completed_line = completed_lines_cnt(y_coords)
        
        if completed_line != 0:
            if tspin:
                tspin_sound = '.\\music\\pvp\\tspin.wav'
                tspinS = pygame.mixer.Sound(tspin_sound)
                tspinS.play()
            else:
                lineclear = '.\\music\\original\\lineclear.wav'
                tetrisclear = '.\\music\\original\\tetrisclear.wav'
                if completed_line == 4:
                    completed = pygame.mixer.Sound(tetrisclear)
                else:
                    completed = pygame.mixer.Sound(lineclear)
                completed.play()
            if completed_line == 1:
                
                score += 40*(level+1)
                linecount += 1
                lc += 1
            elif completed_line == 2:
                score += 100*(level+1)
                linecount += 2
                lc += 2
            elif completed_line == 3:
                score += 300*(level+1)
                linecount += 3
                lc += 3
            elif completed_line >= 4:
                score += 1200*(level+1)
                linecount += 4
                lc += 4
            if linecount >= levelup[level]:
                linecount -= levelup[level]
                level += 1
            update_status()
#更新方塊
next_double = []
index1 = 6
index2 = 6
lastrand = -1
piececnt = [0,0,0,0,0,0,0]
def update_piece_double(who):
    global nextpiece, nowpiece, harddrop, last, SHAPES, boxes, level, levelspeed, fast, last, nowtype, tmp, turn
    global hold, piececnt, use_hold, nextpiece2, nowpiece2, next_double, turn2, nowtype2, harddrop2, boxes2
    lastrand = -1
    percent = [0,0,0,0,0,0,0]
    if len(next_double):
        lastrand = next_double[len(next_double)-1]
    while len(next_double) <= index1 or len(next_double) <= index2:
        randomshuffle = [0,1,2,3,4,5,6]
        for i in range(20):
            a = randint(0, 6)
            b = randint(0, 6)
            randomshuffle[a], randomshuffle[b] = randomshuffle[b], randomshuffle[a]
        for i in range(7):
            next_double.append(randomshuffle[i])
    if not who:
        turn = 0
    else:
        turn2 = 0
    draw_next_double(who)
    if not who:
        nowtype = next_double[index1-6]
    else:
        nowtype2 = next_double[index2-6]
    if not who:
        boxes = draw_now_double(who)
        gamewindows.tag_raise('line')
    else:
        boxes2 = draw_now_double(who)
        gamewindows2.tag_raise('line')

    update_predict_double(who)
    if not who:
        harddrop = 0
    else:
        harddrop2 = 0
        
def update_piece():
    global nextpiece, nowpiece, harddrop, last, SHAPES, boxes, level, levelspeed, fast, last, nowtype, tmp, turn
    global hold, use_hold
    if not nextpiece:#如果下一格沒東西
        tmp = randint(0, 6)
        if tmp == last[0]:
            if last[1]+1>3:
                while tmp == last[0]:
                    tmp = randint(0, 6)
            else:
                last[1] += 1
        else:
            nowtype = tmp
            last[0] = tmp
            last[1] += 1
        nextpiece = SHAPES[tmp][0]#隨機一種方塊
        draw_next(tmp)#畫上去
    nowtype = tmp
    nowpiece = nextpiece#把下一個變成現在的
    turn = 0
    clear_nextcanvas()
    boxes = draw_now()
    tmp = randint(0, 6)
    if tmp == last[0]:
        if last[1]+1>3:
            while tmp == last[0]:
                tmp = randint(0, 6)
        else:
            last[1] += 1
    else:
        last[0] = tmp
        last[1] += 1
    nextpiece = SHAPES[tmp][0]#隨機一種方塊
    draw_next(tmp)#畫上去
   
    harddrop = 0
    gamewindows.tag_raise('line')
    update_predict()#預測位置
def update_status():
    global status_var, mode
    if mode:
        status_var.set(f"HighScore:{properson}---{prohigh}\nScore: {score} Line: {lc} Level:{level}")
    else:
        status_var.set(f"HighScore:{person}---{highscore}\nScore: {score} Line: {lc} Level:{level}")
    status.update()
def game_board_double(who):
    board = [[0] * ((GAME_WIDTH - 40) // BOX_SIZE)\
             for _ in range(GAME_HEIGHT // BOX_SIZE + 4)]
    if not who:
        for box in gamewindows.find_withtag('game'):
            x, y, _, _ = gamewindows.coords(box)
            board[int(y // BOX_SIZE)][int(x // BOX_SIZE)-1] = 1
        return board
    else:
        for box in gamewindows2.find_withtag('game'):
            x, y, _, _ = gamewindows2.coords(box)
            board[int(y // BOX_SIZE)][int(x // BOX_SIZE)-1] = 1
        return board
def game_board():
    board = [[0] * ((GAME_WIDTH - 40) // BOX_SIZE)\
             for _ in range(GAME_HEIGHT // BOX_SIZE + 4)]
    for box in gamewindows.find_withtag('game'):
        x, y, _, _ = gamewindows.coords(box)
        board[int(y // BOX_SIZE)][int(x // BOX_SIZE)-1] = 1
    return board
def play_again_pvp():
    global mode, img, imgfile, pvp, player1, player2
    restart()
    img = PhotoImage(file=imgfile[2])
    endimage.configure(image=img)
    endimage.place(x = GAME_WIDTH + 100, y = 250, width=200, height=200)
    pvp = 0
    mode = 0
    start(0)
    root.mainloop()
def play_again():
    global mode, img, imgfile, pvp
    restart()
    img = PhotoImage(file=imgfile[2])
    endimage.configure(image=img)
    pvp = 0
    mode = 0
    start(0)
    root.mainloop()
def restart():
    global status, end, hiname, status_var, constr_var, end_word, textplayer1, textplayer2
    global gamebox, gamebox2, nextpiece, nextpiece2, nowpiece, nowpiece2, player1, player2
    global img, gamewindows, gamewindows2, next_block, next_block2, hold_block, hold_block2
    global conbovar, combo_text, conbovar2, endimage, root
    root.quit()
    root.destroy()
    root = Tk()
    status = Label(root)
    end = Label(root)
    hiname = StringVar()
    status_var = StringVar()
    constr_var = StringVar()
    end_word = StringVar()
    textplayer1 = StringVar()
    textplayer2 = StringVar()
    gamebox = [[0] * ((GAME_WIDTH - 40) // BOX_SIZE)\
           for _ in range(((GAME_HEIGHT // BOX_SIZE) + 4))]#陣列表示的遊戲框
    gamebox2 = [[0] * ((GAME_WIDTH - 40) // BOX_SIZE)\
               for _ in range(((GAME_HEIGHT // BOX_SIZE) + 4))]
    nextpiece = None#下一個方塊
    nextpiece2 = None
    nowpiece = None#這個方塊
    nowpiece2 = None
    player1 = Label(root)
    player2 = Label(root)
    img = PhotoImage(file=imgfile[2])
    gamewindows = Canvas(root)
    next_block = Canvas(root)
    hold_block = Canvas(root)
    gamewindows2 = Canvas(root)
    next_block2 = Canvas(root)
    hold_block2 = Canvas(root)
    conbovar = StringVar()
    combo_text = Label(root, textvariable = conbovar)
    conbovar2 = StringVar()
    endimage = Label(root, fg="#FF0000", image=img,bg="#000000")
    double_btn = Button(root, text="PK mode", command=PK, bg="#000000",fg="#ffffff")
    contest_btn = Button(root, text="pro mode", command=pro, bg="#000000",fg="#ffffff")
    play_again_btn = Button(root, text="normal mode", command=play_again, bg="#000000",fg="#ffffff")
    quit_btn = Button(root, text="Quit", command=quit, bg="#000000",fg="#ffffff")
    root.geometry("650x550") 
    root.title('Tetris')
    root.iconbitmap('.\\icon.ico')
    root.attributes("-topmost", 1)
    root.config(bg="#000000")
    root.bind("<Key>", game_control)
    root.bind("<KeyRelease>", release)
def PK():
    global mode, imgfile, img, pvp, player1, player2
    restart()
    
    root.geometry("1300x550")
    img = PhotoImage(file=imgfile[2])
    endimage.configure(image=img)
    endimage.place(x = 550, y = 250, width=200, height=200)
    mode = 0
    pvp = 1
    startdouble(0)
    root.mainloop()
def pro_pvp():
    global mode, imgfile, img, pvp, attackbar, attackbar2
    
    restart()
    img = PhotoImage(file=imgfile[2])
    endimage.configure(image=img)
    endimage.place(x = GAME_WIDTH + 100, y = 250, width=200, height=200)
    mode = 1
    pvp = 0
    start(18)
    root.mainloop()
def pro():
    global mode, imgfile, img, pvp
    restart()
    img = PhotoImage(file=imgfile[2])
    endimage.configure(image=img)
    mode = 1
    pvp = 0
    start(18)
    root.mainloop()
def quit():
    global mode, imgfile, img
    hc=open('.\\highscore.txt', 'w+')
    hc.write(str(highscore)+'\n'+ person+'\n'+str(prohigh)+'\n'+ properson)
    hc.close()
    img = PhotoImage(file=imgfile[2])
    endimage.configure(image=img)
    root.quit()
    pygame.mixer.music.stop()
    pygame.quit()
    root.destroy()
def highrecord():
    global content, check, hiname, highscore, hi_text, person
    global contest_btn, quit_btn, play_again_btn, img, properson, mode, double_btn
    if not mode:
        person=hiname.get()
    else:
        properson=hiname.get()
    hc=open('.\\highscore.txt', 'w+')
    hc.write(str(highscore)+'\n'+ person+'\n'+str(prohigh)+'\n'+ properson)
    hc.close()
    hi_text.destroy()
    content.pack_forget()
    check.destroy()
    play_again_btn.place(x = GAME_WIDTH + 146, y = 450, width=100, height=25)
    contest_btn.place(x = GAME_WIDTH + 146, y = 475, width=100, height=25)
    double_btn.place(x = GAME_WIDTH + 146, y = 500, width=100, height=25)
    endimage.configure(image=img)
    update_status()
def game_over_pvp():
    global highscore, end_word, play_again_btn, quit_btn, end_b , contest_btn, gamebox, double_btn
    global content, check, hiname, highscore, hi_text, imgfile, img, mode, prohigh
    total = 0
    total2 = 0
    for i in range(4):
        for j in range(10):
            total += gamebox[i][j]
            total2 += gamebox2[i][j]
    if total > 1 or total2 > 1:
        pygame.mixer.music.stop()
        ko = '.\\music\\pvp\\KO.wav'
        ks = pygame.mixer.Sound(ko)
        ks.play()
        contest_btn = Button(root, text="pro mode", command=pro_pvp, bg="#000000",fg="#ffffff")
        play_again_btn = Button(root, text="normal mode", command=play_again_pvp, bg="#000000",fg="#ffffff")
        quit_btn = Button(root, text="Quit", command=quit, bg="#000000",fg="#ffffff")
        double_btn = Button(root, text="PK mode", command=PK, bg="#000000",fg="#ffffff")
        over = '.\\music\\pvp\\gameover_pvp.wav'
        overS = pygame.mixer.Sound(over)
        overS.play()
        if not end_b:
            end_b = True
            if total > 0:
                textplayer1.set('You pretend weak')
                textplayer2.set('   You win orz  ')
            else:
                textplayer2.set('You pretend weak')
                textplayer1.set('   You win orz  ')
            play_again_btn.place(x = 600, y = 450, width=100, height=25)
            contest_btn.place(x = 600, y = 475, width=100, height=25)
            double_btn.place(x = 600, y = 500, width=100, height=25)
            quit_btn.place(x = 600, y = 525, width=100, height=25)

            player1 = Label(root, textvariable=textplayer1, fg="#FF0000", 
                font=("Comic Sans MS", 22, "bold"),bg="#000000").place(x =  GAME_WIDTH + 50+100+5, y = 200)
            player2 = Label(root, textvariable=textplayer2, fg="#FF0000", 
                font=("Comic Sans MS", 22, "bold"),bg="#000000").place(x = 1300-GAME_WIDTH-50-100-5-222, y = 200)
        return True
    return False
def game_over():
    global highscore, end_word, play_again_btn, quit_btn, end_b , contest_btn, gamebox, double_btn
    global content, check, hiname, highscore, hi_text, imgfile, img, mode, prohigh
    total = 0
    total2 = 0
    for i in range(4):
        for j in range(10):
            total += gamebox[i][j]
    if total > 1:
        
        pygame.mixer.music.stop()
        over = '.\\music\\original\\game-over.wav'
        overS = pygame.mixer.Sound(over)
        overS.play()
        contest_btn = Button(root, text="pro mode", command=pro, bg="#000000",fg="#ffffff")
        play_again_btn = Button(root, text="normal mode", command=play_again, bg="#000000",fg="#ffffff")
        quit_btn = Button(root, text="Quit", command=quit, bg="#000000",fg="#ffffff")
        double_btn = Button(root, text="PK mode", command=PK, bg="#000000",fg="#ffffff")
        if not end_b:
            end_b = True
            if score > (highscore if not mode else prohigh):
                end_word.set("You are Tetris Master orz")
                end.place(x =  GAME_WIDTH, y = 200)
                img = PhotoImage(file=imgfile[1])
                if not mode:    
                    highscore = score
                else:
                    prohigh = score
                hi_text=Label(root, text='Your name', bg="#000000", fg='#ffffff')
                hi_text.place(x =  GAME_WIDTH + 100, y = 300)
                hiname = StringVar()
                content = Entry(root, textvariable=hiname, bd=5, bg="#ffffff", fg="#000000")
                content.place(x =  GAME_WIDTH + 100, y = 350)
                check = Button(root, text='OK', command=highrecord, bg="#000000",fg="#ffffff")
                check.place(x = GAME_WIDTH + 146, y = 250, width=100, height=20)
            else:
                play_again_btn.place(x = GAME_WIDTH + 146, y = 450, width=100, height=25)
                contest_btn.place(x = GAME_WIDTH + 146, y = 475, width=100, height=25)
                double_btn.place(x = GAME_WIDTH + 146, y = 500, width=100, height=25)
                quit_btn.place(x = GAME_WIDTH + 146, y = 525, width=100, height=25)
                img = PhotoImage(file=imgfile[0])
                endimage.configure(image=img)
                end_word.set("You Pretend Weak!")
                end.place(x =  GAME_WIDTH + 50, y = 200)
        status.update()
        return True
    return False
def drop_double(who):
    global gamebox, blockcount, fast, levelspeed, level, levelup, wait, use_hold2, use_hold, index1, index2, gamebox2
    global nowtype, nowtype2
    
    softsound = '.\\music\\pvp\\soft drop.wav'
    softS = pygame.mixer.Sound(softsound)
    if not move_double((0,1), who):
        remove_predicts_double(who)
        completed_lines_double(who)
        if not who:
            if harddrop:
                fall_sound = '.\\music\\pvp\\harddrop.wav'
            else:
                fall_sound = '.\\music\\pvp\\fall.wav'
        else:
            if harddrop2:
                fall_sound = '.\\music\\pvp\\harddrop.wav'
            else:
                fall_sound = '.\\music\\pvp\\fall.wav'
        dropS = pygame.mixer.Sound(fall_sound)
        dropS.play()
        
        if not who:
            use_hold = 0
        else:
            use_hold2 = 0
        if not who:
            gamebox = game_board_double(who)
            index1 += 1
            nowtype = next_double[index1-6]
        else:
            gamebox2 = game_board_double(who)
            index2 += 1
            nowtype2 = next_double[index2-6]
        update_piece_double(who)
        if game_over_pvp():
            return
    else:
        if not who:
            if fast == 10:
                softS.play()
        else:
            if fast2 == 10:
                softS.play()
def drop():
    global gamebox, blockcount, fast, levelspeed, level, levelup, wait, use_hold
    if not move((0,1)):
        fall_sound = '.\\music\\original\\fall.wav'
        dropS = pygame.mixer.Sound(fall_sound)
        dropS.play()
        remove_predicts()
        completed_lines()
        use_hold = 0
        gamebox = game_board()
        update_piece()
        if game_over():
            return
    if(level > len(levelspeed)):
        levelspeed.append(16)
        levelup.append(10)
    wait = root.after((levelspeed[level]//fast), drop)
def startdouble(lev):
    global level, gamebox, end_b, fast, pressdown, hold, attackbar, attackbar2
    global gamewindows, nextstr, next_block, holdstr, hold_block, endimage, constr_var
    global gamewindows2, nextstr2, next_block2, holdstr2, hold_block2, pressdown2, fast2, hold2, gamebox2
    global combo, combo2, damage, damage2, index1, index2, turn2, turn, next_double, harddrop2, boxes2, use_hold2, holdtype, holdtype2
    global index1, index2, nowtype, nowtype2, combo_text, combo_text2, conbovar, conbovar2, piececnt
    next_double = []
    index1 = 6
    index2 = 6
    turn2 = 0
    combo = 0
    combo2 = 0
    b2b = 0
    b2b2 = 0
    fast2 = 1
    harddrop2 = 0
    boxes2 = []
    hold2 = None
    holdtype2 = -1
    holdstr2 = None
    hold_block2 = None
    use_hold2 = 0
    gamewindows2 = None
    nextstr2 = None
    next_block2 = []
    damage = []
    damage2 = []
    gamewindows = Canvas(root,width = GAME_WIDTH, 
                              height = GAME_HEIGHT+4*BOX_SIZE,bg="#000000", bd = 0)
    gamewindows.pack(padx=5 ,pady=0, side = LEFT)#對齊左邊
    attackbar = Canvas(root, width = 15, height = 15*20, bg = '#000000')
    attackbar.place(x = GAME_WIDTH+155, y = 150)
    attackbar2 = Canvas(root, width = 15, height = 15*20, bg = '#000000')
    attackbar2.place(x = 1300-GAME_WIDTH-30-100-5-5, y = 150)
    combo_text = Label(root, textvariable = conbovar, bg = 'Black', fg = 'Yellow',font=("Calisto MT", 12, "bold"))
    combo_text.place(x =GAME_WIDTH+200, y = 150)
    conbovar.set(f"combo:{combo}")
    combo_text2 = Label(root, textvariable = conbovar2, bg = 'Black', fg = 'Yellow',font=("Calisto MT", 12, "bold"))
    combo_text2.place(x =1300-(GAME_WIDTH+200+70), y = 150)
    conbovar2.set(f"combo:{combo2}")
    clear_windows()
    constr_var.set(f"Next:")
    next_block = ['', '', '', '', '']
    nextstr = Label(root,
                    textvariable=constr_var, fg="white", 
                    font=("Calisto MT", 12, "bold"),bg="#000000")
    nextstr.place(x = GAME_WIDTH+50, y = 10)
    for i in range(5):
        next_block[i] = Canvas(root, width = 100,height = 100,bg="#000000")
        next_block[i].place(x = GAME_WIDTH+50, y = 35+i*100)
    holdstr = Label(root,
            text='Hold', fg="white", 
            font=("Calisto MT", 12, "bold"),bg="#000000")
    hold_block = Canvas(root, width = 100,height = 100,bg="#000000")
    holdstr.place(x = GAME_WIDTH+200, y = 10)
    hold_block.place(x = GAME_WIDTH+200, y = 35)
    gamewindows.delete("all")
    holdtype = -1
    clear_windows()
    for i in range(5):
        next_block[i].delete("all")
        next_block[i].create_rectangle(10, 10, 90, 90, tags="frame")
    bgm = '.\\music\\pvp\\battlebgm.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(bgm)
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)
    end_b = False
    pressdown = False
    fast = 1
    level = lev
    clear_holdcanvas()
    hold_block.create_rectangle(10, 10, 90, 90, tags="frame")        
    gamebox = [[0] * ((GAME_WIDTH - 40) // BOX_SIZE)\
                           for _ in range(((GAME_HEIGHT // BOX_SIZE) + 4))]
    
    
    gamewindows2 = Canvas(root,width = GAME_WIDTH, 
                              height = GAME_HEIGHT+4*BOX_SIZE,bg="#000000", bd = 0)
    gamewindows2.pack(padx=5 ,pady=0, side = RIGHT)#對齊左邊
    clear_windows2()
    next_block2 = ['', '', '', '', '']
    nextstr2 = Label(root,
                    textvariable=constr_var, fg="white", 
                    font=("Calisto MT", 12, "bold"),bg="#000000")
    nextstr2.place(x = GAME_WIDTH+50+650, y = 10)
    for i in range(5):
        next_block2[i] = Canvas(root, width = 100,height = 100,bg="#000000")
        next_block2[i].place(x = GAME_WIDTH+50+650, y = 35+i*100)
    holdstr2 = Label(root,
            text='Hold', fg="white", 
            font=("Calisto MT", 12, "bold"),bg="#000000")
    hold_block2 = Canvas(root, width = 100,height = 100,bg="#000000")
    holdstr2.place(x = GAME_WIDTH+200+400, y = 10)
    hold_block2.place(x = GAME_WIDTH+150+400, y = 35)
    gamewindows2.delete("all")
    holdtype2 = -1
    clear_windows2()
    for i in range(5):
        next_block2[i].delete("all")
        next_block2[i].create_rectangle(10, 10, 90, 90, tags="frame")
    pressdown2 = False
    fast2 = 1
    clear_holdcanvas_double(1)
    hold_block2.create_rectangle(10, 10, 90, 90, tags="frame")        
    gamebox2 = [[0] * ((GAME_WIDTH - 40) // BOX_SIZE)\
                           for _ in range(((GAME_HEIGHT // BOX_SIZE) + 4))]
    combo = 0
    combo2 = 0
    damage = []
    damage2 = []
    piececnt = [0,0,0,0,0,0,0]
    update_piece_double(0)#更新方塊
    update_piece_double(1)
    root.after(33, None)#延遲時間
    timer()#掉落
    
     
def start(lev):
    global end_word, level, score, linecount, lc, gamebox, end_b, fast, pressdown, hold
    global gamewindows, constr_var, nextstr, next_block, status, end, img, imgfile, holdstr, hold_block, endimage
    root.geometry("650x550")
    gamewindows = Canvas(root,width = GAME_WIDTH, 
                              height = GAME_HEIGHT+4*BOX_SIZE,bg="#000000", bd = 0)
    gamewindows.pack(padx=5 ,pady=0, side = LEFT)#對齊左邊
    clear_windows()
    constr_var.set(f"Next:")
    nextstr = Label(root,
                    textvariable=constr_var, fg="white", 
                    font=("Calisto MT", 12, "bold"),bg="#000000")
    nextstr.place(x = GAME_WIDTH+50, y = 10)
    next_block = Canvas(root, width = 100,height = 100,bg="#000000")
    next_block.place(x = GAME_WIDTH+50, y = 35)
    status = Label(root, 
                   textvariable=status_var,fg="yellow", 
                   font=("Franklin Gothic Medium", 11, "bold"),bg="#000000")
    status.place(x =  GAME_WIDTH + 100, y = 150)
    end =  Label(root,
                textvariable=end_word, fg="#FF0000", 
                font=("Comic Sans MS", 22, "bold"),bg="#000000")
    end.place(x =  GAME_WIDTH + 50, y = 200)
   
    holdstr = Label(root,
            text='Hold', fg="white", 
            font=("Calisto MT", 12, "bold"),bg="#000000")
    hold_block = Canvas(root, width = 100,height = 100,bg="#000000")
    holdstr.place(x = GAME_WIDTH+200, y = 10)
    hold_block.place(x = GAME_WIDTH+200, y = 35)
    img = PhotoImage(file=imgfile[2])
    endimage = Label(root, fg="#FF0000", image=img,bg="#000000")
    endimage.place(x = GAME_WIDTH + 100, y = 250, width=200, height=200)
    
    gamewindows.delete("all")
    
    holdtype = -1
    clear_windows()
    clear_nextcanvas()
    bgm = '.\\music\\original\\bgm.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(bgm)
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1)
    status.update()
    linecount=0
    lc = 0
    end_word.set(" ")
    end_b = False
    pressdown = False
    fast = 1
    level = lev
    score = 0
    if not mode:
        clear_holdcanvas()
        hold_block.create_rectangle(10, 10, 90, 90, tags="frame")        
    gamebox = [[0] * ((GAME_WIDTH - 40) // BOX_SIZE)\
                           for _ in range(((GAME_HEIGHT // BOX_SIZE) + 4))]
    update_piece()#更新方塊
    update_status()#更新分數
    root.after(33, None)#延遲時間
    drop()#掉落
    update_status()
#基本設定
root.geometry("650x550") 
root.title('Tetris')
root.iconbitmap('.\\icon.ico')
root.attributes("-topmost", 1)
root.config(bg="#000000")
root.bind("<Key>", game_control)
root.bind("<KeyRelease>", release)
#遊戲框



#畫邊邊(美觀
def clear_windows():
    gamewindows.delete("all")
    gamewindows.create_line(20, 4*BOX_SIZE, 20, GAME_HEIGHT+4*BOX_SIZE, fill = "#FFFFFF", tags = "line")
    gamewindows.create_line(GAME_WIDTH-20, 4*BOX_SIZE, GAME_WIDTH-20, GAME_HEIGHT+4*BOX_SIZE, fill = "#FFFFFF", tags = "line")
    gamewindows.create_line(20, GAME_HEIGHT+4*BOX_SIZE, GAME_WIDTH-20, GAME_HEIGHT+4*BOX_SIZE, fill = "#FFFFFF", tags = "line")
    gamewindows.create_line(20, 4*BOX_SIZE, GAME_WIDTH-20, 4*BOX_SIZE, fill = "#FFFFFF", tags = "line")
    gamewindows.create_rectangle(0, 0, GAME_WIDTH, 4*BOX_SIZE-1, fill = "#000000", tags = "line")
    for i in range(1, 10):
        gamewindows.create_line((i+1)*20, 4*BOX_SIZE+1, (i+1)*20, GAME_HEIGHT+4*BOX_SIZE, fill = "#2A2A2A", tags = "line")
    for i in range(1, 20):
        gamewindows.create_line(21, (i*BOX_SIZE)+4*BOX_SIZE, GAME_WIDTH-20, (i*BOX_SIZE)+4*BOX_SIZE, fill = "#2A2A2A", tags = "line")
    gamewindows.tag_raise('line')
def clear_windows2():
    gamewindows2.delete("all")
    gamewindows2.create_line(20, 4*BOX_SIZE, 20, GAME_HEIGHT+4*BOX_SIZE, fill = "#FFFFFF", tags = "line")
    gamewindows2.create_line(GAME_WIDTH-20, 4*BOX_SIZE, GAME_WIDTH-20, GAME_HEIGHT+4*BOX_SIZE, fill = "#FFFFFF", tags = "line")
    gamewindows2.create_line(20, GAME_HEIGHT+4*BOX_SIZE, GAME_WIDTH-20, GAME_HEIGHT+4*BOX_SIZE, fill = "#FFFFFF", tags = "line")
    gamewindows2.create_line(20, 4*BOX_SIZE, GAME_WIDTH-20, 4*BOX_SIZE, fill = "#FFFFFF", tags = "line")
    gamewindows2.create_rectangle(0, 0, GAME_WIDTH, 4*BOX_SIZE-1, fill = "#000000", tags = "line")
    for i in range(1, 10):
        gamewindows2.create_line((i+1)*20, 4*BOX_SIZE+1, (i+1)*20, GAME_HEIGHT+4*BOX_SIZE, fill = "#2A2A2A", tags = "line")
    for i in range(1, 20):
        gamewindows2.create_line(21, (i*BOX_SIZE)+4*BOX_SIZE, GAME_WIDTH-20, (i*BOX_SIZE)+4*BOX_SIZE, fill = "#2A2A2A", tags = "line")
    gamewindows2.tag_raise('line')
#下一個方塊的畫面
def clear_holdcanvas_double(who):
    if not who:
        if holdtype != -1:
            hold_block.delete("game")
        hold_block.create_rectangle(10, 10, 90, 90, tags="frame")
    else:
        if holdtype2 != -1:
            hold_block2.delete("game")
        hold_block2.create_rectangle(10, 10, 90, 90, tags="frame")
def clear_holdcanvas():
    if holdtype != -1:
        hold_block.delete("game")
    hold_block.create_rectangle(10, 10, 90, 90, tags="frame")
def clear_nextcanvas_double(who):
    for i in range(5):
        if not who:
            next_block[i].delete("all")
            next_block[i].create_rectangle(10, 10, 90, 90, tags="frame")
        else:
            next_block2[i].delete("all")
            next_block2[i].create_rectangle(10, 10, 90, 90, tags="frame")
def clear_nextcanvas():
    next_block.delete("all")
    next_block.create_rectangle(10, 10, 90, 90, tags="frame")
#陣列表示遊戲畫面
gamebox = [[0] * ((GAME_WIDTH - 40) // BOX_SIZE)\
           for _ in range(((GAME_HEIGHT // BOX_SIZE) + 4))]#陣列表示的遊戲框
gamebox2 = [[0] * ((GAME_WIDTH - 40) // BOX_SIZE)\
           for _ in range(((GAME_HEIGHT // BOX_SIZE) + 4))]
nextpiece = None#下一個方塊
nextpiece2 = None
nowpiece = None#這個方塊
nowpiece2 = None
player1 = Label(root)
player2 = Label(root)
img = PhotoImage(file=imgfile[2])
gamewindows = Canvas(root)
next_block = Canvas(root)
hold_block = Canvas(root)
gamewindows2 = Canvas(root)
next_block2 = Canvas(root)
hold_block2 = Canvas(root)
conbovar = StringVar()
combo_text = Label(root, textvariable = conbovar)
conbovar2 = StringVar()
combo_text2 = Label(root, textvariable = conbovar2)

endimage = Label(root, fg="#FF0000", image=img,bg="#000000")
endimage.place(x = GAME_WIDTH + 100, y = 250, width=200, height=200)
double_btn = Button(root, text="PK mode", command=PK, bg="#000000",fg="#ffffff")
contest_btn = Button(root, text="pro mode", command=pro, bg="#000000",fg="#ffffff")
play_again_btn = Button(root, text="normal mode", command=play_again, bg="#000000",fg="#ffffff")
quit_btn = Button(root, text="Quit", command=quit, bg="#000000",fg="#ffffff")
play_again_btn.place(x = GAME_WIDTH + 146, y = 450, width=100, height=25)
quit_btn.place(x = GAME_WIDTH + 146, y = 525, width=100, height=25)
contest_btn.place(x = GAME_WIDTH + 146, y = 475, width=100, height=25)
double_btn.place(x = GAME_WIDTH + 146, y = 500, width=100, height=25)
root.mainloop()