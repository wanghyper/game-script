import os


def click(x, y):
    return os.system('adb shell input tap {0} {1}'.format(x,y))


def swipe(x1,y1,x2,y2,time):
    return os.system('adb shell input swipe {0} {1} {2} {3} {4}'.format(x1,y1,x2,y2,time))


def screen_cap(screen_name):
    return os.system('adb shell screencap /sdcard/'+screen_name)


def pull_screen(screen_name):
    return os.system('adb pull /sdcard/'+screen_name+' ./')
