from pickle import FALSE


class Nabeatsu:
    def __init__(self, foolish_num, num):
        self.foolish_num = foolish_num
        self.num = num

    def is_foolish(self):
        flg = False
        if self.num == 0:
            flg == False
        # foolish_numの倍数
        elif self.num % self.foolish_num == 0:
            flg = True
        # foolish_numがつく数字
        elif str(self.foolish_num) in str(self.num):
            flg = True
        return flg
