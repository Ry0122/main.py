from tkinter import *
import random
from threading import Timer
import time
import operator
from tkinter.messagebox import *
from ma_cpu import cpu




win = Tk()  # 创建窗口对象
win.title("Game")  # 设置窗口标题
cpu().BeginGame()  # 开始游戏，玩家先出牌
win.mainloop()
