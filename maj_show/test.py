import os

from psychopy import visual, core

frames_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'res')
background = os.path.join(frames_file_path, 'background.png')
window = visual.Window(size=(2560, 1536), units='pix', color=(-1, -1, -1), pos=(0, 0),
                                    useFBO=True, allowStencil=True, screen=0)
back = visual.ImageStim(window, image = background, pos=(-400, 240), units='pix',size=(1200,720))

display_mode_selection_txt1 = visual.TextStim(win=window, text='打牌', height=27, color='#FFFFFF',
                                              pos=(-300, -100), units='pix', bold=True, )
display_mode_selection_txt2 = visual.TextStim(win=window, text='摸牌', height=27, color='#FFFFFF',
                                              pos=(-200, -100), units='pix', bold=True, )
display_mode_selection_txt3 = visual.TextStim(win=window, text='胡牌', height=27, color='#FFFFFF',
                                              pos=(-100, -100), units='pix', bold=True, )
display_mode_selection_txt4 = visual.TextStim(win=window, text='碰牌', height=27, color='#FFFFFF',
                                              pos=(0, -100), units='pix', bold=True, )
rect1 = visual.Rect(win=window, units="pix", width=70, height=30, lineWidth=2,
                    interpolate='True',  # 消除锯齿
                    fillColor='#000000', lineColor='#808080', pos=(-300, -100), )
rect2 = visual.Rect(win=window, units="pix", width=70, height=30, lineWidth=2,
                    interpolate='True',  # 消除锯齿
                    fillColor='#000000', lineColor='#808080', pos=(-200, -100), )
rect3 = visual.Rect(win=window, units="pix", width=70, height=30, lineWidth=2,
                    interpolate='True',  # 消除锯齿
                    fillColor='#000000', lineColor='#808080', pos=(-100, -100), )
rect4 = visual.Rect(win=window, units="pix", width=70, height=30, lineWidth=2,
                    interpolate='True',  # 消除锯齿
                    fillColor='#000000', lineColor='#808080', pos=(0, -100), )

back.draw()

rect1.draw()
rect2.draw()
rect3.draw()
rect4.draw()

display_mode_selection_txt1.draw()
display_mode_selection_txt2.draw()
display_mode_selection_txt3.draw()
display_mode_selection_txt4.draw()
for x in range(11, 19, 1):
    piece_n = '{}.png'.format(x)
    piece_picture = os.path.join(frames_file_path, 'nan',piece_n)
    piece = visual.ImageStim(window, piece_picture, anchor='center', units='pix',
                             pos=(-1400 + 53 * x,  0 ))
    piece.draw()

window.flip()
core.wait(5)
window.close()
core.quit()


