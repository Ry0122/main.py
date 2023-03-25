import threading
import time
from psychopy import visual, event, core
import random
import os
from loguru import logger
from StimulationSystem.paradigm.config.stimulation_config import StimulationConfig
frames_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'res')
stim_frames = []
frame_num = 0

window = visual.Window(size=(1920, 1080), units='pix', pos=(0, 0),
                                        useFBO=True, allowStencil=True, screen=0)
stim_frames_num = 10  #扫描所有的牌序号
for num in range(stim_frames_num):
    frame_path = os.path.join(frames_file_path, 'nan', '1{}.png'.format(num))
    stim_frames.append(visual.ImageStim(win=window, image=frame_path))

while frame_num <= 10:
    stim_frame = stim_frames[frame_num]
    stim_frame.draw()
    window.flip()
    # 刺激过程中显示提示三角可能会导致刺激不稳定，如需在刺激过程中设置提示请测试刺激稳定性
    # self.__draw_target_tip(stim_target)
    frame_num = frame_num + 1
    core.wait(1)
