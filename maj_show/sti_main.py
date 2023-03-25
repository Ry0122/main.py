import sys
import time
from loguru import logger
from StimulationController import StimulationControl

sys.path.append('.')

if __name__ == '__main__':
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    logger.add(sink=fr'./log/stimulation-system-{date}.log', level="INFO", retention='1 week')

    stim = StimulationControl()
    stim.start()