class huMain():

    def __init__(self):  # 构造函数
        # 定义手中的牌int allPai[4][10]
        self.allPai = [[6, 1, 4, 1, 0, 0, 0, 0, 0, 0],  # 桶
                       [3, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # 条
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 万
                       [5, 2, 3, 0, 0, 0, 0, 0, 0, 0]]  # 字

    # 判断是否胡牌的函数
    def Win(self, allPai):
        jiangPos = 0  # “将”的位置
        # yuShu		#余数
        jiangExisted = False
        # 第一步 是否满足3,3,3,3,2模型
        for i in range(0, 4):
            yuShu = allPai[i][0] % 3
            if yuShu == 1:
                return False
            if yuShu == 2:
                if jiangExisted == True:
                    return False
                jiangPos = i  # “将”在那行
                jiangExisted = True

        # 不含将处理
        for i in range(0, 4):
            if i != jiangPos:
                if not self.Analyze(allPai[i], i == 3):
                    return False

        # 该类牌中要包含将,因为要对将进行轮询,效率较低,放在最后
        success = False  # 指示除掉“将”后能否通过
        for j in range(1, 10):  # 对列进行操作,用j表示
            if (allPai[jiangPos][j] >= 2):
                # 除去这2张将牌
                allPai[jiangPos][j] -= 2
                allPai[jiangPos][0] -= 2
                if self.Analyze(allPai[jiangPos], jiangPos == 3):
                    success = True
                # 还原这2张将牌
                allPai[jiangPos][j] += 2
                allPai[jiangPos][0] += 2
                if success == True:
                    break
        return success

    # 分解成“刻”“顺”组合
    def Analyze(self, aKindPai, ziPai):  # (int []aKindPai,Boolean ziPai)
        if aKindPai[0] == 0:
            return True
        # 寻找第一张牌
        for j in range(1, 10):
            if aKindPai[j] != 0:
                break
        if aKindPai[j] >= 3:  # 作为刻牌
            # 除去这3张刻牌
            aKindPai[j] -= 3
            aKindPai[0] -= 3
            result = self.Analyze(aKindPai, ziPai)
            # 还原这3张刻牌
            aKindPai[j] += 3
            aKindPai[0] += 3
            return result
        # 作为顺牌
        if (not ziPai) and (j < 8) and (aKindPai[j + 1] > 0) and (aKindPai[j + 2] > 0):
            # 除去这3张顺牌
            aKindPai[j] -= 1
            aKindPai[j + 1] -= 1
            aKindPai[j + 2] -= 1
            aKindPai[0] -= 3
            result = self.Analyze(aKindPai, ziPai)
            # 还原这3张顺牌
            aKindPai[j] += 1
            aKindPai[j + 1] += 1
            aKindPai[j + 2] += 1
            aKindPai[0] += 3
            return result
        return False
# ----------------------------------class huMain() end
