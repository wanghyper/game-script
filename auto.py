import cmd
import time
up='up';down='down';left='left';right='right'
def walk(direct, steps):
    while steps:
        cmd.walk(direct+'-1')
        time.sleep(0.2)
        steps-=1
def attack(interval):
    cmd.walk('attack')
    time.sleep(10.5)
    receive()
def receive():
    cmd.walk('receive')
    time.sleep(0.8)
start_time = time.time()
walk(right,9)
walk(up,2)
attack(9)

walk(right,4)
attack(3.5)

walk(right,1)
walk(down,1)
walk(right,2)
attack(9.5)

walk(right,3)
walk(down,1)
attack(3.5)

walk(up,2)
attack(3.5)

walk(left,1)
attack(9.5)

walk(up,5)
walk(left,11)
walk(up,4)
attack(3.5)

walk(left,3)
attack(3.5)
walk(left,1)
walk(up,2)
attack(3.5)
walk(up,1)
attack(3.5)

walk(left,1)
attack(3.5)
walk(left,1)
attack(3.5)
walk(left,1)
attack(3.5)

walk(up,3)
attack(3.5)
walk(right,1)
attack(3.5)
walk(right,1)
attack(3.5)

walk(left,1)
walk(down, 3)
walk(right, 3)
attack(6.5)
walk(right,1)
attack(3.5)
walk(up,1)
attack(3.5)

walk(up,1)
attack(9.5)
walk(up,1)
attack(3.5)

walk(up,1)
walk(right,1)
attack(3.5)

walk(up,1)
walk(left,4)
attack(3.5)
walk(left,1)
attack(10.5)
cmd.walk('quit')

end_time = time.time()
print('done! use ',int(end_time-start_time),'秒')