import os

from loguru import logger
from psychopy import visual

from maj_show.sticontrol import StimulationControl
from maj_show.paradim.frequence import Frequence


class SSVEP:
    # def __init__(self, trigger_controller):
    #
    #     # trigger控制
    #     self.trig_ctrl = trigger_controller
    #     self.trig_ctrl.open()
    #
    #     # 实验结束flag
    #     self.finish_experiment_flag = False
    #
    #     # block轮次
    #     self.block_num = 0
    #
    #     # 当前阶段执行函数
    #     self.cur_step_func = self.start_interface_drawing
    #
    #     # 刺激事件
    #     self.stim_event: list = StimulationConfig.STIMULATION_EVENT
    #
    #     # trial开始trigger
    #     self.trial_start_trig: list = StimulationConfig.TRIAL_START_TRIGGER
    #
    #     # 刺激结束输出trigger
    #     self.trial_end_trig: int = StimulationConfig.TRIAL_END_TRIGGER
    #
    #     # block启动输出trigger
    #     self.block_start_trig: int = StimulationConfig.BLOCK_START_TRIGGER
    #
    #     # block结束输出trigger
    #     self.block_end_trig: int = StimulationConfig.BLOCK_END_TRIGGER
    #
    #     # 数据开始记录trigger
    #     self.record_start_trig: int = StimulationConfig.RECORD_START_TRIGGER
    #
    #     # 数据停止记录trigger
    #     self.record_end_trig: int = StimulationConfig.RECORD_END_TRIGGER
    #
    #     # 刺激帧文件路径
    #     self.frames_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'stimulation_generate')
    #
    #     # 初始化帧
    #     self.init_frame = None
    #
    #     # 刺激帧
    #     self.stim_frames = []
    #
    #     # 窗口
    #     self.window = None
    #
    #     # 刺激目标序列
    #     self.stim_target_order = None
    #
    #     # 当前trial
    #     self.cur_trial_num = 0
    #
    #     # 所有刺激目标的位置
    #     self.stim_target_pos = StimulationConfig.STIM_TARGET_POSITION
    #
    #     # 反馈结果
    #     self.feedback_result = None
    def __init__(self):
        # 刺激帧文件路径
        self.i = 0
        self.window = None
        self.frames_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'pythonProject1')
        self.cur_step_func = self.initial_game
        self.finish_experiment_flag = False
        self.chess_color = 'black'
        self.distance = 170
        self.fre_control5 = StimulationControl()
        self.red = 3
        self.black = 4
        self.fre_control40 = StimulationControl()
        self.fre_opa = Frequence()
        self.chess_map = []
        self.combat_mode = None
        self.command = False
        self.state_flag = None
        self.selected_flag = None
        self.mode_pos = None
        self.selected_piece_row = None
        self.selected_piece_line = None

    def run(self):  # 游戏开始
        logger.info('刺激范式开始运行')

        while not self.finish_experiment_flag:
            self.cur_step_func()

    def finish_experiment(self):  # 实验完成
        self.finish_experiment_flag = True
        logger.info('实验结束')

    def close(self):  # 关闭游戏界面
        # 停止刺激
        self.finish_experiment_flag = True
        # self.finish_experiment()
        # 关闭psychopy窗口
        self.window.close()
        # 关闭trigger
        # self.trig_ctrl.close()

    # create a window
    def initial_game(self):
        # self.window = visual.Window(size=(2560, 1600), units='pix', color=(-1, -1, -1), pos=(0, 0),
        # useFBO=True, allowStencil=True, screen=0, fullscr=True)
        self.window = visual.Window(size=(2560, 1600), units='pix', color=(-1, -1, -1), pos=(0, 0),
                                    useFBO=True, allowStencil=True, screen=0)

        init_txt = visual.TextStim(win=self.window, text='游戏加载中，请稍后...', height=100, color='white',
                                   pos=(-260, 0), units='pix', font='STCAIYUN', bold=True)

        init_txt.draw()
        self.window.flip()  # 界面翻转替换
        self.cur_step_func = self.gmae_drawing

    def game_drawing(self):
        self.command = False
        background = os.path.join(self.frames_file_path,'res', 'background.png')

        pic1 = visual.ImageStim(self.window, background, anchor='center', units='pix')

        display_mode_selection_txt1 = visual.TextStim(win=self.window, text='打牌', height=27, color='#FFFFFF',
                                                      pos=(-300, -650), units='pix', bold=True, )
        display_mode_selection_txt2 = visual.TextStim(win=self.window, text='摸牌', height=120, color='#FFFFFF',
                                                      pos=(-500, -650), units='pix', bold=True, )
        display_mode_selection_txt3 = visual.TextStim(win=self.window, text='胡牌', height=120, color='#FFFFFF',
                                                      pos=(-700, -650), units='pix', bold=True, )
        display_mode_selection_txt4 = visual.TextStim(win=self.window, text='碰牌', height=120, color='#FFFFFF',
                                                      pos=(-900, -650), units='pix', bold=True, )
        rect1 = visual.Rect(win=self.window, units="pix", width=600, height=180, lineWidth=4,
                            interpolate='True',  # 消除锯齿
                            fillColor='#000000', lineColor='#808080', pos=(-300, -650), )
        rect2 = visual.Rect(win=self.window, units="pix", width=70, height=30, lineWidth=4,
                            interpolate='True',  # 消除锯齿
                            fillColor='#000000', lineColor='#808080', pos=(-500, -650), )
        rect3 = visual.Rect(win=self.window, units="pix", width=70, height=30, lineWidth=4,
                            interpolate='True',  # 消除锯齿
                            fillColor='#000000', lineColor='#808080', pos=(-700, -650), )
        rect4 = visual.Rect(win=self.window, units="pix", width=70, height=30, lineWidth=4,
                            interpolate='True',  # 消除锯齿
                            fillColor='#000000', lineColor='#808080', pos=(-900, -650), )


        while not self.command:
            rect1.opacity = 0.5
            rect2.opacity = 0.5
            rect3.opacity = 0.5
            rect4.opacity = 0.5

            pic1.draw()

            rect1.draw()
            rect2.draw()
            rect3.draw()
            rect4.draw()

            display_mode_selection_txt1.draw()
            display_mode_selection_txt2.draw()
            display_mode_selection_txt3.draw()
            display_mode_selection_txt4.draw()

            self.red = 3
            self.black = 4
            self.maj_create()
            self.action_create()
            #如果牌已经被选择
            if self.selected_flag == 1:
                self.cur_step_func = self.select_one()



    def select_one(self):
        self.command = False
        background = os.path.join(self.frames_file_path, 'res', 'background.png')

        pic1 = visual.ImageStim(self.window, background, anchor='center', units='pix')

        display_mode_selection_txt1 = visual.TextStim(win=self.window, text='打牌', height=27, color='#FFFFFF',
                                                      pos=(-300, -650), units='pix', bold=True, )
        display_mode_selection_txt2 = visual.TextStim(win=self.window, text='摸牌', height=120, color='#FFFFFF',
                                                      pos=(-500, -650), units='pix', bold=True, )
        display_mode_selection_txt3 = visual.TextStim(win=self.window, text='胡牌', height=120, color='#FFFFFF',
                                                      pos=(-700, -650), units='pix', bold=True, )
        display_mode_selection_txt4 = visual.TextStim(win=self.window, text='碰牌', height=120, color='#FFFFFF',
                                                      pos=(-900, -650), units='pix', bold=True, )
        rect1 = visual.Rect(win=self.window, units="pix", width=600, height=180, lineWidth=4,
                            interpolate='True',  # 消除锯齿
                            fillColor='#000000', lineColor='#808080', pos=(-300, -650), )
        rect2 = visual.Rect(win=self.window, units="pix", width=70, height=30, lineWidth=4,
                            interpolate='True',  # 消除锯齿
                            fillColor='#000000', lineColor='#808080', pos=(-500, -650), )
        rect3 = visual.Rect(win=self.window, units="pix", width=70, height=30, lineWidth=4,
                            interpolate='True',  # 消除锯齿
                            fillColor='#000000', lineColor='#808080', pos=(-700, -650), )
        rect4 = visual.Rect(win=self.window, units="pix", width=70, height=30, lineWidth=4,
                            interpolate='True',  # 消除锯齿
                            fillColor='#000000', lineColor='#808080', pos=(-900, -650), )

        while not self.command:
            rect1.opacity = 0.5
            rect2.opacity = 0.5
            rect3.opacity = 0.5
            rect4.opacity = 0.5

            pic1.draw()

            rect1.draw()
            rect2.draw()
            rect3.draw()
            rect4.draw()

            display_mode_selection_txt1.draw()
            display_mode_selection_txt2.draw()
            display_mode_selection_txt3.draw()
            display_mode_selection_txt4.draw()

            self.red = 3
            self.black = 4
            self.maj_create()
            self.action_create()


    def action_create(self):
        for x in range(11, 13, 1):
            piece_n = '{}.png'.format(x)
            piece_picture = os.path.join(self.frames_file_path, 'nan', piece_n)
            piece = visual.ImageStim(self.window, piece_picture, anchor='center', units='pix',
                                     pos=(-1400 + 53 * x, 100))
            piece.draw()


    def maj_create(self):
        for x in range(11, 19, 1):
            piece_n = '{}.png'.format(x)
            piece_picture = os.path.join(self.frames_file_path, 'nan', piece_n)
            piece = visual.ImageStim(self.window, piece_picture, anchor='center', units='pix',
                                     pos=(-1400 + 53 * x, 0))
            piece.draw()

