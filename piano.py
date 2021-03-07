from threading import Thread
import pygame as pg
import time

nodL = [0]
fibs = [0,1]

errection = []

pg.mixer.init()
pg.init()

def play_notes(path, dur=0.3):
    time.sleep(dur)
    pg.mixer.Sound(path).play()
    time.sleep(dur)

pth = r'C:\Users\ACER\Desktop\mp3shit\mp3'

def appenddeeznuts(lily):
    girth = len(lily)
    for i in range(1,girth+1):
        #print(lily[girth-i])
        nodL.append(lily[girth-i])
    errection.clear()

def eklachalore(x):
    lon = 1
    while(True):
        try:
            lon/x
        except(TypeError, ZeroDivisionError):
            break
        else:
            lon = x%10
            errection.append(lon)
        x= int((x-lon)/10)
    #print(errection)
    appenddeeznuts(errection)

def fibocs():
    i=0
    while i<100:
        a = fibs[i] +fibs[i+1]
        #print(a)
        fibs.append(a)
        i=i+1

def letsdoeit():
    fibocs()
    for o in fibs:
        eklachalore(o)
    for t in nodL:
        play_notes(pth + '\{}.mp3'.format(t))

letsdoeit()


