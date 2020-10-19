import sys
import time

def delay_print(intro_text, s, a):
    print(intro_text)
    for i in s:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.3)
    print(a)
    time.sleep(0.5)


def slow_print(txt_speed, text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(txt_speed)


def atk_txt(attacker, reciever, text):
    print(f'{attacker} attackerar {reciever} ')
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.3)
    print(''' 
          |
O=========|>>>>>>>>>>>>>>>>>>>>>>>>>>
          |
       ''')
    time.sleep(0.5)