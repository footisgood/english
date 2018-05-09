import pygame
from pygame.locals import *
import random
import time
import win32com.client

def display(word,p1):   #z  显示WORD单词，p1个前是已打的正确的
    global maxspeed
    screen.blit(background, (0, 0))
    s1=s_now[:p1]
    s2=s_now[p1:]
    text_surface = my_font.render(s1, True, (200, 0, 0))
    screen.blit(text_surface, (100, 100))
    t = text_surface.get_rect()
    text_surface1 = my_font.render(s2, True, (170, 255, 0))
    screen.blit(text_surface1,(100+t.width,100))
    end=time.clock()
    costtime=end-start
    speed=n_all / costtime * 60
    if speed>maxspeed :
        maxspeed = speed
    s_time='Time:%.2fs    |||   Count:%d     |||   Speed:%.1f letters/min   '%(costtime , count , speed )
    text_surface2=font_time.render(s_time , True , (0,0,0))
    screen.blit(text_surface2,(180,10))
    text_surface3= font_time.render('MAX SPEED = %.2f'%(maxspeed) , True, (255, 0 , 0))
    screen.blit(text_surface3, (560,10))
    pygame.display.update()

def pickupanddisplay():  #挑选一个新的单词s_now ， 并在指针至于0，然后显示出来
    global s_now , p_s , count
    count += 1
    s_now=random.choice(data)
    p_s = 0
    display(s_now , p_s)
    speak.Speak(s_now)

#main pro
pygame.init()
screen = pygame.display.set_mode((760, 480), 0, 32)
# 设置帧率（屏幕每秒刷新的次数）
FPS = 60
# 获得pygame的时钟
fpsClock = pygame.time.Clock()

my_font = pygame.font.SysFont('arial' , 56)
font_time = pygame.font.SysFont('arial' , 13)
background = pygame.image.load("back.jpg").convert()
speak = win32com.client.Dispatch('SAPI.SPVOICE')

f=open('data.txt' , 'r' , encoding='utf-8').read()
data=f.split('\n')
print (data)
start=time.clock()
count , n_all , maxspeed = [0 , 0 , 0]  #count是打了几个单词，n_all是总共正确打了几个字母
pickupanddisplay()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            pressed_keys = pygame.key.get_pressed()
            print (chr(event.key) , end=' ')

            if pressed_keys[ord(s_now[p_s].lower())]:
                p_s += 1
                n_all += 1
                display(s_now , p_s)
                if p_s == len(s_now) :
                    print ('c...')
                    pickupanddisplay()
            elif event.key == 127:
                start = time.clock()
                n_all, maxspeed = [0, 0]  # count是打了几个单词，n_all是总共正确打了几个字母
    display(s_now , p_s)
    fpsClock.tick(FPS)