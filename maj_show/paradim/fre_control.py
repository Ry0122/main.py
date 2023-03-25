import decimal
import random

import numpy as np

from psychopy import visual, core, event


class StimulationControl:

    def __init__(self):
        self.time = np.empty((40, 1), dtype=np.float64)
        self.frequency = np.empty((40, 1), dtype=np.float64)
        self.second_temp = np.empty((40, 1), dtype=np.float64)
        self.second = np.empty((40, 1), dtype=np.float64)
        self.opacity = np.empty((40, 1), dtype=np.float64)
        for i in range(0, 40, 1):
            self.time[i] = 0.0
            self.frequency[i] = 8 + i * 0.2
            self.second_temp[i] = self.second[i] = float(1 / self.frequency[i])
            self.opacity[i] = 0.0
            # print(i)
            # print(self.frequency[i])
            # print(self.second_temp[i])
            # print(self.second[i])

    def opacity_refresh(self, number):

        for i in range(0, number, 1):
            self.time[i] = self.time[i] + float(1 / 60)
            # print(i)
            # print(self.time[i])
            # print(self.second_temp[i])
            if self.time[i] >= self.second_temp[i]:
                self.second_temp[i] = self.second_temp[i] + self.second[i]
                if self.second_temp[i] > self.second[i] * self.frequency[i]:
                    self.second_temp[i] = self.second[i]
                # self.opacity[i] = np.sin(0.5 * np.pi * self.time[i])
                # temp = random.uniform(1, 5)
                # self.opacity[i] = np.sin(0.5 * np.pi * (self.time[i]*2))
                self.opacity[i] = self.opacity[i] + 0.125
                if self.opacity[i] > 1:
                    self.opacity[i] = 0
            if self.time[i] >= self.second[i] * self.frequency[i]:
                self.time[i] = self.time[i] - 1
            # print(self.second_temp[1])
