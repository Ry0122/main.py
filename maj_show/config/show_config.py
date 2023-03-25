class showconfig:
    """
    该配置文件为目标SSVEP范式的配置文件
    """
    # trial开始trigger，对应40个刺激目标
    # 此处直接使用刺激目标trigger作为trial开始trigger
    TRIAL_START_TRIGGER = [trigger for trigger in range(1, 41)]

    # trial结束trigger
    TRIAL_END_TRIGGER = 241

    # block开始trigger
    BLOCK_START_TRIGGER = 242

    # block结束trigger
    BLOCK_END_TRIGGER = 243

    # 数据记录开始trigger
    RECORD_START_TRIGGER = 250

    # 数据记录结束trigger
    RECORD_END_TRIGGER = 251

    # 刺激事件，对应40个刺激目标
    STIMULATION_EVENT = [stim_event for stim_event in range(1, 41)]

    # block数量
    BLOCK_NUMBER = 3

    # 一个block中的trial数量
    TRIAL_NUMBER = 40

    # 实验开始前的等待时长
    RECORD_START_WAIT_TIME = 30

    # 实验结束后的等待时长
    RECORD_END_WAIT_TIME = 30

    # block开始时的等待时长
    BLOCK_START_WAIT_TIME = 5

    # trial开始时的等待时长
    TRIAL_START_WAIT_TIME = 1

    # trial结束时的等待时长
    TRIAL_END_WAIT_TIME = 1

    # 刺激目标位置
    # STIM_TARGET_POSITION = []
    # for i in range(10):
    #     STIM_TARGET_POSITION.append((-834 + 184 * i, 260))
    # for i in range(10):
    #     STIM_TARGET_POSITION.append((-834 + 184 * i, 260 - 222))
    # for i in range(10):
    #     STIM_TARGET_POSITION.append((-834 + 184 * i, 260 - 222 * 2))
    # for i in range(10):
    #     STIM_TARGET_POSITION.append((-834 + 184 * i, 260 - 222 * 3))
    STIM_TARGET_POSITION = [(-834, 260), (-650, 260), (-466, 260), (-282, 260), (-98, 260), (86, 260), (270, 260), (454, 260), (638, 260), (822, 260),
                            (-834, 38), (-650, 38), (-466, 38), (-282, 38), (-98, 38), (86, 38), (270, 38), (454, 38), (638, 38), (822, 38),
                            (-834, -184), (-650, -184), (-466, -184), (-282, -184), (-98, -184), (86, -184), (270, -184), (454, -184), (638, -184), (822, -184),
                            (-834, -406), (-650, -406), (-466, -406), (-282, -406), (-98, -406), (86, -406), (270, -406), (454, -406), (638, -406), (822, -406)]


if __name__ == '__main__':
    print(StimulationConfig.STIM_TARGET_POSITION)
