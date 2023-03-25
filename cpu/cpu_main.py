import sys
import time
from loguru import logger
from cpu.cpu_control import ActionControl

sys.path.append('.')

if __name__ == '__main__':
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    logger.add(sink=fr'./log/cpu-system-{date}.log', level="INFO", retention='1 week')

    cpu = ActionControl()
    cpu.start()