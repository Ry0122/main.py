import threading
import time
from psychopy import visual, event, core
import random
import os
from loguru import logger
from StimulationSystem.paradigm.config.stimulation_config import StimulationConfig


class SSVEP:
    def __init__(self, trigger_controller):
        # trigger控制
        self.trig_ctrl = trigger_controller
        self.trig_ctrl.open()

        # 实验结束flag
        self.finish_experiment_flag = False

        # block轮次
        self.block_num = 0

        # 当前阶段执行函数
        self.cur_step_func = self.init_step_func

        # 刺激事件
        self.stim_event: list = StimulationConfig.STIMULATION_EVENT

        # trial开始trigger
        self.trial_start_trig: list = StimulationConfig.TRIAL_START_TRIGGER

        # 刺激结束输出trigger
        self.trial_end_trig: int = StimulationConfig.TRIAL_END_TRIGGER

        # block启动输出trigger
        self.block_start_trig: int = StimulationConfig.BLOCK_START_TRIGGER

        # block结束输出trigger
        self.block_end_trig: int = StimulationConfig.BLOCK_END_TRIGGER

        # 数据开始记录trigger
        self.record_start_trig: int = StimulationConfig.RECORD_START_TRIGGER

        # 数据停止记录trigger
        self.record_end_trig: int = StimulationConfig.RECORD_END_TRIGGER

        # 刺激帧文件路径
        self.frames_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'res')

        # 初始化帧
        self.init_frame = None

        # 刺激帧
        self.stim_frames = []

        # 窗口
        self.window = None

        # 刺激目标序列
        self.stim_target_order = None

        # 当前trial
        self.cur_trial_num = 0

        # 所有刺激目标的位置
        self.stim_target_pos = StimulationConfig.STIM_TARGET_POSITION

        # 反馈结果
        self.feedback_result = None

        def run(self):
            logger.info('刺激范式开始运行')
            while not self.finish_experiment_flag:
                self.cur_step_func()

        def finish_experiment(self):
            self.finish_experiment_flag = True
            logger.info('实验结束')

        def close(self):
            # 停止刺激
            self.finish_experiment()

            # 关闭psychopy窗口
            self.window.close()

            # 关闭trigger
            self.trig_ctrl.close()

        def init_step_func(self):
            """
            刺激的初始化阶段函数
            """
            logger.info('进入刺激初始化阶段')

            # 定义psychopy窗口
            self.window = visual.Window(size=(1920, 1080), units='pix', color=(-1, -1, -1), pos=(0, 0),
                                        useFBO=True, allowStencil=True, fullscr=True, screen=0)

            # 显示系统初始化文本
            init_txt = visual.TextStim(win=self.window, text='游戏即将开始，请保持放松', height=60, color='white',
                                       pos=(-80, 0), units='pix')
            init_txt.draw()
            self.window.flip()

            # 加载初始化帧
            self.init_frame = os.path.join(self.frames_file_path, 'background.png')

            # 加载刺激帧
            stim_frames_num = 13  #扫描所有的牌序号
            for num in range(stim_frames_num):
                frame_path = os.path.join(self.frames_file_path, 'nan', '11.png'.format(num))
                self.stim_frames.append(visual.ImageStim(win=self.window, image=frame_path))

            # 发送数据开始记录trigger
            self.trig_ctrl.send(self.record_start_trig)
            logger.info('发送数据开始记录trigger')



