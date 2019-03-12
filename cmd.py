import adb
import threading

grid_width = 110
center = (547, 1070)
screen_name = 'screen.png'


def walk(action):
    x, y = None, None
    if action.find('left') > -1:
        steps = int(action.split('-')[1])
        x, y = center[0] - grid_width * steps, center[1]  # 向左n格
    if action.find('right') > -1:
        steps = int(action.split('-')[1])
        x, y = center[0] + grid_width * steps, center[1]  # 向右n格
    if action.find('up') > -1:
        steps = int(action.split('-')[1])
        x, y = center[0], center[1] - grid_width * steps  # 向上n格
    if action.find('down') > -1:
        steps = int(action.split('-')[1])
        x, y = center[0], center[1] + grid_width * steps  # 向下n格
    if action == 'attack':
        x, y = 745, 1300  # 确定 右
    if action == 'retreat':
        x, y = 367, 1305  # 确定 左
    if action == 'receive':
        x,y = 540, 1402  # 领取
    if action == 'quit':
        x = 545;y = 1155
    print('walk', action, x, y)
    adb.click(x, y)


def screen_cap():
    adb.screen_cap(screen_name)
    adb.pull_screen(screen_name)


def swipe(x1, x2, y1, y2, time):
    print('swipe', x1, x2, y1, y2, time)
    adb.swipe(x1, x2, y1, y2, time)


def swipe_threading():
    threading.Thread(target=lambda: adb.swipe(100, 100, 200, 200, 1000)).start()
    threading.Thread(target=lambda: adb.swipe(200, 200, 100, 300, 1000)).start()


def click(x, y):
    print("clicked at", x, y)
    # adb.click(x, y)
