#可以实现麻将牌正面，背面显示以及移动的功能   
class  Card():
        
    #构造函数，参数type指定牌的类型，参数num指定牌的点数
    def __init__(self,cardtype,num):
        self.m_nType = cardtype      #牌的类型 饼=1 条=2 万=3 字牌=4
        self.m_nNum= num            #牌的点数（1到9）
        #根据牌的类型及编号来设置牌文件的路径及文件名
        if self.m_nType==1 :#桶（饼）
            FrontURL = "res/nan/1"
        elif self.m_nType== 2 :#条
            FrontURL = "res/nan/2"
        elif self.m_nType== 3 :#万
            FrontURL = "res/nan/3"
        elif self.m_nType== 4 :#字牌
            FrontURL = "res/nan/4"
        self.imageID = self.m_nType * 10 + self.m_nNum # 牌自己图像编号ID
        FrontURL = FrontURL + str(self.m_nNum)#URL地址
        FrontURL = FrontURL + ".png"

    def getImageID(self):# 牌自己图像编号ID
        return self.imageID
#------------------------------------Card end