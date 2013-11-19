# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:50:58 2013

@author: zeng
"""

from PIL import Image,ImageDraw,ImageFont
import os


def getCharList(filename):
    clist = set()
    for line in file(filename):
        chars = line.strip().split(' ')
        for char in chars:
            clist.add(char)
    print clist
    return clist
    
def getFonts():
    fontPath = './fonts'
    fontList = os.listdir(fontPath)
    fonts = []
    for f in fontList:
        font = ImageFont.truetype(os.path.join(fontPath,f),size = 40)
        fonts.append((font,f))
        
    return fonts
    
    
    
def drawChar(char,font):
    img = Image.new('1',(40,40),255)
    draw = ImageDraw.Draw(img)
    draw.text((0,-3),u'%s'%char,font=font[0])
    savePath = './image'
    filePath = os.path.join(savePath,u'%s'%char)
    os.makedirs(filePath)
    filename = u'%s.png'%font[1]
    filename = os.path.join(filePath,filename)
    img.save(filename)
    
if __name__ == '__main__':
    clist = getCharList('a')
    fonts = getFonts()
    while len(clist):
        c = clist.pop()
        for f in fonts:
            drawChar(c,f)
    
    
        
    
    
    