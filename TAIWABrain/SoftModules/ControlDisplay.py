import os
import time

def system_details():
    os.system('xrandr -q')    

def rotate_left():
    os.system('xrandr --output HDMI1 --rotate left')

def rotate_right():
    os.system('xrandr --output HDMI1 --rotate right')
    
def rotate_inverted():
    os.system('xrandr --output HDMI1 --rotate inverted')            

def rotate_normal():
    os.system('xrandr --output HDMI1 --rotate normal')    

def mirror_image():
    os.system('xrandr --output HDMI1 --reflect x')

